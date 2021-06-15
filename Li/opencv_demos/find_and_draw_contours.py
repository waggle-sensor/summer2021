'''

Sources: 
OpenCV Python Tutorial For Beginners 23
https://www.youtube.com/watch?v=FbR9Xr0TVdY&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=27

More Readings:
https://docs.opencv.org/3.4/d4/d73/tutorial_py_contours_begin.html
    
'''

import numpy as np
import cv2

# Contours can be explained simply as a curve joining all the continuous points 
# (along the boundary), having same color or intensity. The contours are a useful 
# tool for shape analysis and object detection and recognition

# In OpenCV, finding contours is like finding white object from black background. 
# So remember, object to be found should be white and background should be black

img = cv2.imread('triangle.jpg')
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

# three arguments in cv.findContours() function, first one is source image, 
#  second is contour retrieval mode, third is contour approximation method

# contours is list of all contours in image
# each individual contour is a numpy array of xy coordinates of boundary pt 
# of the object
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
print("Number of contours = " + str(len(contours)))
print(contours[0])

# cv.drawContours
# first argument is source image, second argument is the contours which should 
# be passed as a Python list, third argument is index of contour
# To draw all contours, pass -1) and remaining arguments are color, thickness etc.
# -1 up to 8

cv2.drawContours(img, contours, -1, (255, 225, 0), 3)
cv2.drawContours(imgray, contours, -1, (0, 255, 0), 3)

cv2.imshow('Image', img)
# cv2.imshow('Image GRAY', imgray)
cv2.waitKey(0)
cv2.destroyAllWindows()