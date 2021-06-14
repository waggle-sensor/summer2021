'''

Sources: 
OpenCV Python Tutorial For Beginners 16
https://www.youtube.com/watch?v=eX7wXfNLFDw&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=18
More Readings:
https://docs.opencv.org/master/d7/d4d/tutorial_py_thresholding.html
'''

import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('gradient.png',0)
_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

# create a list for thresholds
titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV']
# create a list for images results
images = [img, th1 ,th2 ,th3 ,th4, th5]

# multiple images in one window
for i in range(6):
    # 2 rows  x 3 columns
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()
