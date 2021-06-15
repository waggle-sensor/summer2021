'''

Sources: 
OpenCV Python Tutorial For Beginners 21
https://www.youtube.com/watch?v=8yvln2atFkA&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=23

More Readings:
https://docs.opencv.org/3.4/d4/d1f/tutorial_pyramids.html
https://theailearner.com/tag/cv2-pyrdown/
    
'''

# Usually we need to convert an image to a size different than its original. 
# For this, there are two possible options:
# 1) Upsize the image (zoom in) or
# 2) Downsize it (zoom out).

# pyramid representation is a type of multi scale signal representation in which
# a signal or an image is subject to repeated smoothing and subsampling
# useful: blend images

import cv2
import numpy as np


img = cv2.imread("lena.jpg")
layer = img.copy()

# two types: gaussian and laplace
# Gaussian pyramid: Used to downsample images
# Laplacian pyramid: Used to reconstruct an upsampled image from an image lower 
# in the pyramid (with less resolution)

# We can find Gaussian pyramids using cv.pyrDown() and cv.pyrUp() functions
# pyrDown: downsize
# pyrUp: upsize
# try running pyrdown and pyrup on their own
# try running pyrdown, followed by pyrup

# pd = cv2.pyrDown(img)
# cv2.imshow("pyrdown", pd)

# pu = cv2.pyrUp(img)
# cv2.imshow("pyrup", pu)

# pdpu = cv2.pyrUp(pd)
# cv2.imshow("pyrdown, then pyrup", pdpu)

# pupd = cv2.pyrDown(pu)
# cv2.imshow("pyrup, then pyrdown", pupd)

# When we reduce the size of an image, we are actually losing information of the image


# gaussian pyramid
gaussian_pyramid_list = [layer]


for i in range(6):
    layer = cv2.pyrDown(layer)
    gaussian_pyramid_list.append(layer)
    # cv2.imshow(str(i), layer)

layer = gaussian_pyramid_list[5]

# You can easily notice that the resulting image will be exactly one-quarter the area of its predecessor

cv2.imshow('upper level Gaussian Pyramid', layer)



# there is no function for laplacian pyramid
# Laplacian of a level is obtained by subtracting that level in Gaussian Pyramid 
# and expanded version of its upper level in Gaussian Pyramid

# Since Laplacian is a high pass filter, so at each level of this pyramid, we 
# will get an edge image as an output
# https://i0.wp.com/theailearner.com/wp-content/uploads/2019/08/laplacian_pyr.png?w=532&ssl=1


laplacian_pyramid_list = [layer]

for i in range(5, 0, -1): # 5 to 0, decrements of -1 
    gaussian_extended = cv2.pyrUp(gaussian_pyramid_list[i])
    laplacian = cv2.subtract(gaussian_pyramid_list[i-1], gaussian_extended)
    cv2.imshow(str(i), laplacian)



cv2.imshow("Original image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

