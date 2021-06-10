'''

Sources: 
OpenCV Python Tutorial For Beginners 15
https://www.youtube.com/watch?v=Zf1F4cz8GHU&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=17
More Readings:
https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
'''
# previous section, we used one global value as a threshold
# cases where lighting is different per region --> i.e. different thresholds 
# in different regions


import cv2 as cv
import numpy as np


# run sudoku with global/static threshold and compare results 
img = cv.imread('sudoku.png',0)

# two types of adaptive methods: ADAPTIVE_THRESH_MEAN_C, ADAPTIVE_THRESH_GAUSSIAN_C
# algorithms determines the threshold for a pixel based on a small region around it.

_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY) # two colors 0/1 (static)

# mean of neighborhood area: mean of blocksize x blocksize - C
# block size: size of neighborhood area = 11
# value of c = 2, constant
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 2);

# weighted sum of blocksize x blocksize - C
# block size: size of neighborhood area = 11
# value of c = 2, constant
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2);



cv.imshow("Image", img)
cv.imshow("THRESH_BINARY", th1)
cv.imshow("ADAPTIVE_THRESH_MEAN_C", th2)
cv.imshow("ADAPTIVE_THRESH_GAUSSIAN_C", th3)

cv.waitKey(0)
cv.destroyAllWindows()