import statistics

import cv2
import numpy as np
from matplotlib import pyplot as plt
from skimage.color import rgb2gray
from skimage.filters.rank import entropy
from skimage.morphology import disk
import math


def display(image_to_display):
    '''
    Helper function that displays an image passed in
    :param image_to_display: image that needs to be displayed
    :return: void
    '''
    cv2.imshow("image", image_to_display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_hsv(hsv_image, image):
    '''
    Detects a certain color in image
    :param hsv_image: HSV image
    :param image:     BGR image
    :return: void
    '''
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

def find_mean_hue(hsv_image):
    '''

    Hue is in a circle [0, 180] because of this
    convert hue angles to a set of vectors from polar to cartesian coordinates
    after taking mean of those coordinates, convert back to polar form
    :param hsv_image:
    :return: mean hue
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

    return mean_hue

def find_mean_hsv(hsv_image):
    '''
    Computes the mean hue, saturation, and value of image given HSV image
    :param hsv_image:
    :return: mean hue, saturation, and value
    '''

    # hsv_image[...,0] is all the values that represent the hue
    # same for saturation and value

    mean_hue = find_mean_hue(hsv_image)
    mean_sat = hsv_image[..., 1].mean() # a measure of how intense or pure the colors of the scene are on avg
    mean_val = hsv_image[...,2].mean() # a measure of the avg luminance of a scene

    mean_hsv = [mean_hue, mean_sat, mean_val]

    hsv_image[...,0] = mean_hue
    hsv_image[...,1] = mean_sat
    hsv_image[...,2] = mean_val

    return mean_hsv

def find_standard_deviation_hsv(hsv_image):

    hue_1D = hsv_image[...,0].flatten()
    sat_1D = hsv_image[...,1].flatten()
    val_1D = hsv_image[...,2].flatten()

    hue_SD = np.std(hue_1D)
    sat_SD = np.std(sat_1D)
    val_SD = np.std(val_1D)

    SD_hsv = [hue_SD, sat_SD, val_SD]

    return SD_hsv

# When using canny edge detection you have to take into account the thresholds
def detect_edges(image):
    # figure out correct thresholds (use track bar?)
    canny= cv2.Canny(image, 250, 400)
    #display(canny)

    return canny

def find_straight_edge_density(image):
  '''
  Find a measure of how many straight edges are in the scene image
  uses Hough Line Transform method
  :return: number of lines
  '''

  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  # Guassian blur

  # kernel = np.ones((5, 5), np.float32) / 25
  # gray_image = cv2.filter2D(gray_image, -1, kernel)

  # # blur the image while keeping the edges sharp
  #gray_image = cv2.bilateralFilter(gray_image, 9, 75, 75)

  fld = cv2.ximgproc.createFastLineDetector()

  lines = fld.detect(gray_image)

  draw_image = fld.drawSegments(image, lines)

  '''[
      [[line 1]]
      [line 2]]
      print(...)
  ]
  
  [line 1] ---> [xstart, ystart, xend, yend]
  
  so to find length use distance formula on every line segment and then add them together 
  '''

  sum_length = 0
  for i in range(len(lines)):
      x1 = lines[i][0][0]
      y1 = lines[i][0][1]
      x2 = lines[i][0][2]
      y2 = lines[i][0][3]

      length_line_segment = math.sqrt(((x2 - x1) ** 2) +  ((y2 - y1) ** 2))

      if (length_line_segment > 50):        # ignore line segments that are very small
          sum_length += length_line_segment
      else:
          lines[i][0][0] = 0
          lines[i][0][1] = 0
          lines[i][0][2] = 0
          lines[i][0][3] = 0

  # len(lines) will give you the number of lines

  display(draw_image)
  return sum_length

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

def find_entropy(image):
    '''
    The entropy or average information of an image is a measure of the degree of randomness in the image.
    :param image: BGR image
    :return: entropy
    '''

    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    image_1D = gray_image.flatten()

    length = image_1D.size
    symset = list(set(image_1D))
    nymsym = len(symset)
    propab = [np.size(image_1D[image_1D == i]) / (1.0 * length) for i in symset]
    entropy = np.sum([p * np.log2(1.0/p) for p in propab])

    return entropy

def remove_one_col_pixels(image):
    '''
    Helper method that removes one column of pixels from the right
    :param image: BGR image
    :return: the image with one column of pixels removed
    '''

    split = image.shape[1] - 1
    image = image[:, :split]

    return image

def calculate_symmetry(image):
    '''
    Calculates vertical reflectional symmetry
    :param image: BGR image
    :return: returns a decimal between 0 and 1, closer to 1 being more symmetry, closer to 0 being less symmetry
    '''

    #split image into two equal left and right parts

    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    ncols = image.shape[1]
    csplit = ncols // 2

    quadrants = [
        image[:, :csplit],  # left
        image[:, csplit:],  # right
    ]

    quadrants[1] = np.flip(quadrants[1], axis = 1)

    # make sure both sides of image are same size
    if (quadrants[0].shape[1] < quadrants[1].shape[1]):
        quadrants[1] = remove_one_col_pixels(quadrants[1])

    elif (quadrants[0].shape[1] > quadrants[1].shape[1]):
        quadrants[0] = remove_one_col_pixels(quadrants[0])

    # calculate symmetry
    intersection = cv2.bitwise_and(quadrants[0], quadrants[1])
    union = cv2.bitwise_or(quadrants[0], quadrants[1])
    symmetry = cv2.countNonZero(intersection) / cv2.countNonZero(union)

    symmetry = cv2.countNonZero(intersection) / (quadrants[0].shape[0] * quadrants[0].shape[1])

    return symmetry

def main():
    '''
     Computes features of images that would help measure visual disorder
    :return:
    '''

    file_path = 'images/image1.jpg'

    image = cv2.imread(file_path, 1)    # hue --> [0, 180], sat/val --> [0, 255]
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    detect_hsv(hsv_image, image)
    find_mean_hsv(hsv_image)
    find_standard_deviation_hsv(hsv_image)
    find_edge_density(image)
    find_straight_edge_density(image)
    find_entropy(image)
    calculate_symmetry(image)

    ''' [x, y, hsv]  
        
    '''
    px = image[100, 0, 2]
    print(px)

if __name__ == '__main__':
    main()
