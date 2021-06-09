import cv2
import numpy as np
from matplotlib import pyplot as plt
import math
import statistics


def display(image_to_display):
    cv2.imshow("image", image_to_display)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def detect_hsv(hsv_image, image):
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
    mean_hue = hsv_image[..., 0].mean() # a measure of the avg color appearance of a scene
    mean_sat = hsv_image[..., 1].mean() # a measure of how intense or pure the colors of the scene are on avg
    mean_val = hsv_image[...,2].mean() # a measure of the avg luminance of a scene

    mean_hsv = [mean_hue, mean_sat, mean_val]

    return mean_hsv
    print("Mean hue:", mean_hue, "Mean sat:", mean_sat, "Mean val:", mean_val)

    print("Hue SD:", hue_SD)
def find_standard_deviation_hsv(hsv_image):

    mean_hsv = find_mean_hsv(hsv_image)

    mean_hue = mean_hsv[0]

    print("Mean h:", mean_hue)


    #
    # sum = 0
    #
    # for i in range(len(hsv_image[...,0])):
    #     sub_mean = hsv_image[i] - mean_hue
    #
    #     sum += (sub_mean ** 2)

    # hue_SD = math.sqrt(sum)
    #
    # print("sum:", sum)
    #
    #
    # stat_hue_SD = statistics.stdev(hsv_image[...,0])
    #
    # print("Stat_hue_SD:", stat_hue_SD)
    #
    # print("Find standard deviation hsv")

def detect_edges(image):
    # figure out correct thresholds (use track bar?)
    canny_image = cv2.Canny(image, 100, 200)
    display(canny_image)

'''
    "Research suggests that people prefer curve contours to sharp contours" 
    according to the research paper "The Nature-Disorder Paradox: A Perceptual Study on How Nature Is
                                     Disorderly Yet Aesthetically Preferred"
'''
def detect_curved_contours():
    print("Detect curved contours")

def detect_edge_density():
    print("Detect edge density")



def main():
    file_path = 'images/image1.jpg'

    image = cv2.imread(file_path, 1)    # hue --> [0, 180], sat/val --> [0, 255]
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    detect_hsv(hsv_image, image)
    find_mean_hsv(hsv_image)
    find_standard_deviation_hsv(hsv_image)
    detect_edges(image) # using canny edge detection
    detect_curved_contours()

    print("image:", image)
    print("hsv_image:", hsv_image)


if __name__ == '__main__':
    main()
