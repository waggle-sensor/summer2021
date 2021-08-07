import skimage as sk
from skimage import util
import cv2
import numpy as np
import random

def fill(image, h, w):
    '''
    fills image with data augmentation
    :param image: image to fill
    :param h: height
    :param w: width
    :return: augmented image
    '''
    image = cv2.resize(image, (h, w), cv2.INTER_CUBIC)
    return image

def horizontal_shift(image, ratio = 0.0):
    '''
    shifts image horizontally by ratio given
    :param image: image to shift
    :param ratio: what ratio to shift image by
                  ratio needs to be less than 1 and
                  greater than 0
    :return: augmented image
    '''

    ratio = random.uniform(-ratio, ratio)
    h, w = image.shape[:2]
    to_shift = w * ratio
    if (ratio > 0):
        image = image[:, :int(w - to_shift), :]

    if (ratio < 0):
        image = image[:, int(-1 * to_shift):, :]

    image = fill(image, h, w)
    return image

def vertical_shift(image, ratio = 0.0):
    '''
    shifts image vertically by ratio given
    :param image: image to shift
    :param ratio: what ratio to shift image by
                  ratio needs to be less than 1 and
                  greater than 0
    :return: augmented image
    '''
    # ratio needs to be less than 1 and greater than 0

    ratio = random.uniform(-ratio, ratio)
    h, w = image.shape[:2]
    to_shift = h * ratio
    if (ratio > 0):
        image = image[:int(h-to_shift), :,:]

    if (ratio < 0):
        image = image[int(-1 * to_shift):, :, :]

    image = fill(image, h, w)
    return image

def random_noise(image):
    '''
    Adds random noise to the image
    :param image: image to add noise to
    :return: augmented image
    '''

    return sk.util.random_noise(image)

def brightness(img, value):
    '''
    increases / decreases brightness by value given
    :param img: image to change brightness to
    :param value: value to change brightness by
    :return: augmented image
    '''

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype = np.float64)
    hsv[:,:,1] = hsv[:,:,1]*value
    hsv[:,:,1][hsv[:,:,1]>255]  = 255
    hsv[:,:,2] = hsv[:,:,2]*value
    hsv[:,:,2][hsv[:,:,2]>255]  = 255
    hsv = np.array(hsv, dtype = np.uint8)
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

    return img

def zoom(img, value):
    '''
    zooms into image by value given
    :param img: image to zoom into
    :param value: value
    :return:
    '''
    value = random.uniform(value, 1)
    h, w = img.shape[:2]
    h_taken = int(value*h)
    w_taken = int(value*w)
    h_start = random.randint(0, h-h_taken)
    w_start = random.randint(0, w-w_taken)
    img = img[h_start:h_start+h_taken, w_start:w_start+w_taken, :]
    img = fill(img, h, w)
    return img

def change_hsv(image):
   '''
    changes values of hue, saturation, and value of image by a
    random amount between 0 and 5
   :param image: image to change hsv values of
   :return: augmented image
   '''
   hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

   hsv_image[:,:, 0] -= random.randint(0, 5)   # change hue/sat/val by change_value pixels
   hsv_image[:,:, 1] += random.randint(0, 5)
   hsv_image[:,:, 2] -= random.randint(0, 5)

   image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
   return image

