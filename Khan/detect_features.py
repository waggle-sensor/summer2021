import statistics

import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from skimage.filters.rank import entropy
from skimage.morphology import disk
import math


def display(image_to_display):
    cv2.imshow("image", image_to_display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_hsv(hsv_image, image):
    # TODO: create track bar
    # Default values that can be used for lower and upper limit of hsv
    lower_hue = 90
    upper_hue = 130
    lower_sat = 0
    upper_sat = 255
    lower_val = 0
    upper_val = 255

    lower_limit = np.array([lower_hue, lower_sat, lower_val])
    upper_limit = np.array([upper_hue, upper_sat, upper_val])

    mask = cv2.inRange(hsv_image, lower_limit, upper_limit)

    res = cv2.bitwise_and(image, image, mask = mask)

    display(image)
    display(mask)
    display(res)

def find_mean_hsv(hsv_image):

    # hsv_image[...,0] is all the values that represent the hue
    # same for saturation and value
    '''
        Hue is in a circle [0, 180] because of this
        so,
        convert hue angles to a set of vectors from polar to cartesian coordinates
        after taking mean of those coordinates, convert back to polar form
    '''

    hsv_1D = hsv_image[...,0].flatten()

    x_list = []
    y_list = []

    for i in range(len(hsv_1D)):

        # convert to a [0, 360] hue range
        hsv_1D[i] *= 2

        angle_x = math.radians(hsv_1D[i])
        angle_y = math.radians(hsv_1D[i])

        # convert to rectangular cartesian coordinates
        x = math.cos(angle_x)
        y = math.sin(angle_y)

        x_list.append(x)
        y_list.append(y)

    x_mean = statistics.mean(x_list)
    y_mean = statistics.mean(y_list)

    # convert back to polar coordinates
    mean_angle = ((math.atan(y_mean / x_mean)) * 180) / math.pi

    # check quadrant
    if ((x_mean < 0 and y_mean < 0) | (x_mean < 0 and y_mean > 0)):
        mean_angle += 180
    elif (x_mean > 0 and y_mean < 0):
        mean_angle += 360

    # convert back to hsv scale
    mean_hue = mean_angle / 2

    mean_sat = hsv_image[..., 1].mean() # a measure of how intense or pure the colors of the scene are on avg
    mean_val = hsv_image[...,2].mean() # a measure of the avg luminance of a scene

    mean_hsv = [mean_hue, mean_sat, mean_val]

    hsv_image[...,0] = mean_hue
    hsv_image[...,1] = mean_sat
    hsv_image[...,2] = mean_val

    return mean_hsv

def computeSD(list):
    return np.std(list)

def find_standard_deviation_hsv(hsv_image):

    hue_1D = hsv_image[...,0].flatten()
    sat_1D = hsv_image[...,1].flatten()
    val_1D = hsv_image[...,2].flatten()

    hue_SD = computeSD(hue_1D)
    sat_SD = computeSD(sat_1D)
    val_SD = computeSD(val_1D)

    SD_hsv = [hue_SD, sat_SD, val_SD]

    return SD_hsv

# When using canny edge detection you have to take into account the thresholds
def detect_edges(image):
    # figure out correct thresholds (use track bar?)
    canny = cv2.Canny(image, 200, 0, 200)
    canny_image_0_200 = cv2.Canny(image, 0, 200)
    canny_image_199_300 = cv2.Canny(image, 0, 1000)
    #display(canny_image_0_200)
   # display(canny_image_199_300)
    #display(canny)

    return canny_image_199_300

'''
    "Research suggests that people prefer curve contours to sharp contours" 
    according to the research paper "The Nature-Disorder Paradox: A Perceptual Study on How Nature Is
                                     Disorderly Yet Aesthetically Preferred"
'''
def detect_curved_contours():
    print("Detect curved contours")


def find_straight_edge_density(image):
  '''
  Find a measure of how many straight edges are in the scene image
  uses Hough Line Transform method
  :return: number of lines
  '''

  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  edges = cv2.Canny(gray_image,100 ,200)
  cv2.imshow('img', image)
  cv2.imshow('edges', edges)

  hough_lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 100, minLineLength = 80, maxLineGap = 4)

  for line in hough_lines:
      x1, y1, x2, y2 = line[0]
      cv2.line(image, (x1, y1), (x2, y2), (0, 255, 0), 1)

  display(image)

  print(len(hough_lines))
  return len(hough_lines)


'''How much of the image is edges
  (total num of edge pixels / total num of pixels) ----> confirm if this is the correct idea

  Am I supposed to measure the length of the edges?
  
  Write more test cases so I can make sure this is accurate
'''
def find_edge_density(image):

    edges_image = detect_edges(image)

    total_pixels = edges_image.shape[0] * edges_image.shape[1] # rows times columns
    white_pixels = cv2.countNonZero(edges_image)

    edge_density_percentage = (white_pixels / total_pixels) * 100


    return edge_density_percentage

# The entropy or average information of an image is a measure of the degree of randomness in the image.
def find_entropy(image):
    p = np.array([(image--v).sum() for v in range(256)])
    p = p / p.sum()

    e = - (p * np.log2(p)).sum()

    # entr_img = entropy(hsv_image, disk(10))
    # display(entr_img)

    # entropy = []
    #
    # hist = cv2.calcHist([hsv_image], [0], None, [256], [0, 255])
    # total_pixel = hsv_image.shape[0] * hsv_image.shape[1]
    #
    # for item in hist:
    #     probability = item / total_pixel
    #     if probability == 0:
    #         en = 0
    #     else:
    #         en = -1 * probability * (np.log(probability) / np.log(2))
    #     entropy.append(en)
    #
    # sum_en = np.sum(entropy)

    # gray_image = rgb2gray(image)
    # entropy_image = entropy(gray_image, disk(5))

    print("Entropy:", e)

    return e


def main():
    file_path = 'images/image1.jpg'

    image = cv2.imread(file_path, 1)    # hue --> [0, 180], sat/val --> [0, 255]
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    #detect_hsv(hsv_image, image)
    #find_mean_hsv(hsv_image)
    #find_standard_deviation_hsv(hsv_image)
    #detect_curved_contours()
    #find_edge_density(image)
    find_straight_edge_density(image)
    find_entropy(image)

    ''' [x, y, hsv]  
        
    '''
    px = image[100, 0, 2]
    print(px)

if __name__ == '__main__':
    main()
