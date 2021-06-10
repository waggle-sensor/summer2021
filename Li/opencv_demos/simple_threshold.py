'''

Sources: 
OpenCV Python Tutorial For Beginners 14
https://www.youtube.com/watch?v=CdltAssTMs8&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=15

More Readings:
https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
'''

import cv2 as cv
import numpy as np

# thresholding: segmentation technique ... seperate image from background

# Divided into two groups: contains pixels less than threshold & contains pixels 
# greater than threshold


# For every pixel, the same threshold value is applied. If the pixel value is 
# smaller than the threshold, it is set to 0, otherwise it is set to a maximum 
# value. The function cv.threshold is used to apply the thresholding. The first 
# argument is the source image, which should be a grayscale image. The second 
# argument is the threshold value which is used to classify the pixel values.
# The third argument is the maximum value which is assigned to pixel values exceeding the threshold. 


# black to white : 0 to 255
img = cv.imread('gradient.png', 0)
# img = cv.imread('sudoku.png',0)

# fourth argument:  many types of thresholds: binary, binary inv, trunc, to zero

_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY) # two colors 0/1
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV) # inverse of above
_, th3 = cv.threshold(img, 20, 255, cv.THRESH_TRUNC) # value wont change after provided threshold
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO) # value before threshold is 0 ie black
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV) # inverse of above


cv.imshow("Image", img)
cv.imshow("th1", th1)
cv.imshow("th2", th2)
cv.imshow("th3", th3)
cv.imshow("th4", th4)
cv.imshow("th5", th5)

cv.waitKey(0)
cv.destroyAllWindows()