import statistics
import cv2
import numpy as np
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

def find_mean_hue(hsv_image):
    '''
    Convert hue angles to a set of vectors from polar to cartesian coordinates
    after taking mean of those coordinates, convert back to polar form
    :param hsv_image: image in hsv format
    :return: mean hue
    '''

    hsv_1D = hsv_image[...,0].flatten()

    x_list = []
    y_list = []

    for i in range(len(hsv_1D)):

        hsv_1D[i] *= 2

        angle_x = math.radians(hsv_1D[i])
        angle_y = math.radians(hsv_1D[i])

        x = math.cos(angle_x)
        y = math.sin(angle_y)

        x_list.append(x)
        y_list.append(y)

    x_mean = statistics.mean(x_list)
    y_mean = statistics.mean(y_list)

    mean_angle = ((math.atan(y_mean / x_mean)) * 180) / math.pi

    if ((x_mean < 0 and y_mean < 0) or (x_mean < 0 and y_mean > 0)):
        mean_angle += 180
    elif (x_mean > 0 and y_mean < 0):
        mean_angle += 360

    mean_hue = mean_angle / 2

    return mean_hue

def find_mean_hsv(hsv_image):
    '''
    Computes the mean hue, saturation, and value of image given HSV image
    :param hsv_image: image in hsv format
    :return: mean hue, saturation, and value in list
    '''

    mean_hue = find_mean_hue(hsv_image)
    mean_sat = hsv_image[..., 1].mean()
    mean_val = hsv_image[...,2].mean()

    mean_hsv = [mean_hue, mean_sat, mean_val]

    return mean_hsv

def find_standard_deviation_hsv(hsv_image):
    '''
    computed standard deviation of hsv in image
    :param hsv_image: image in hsv format
    :return: array of hsv standard deviation
    '''

    hue_1D = hsv_image[...,0].flatten()
    sat_1D = hsv_image[...,1].flatten()
    val_1D = hsv_image[...,2].flatten()

    hue_SD = np.std(hue_1D)
    sat_SD = np.std(sat_1D)
    val_SD = np.std(val_1D)

    SD_hsv = [hue_SD, sat_SD, val_SD]

    return SD_hsv

def detect_edges(image, lower_threshold, upper_threshold):
    '''
    Use canny edge detection to detect edges in an image
    :param image: image whose edges are to be detected
    :param lower_threshold: lower threshold for canny edge detector
    :param upper_threshold: upper threshold for canny edge detector
    :return: image with edges detected
    '''

    image = cv2.bilateralFilter(image, 9, 75, 75)
    canny = cv2.Canny(image, lower_threshold, upper_threshold)

    return canny

def find_straight_edge_density(image):
  '''
  Find a measure of how many straight edges are in the scene image
  using fast line detector method. Blur image while keeping edges
  sharp using bilateral filter to reduce noise
  :return: sum of straight lines
  '''

  gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

  gray_image = cv2.bilateralFilter(gray_image, 9, 75, 75)

  fld = cv2.ximgproc.createFastLineDetector()
  lines = fld.detect(gray_image)
  draw_image = fld.drawSegments(image, lines) # can use to display image

  try:
    if len(lines) == 0:
        return 0
  except:
      return 0

  sum_length = 0
  for i in range(len(lines)):
      x1 = lines[i][0][0]
      y1 = lines[i][0][1]
      x2 = lines[i][0][2]
      y2 = lines[i][0][3]

      length_line_segment = math.sqrt(((x2 - x1) ** 2) +  ((y2 - y1) ** 2))

      sum_length += length_line_segment

  return sum_length


def find_edge_density(image):
    '''
    Computes how much of the image consists of edges
    :param image: BGR image whose edge density needs to be find
    :return: percentage of image that is made up of edges
    '''

    edges_image = detect_edges(image, 100, 200)

    total_pixels = edges_image.shape[0] * edges_image.shape[1]
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
    propab = [np.size(image_1D[image_1D == i]) / (1.0 * length) for i in symset]
    entropy = np.sum([p * np.log2(1.0/p) for p in propab])

    return entropy