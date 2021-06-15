'''

Sources: 
OpenCV Python Tutorial For Beginners 19
https://www.youtube.com/watch?v=aDY4aBLFOIg&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=21
More Readings:

    
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

# image gradient: directional change in the intensity or color in an image
# can be used to find the edges in image

# methods use different math methods for finding derivatives/gradients

img = cv2.imread("sudoku.png", cv2.IMREAD_GRAYSCALE)

# laplace
lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) # cv2.CV_64F float datatype
lap = np.uint8(np.absolute(lap)) # abs val of laplacian transformation, convert back to 8bit

# sobel; last two arguments: dx, dy
# detect gradients in hor(x)/vert(y) directions
sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) 
sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
# abs val of sobel transformation, convert back to 8bit
sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

# combine, not the X_or
sobelCombined = cv2.bitwise_or(sobelX, sobelY)

titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined']
images = [img, lap, sobelX, sobelY, sobelCombined]
for i in range(5):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()