'''

Sources: 
OpenCV Python Tutorial For Beginners 17
https://www.youtube.com/watch?v=xSzsD4kXhRw&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=19
More Readings:
https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html
'''

# some basic transformation based on image 
# normally performed on binary images
# required: image and kernel (tells you how to change the value of any pixel 
# by combining it with different amounts of neighboring pixels)

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('smarties.png', cv2.IMREAD_GRAYSCALE) # gray scale mode (or 0)
_, mask = cv2.threshold(img, 220, 255, cv2.THRESH_BINARY_INV) # mask


# square or shape that you want to apply to image
# you can increase size, increase size --> affect results: cleans black dots 
# but also increases white spots
# ex: white square
# kernal = np.ones((2,2), np.uint8)

kernal = np.ones((5,5), np.uint8)


# transformations
# default iteration = 1
# increases the white region in the image or size of foreground object increases

dilation = cv2.dilate(mask, kernal, iterations=2) 

# erodes away the boundary
# A pixel in the original image (either 1 or 0) will be considered 1 only if 
# all the pixels under the kernel is 1, otherwise it is eroded (made to zero)
#  thickness or size of the foreground object decreases or simply white region decreases in the image

erosion = cv2.erode(mask, kernal, iterations=1) 


# morph open: erosion followed by dilation
# useful in removing noise
opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernal)

# morph close: dilation followed by erosion
# useful in closing small holes inside the foreground objects
closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernal)

# morph gradient: difference between dilation and erosion
# result will look like the outline of the object
mg = cv2.morphologyEx(mask, cv2.MORPH_GRADIENT, kernal)

# morph tophat: difference between image and opening of image
th = cv2.morphologyEx(mask, cv2.MORPH_TOPHAT, kernal)


# there are many more morephologies
titles = ['image', 'mask', 'dilation', 'erosion', 'opening', 'closing', 'mg', 'th']
images = [img, mask, dilation, erosion, opening, closing, mg, th]

for i in range(8):
    plt.subplot(2, 4, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()