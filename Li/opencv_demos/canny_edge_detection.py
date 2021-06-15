'''

Sources: 
OpenCV Python Tutorial For Beginners 20
https://www.youtube.com/watch?v=CGfXCkHNemo&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=22
More Readings:

    
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# Canny is the named from the founder: John F Canny
# Canny edge detector is an edge detection operator that uses a multi-stage algorithm
# to detect a wide range of edgews in images


# 5 steps
# 1) Noise reduction
# 2) Gradient calculation
# 3) Non-max supression
# 4) Double threshold
# 5) Edge tracking by hystersis -- supress weak edges or edges not connected


# give us less noise than the sobel and laplacian methods

img = cv2.imread("lena.jpg")
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
canny = cv2.Canny(img, 100, 200) # can add a trackbar

titles = ['image', 'canny']
images = [img, canny]
for i in range(2):
    plt.subplot(1, 2, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()