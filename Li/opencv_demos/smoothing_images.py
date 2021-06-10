'''

Sources: 
OpenCV Python Tutorial For Beginners 18
https://www.youtube.com/watch?v=u3poUhCxx4k&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=20
More Readings:
https://docs.opencv.org/master/d4/d13/tutorial_py_filtering.html
'''

import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('lena.jpg')
# more images on site
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Smoothing/Blurring images: most commonly used oprations
# remove noise from images

# Low Pass Filter (LPF) : removes noise, blurring image
# High Pass Filter (HPF) : finds edges in images



# homogeneous: most simple, each output pixel is the mean of its kernel neighbors
# Kernel = 1 / (Kwidth* kHeight) [ kernel matrix]

kernel = np.ones((5, 5), np.float32)/25


# OpenCV provides a function cv.filter2D() to convolve a kernel with an image
# operation works like this: keep this kernel above a pixel, add all the 25 
# pixels below this kernel, take the average, and replace the central pixel 
# with the new average value
dst = cv2.filter2D(img, -1, kernel) # 2D filter

# achieved by convolving the image with a low-pass filter kernel
# removes high frequency content (eg: noise, edges) from the image

# takes the average of all the pixels under the kernel area and replaces the central element'

blur = cv2.blur(img, (5, 5)) # blur filter

# gaussian filter, different weight kernels in both x, y directions
# specifically designed to remove high frequency noise

gblur = cv2.GaussianBlur(img, (5, 5), 0) 

# median blur method: good for salt pepper noise
# kernel size must be odd 
median = cv2.medianBlur(img, 5)


# noise removal but edges are preserved
# operation is slower compared to other filter
# Bilateral filtering also takes a Gaussian filter in space, but one more 
# Gaussian filter which is a function of pixel difference

# The Gaussian function of space makes sure that only nearby pixels are considered 
# for blurring, while the Gaussian function of intensity difference makes sure
# that only those pixels with similar intensities to the central pixel are
#  considered for blurring. 

bilateralFilter = cv2.bilateralFilter(img, 9, 75, 75)

titles = ['image', '2D Convolution', 'blur', 'GaussianBlur', 'median', 'bilateralFilter']
images = [img, dst, blur, gblur, median, bilateralFilter]

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()