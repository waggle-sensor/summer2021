'''

Sources: 
OpenCV Python Tutorial For Beginners 16
https://www.youtube.com/watch?v=eX7wXfNLFDw&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=18
More Readings:
https://www.geeksforgeeks.org/how-to-display-an-opencv-image-in-python-with-matplotlib/
'''


import cv2
from matplotlib import pyplot as plt

# plt version
# Note: plt reads in RBG format whereas OpenCV reads in BGR format
# need to convert bgr to rbg

img = cv2.imread('lena.jpg', -1)
cv2.imshow('image', img)
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)


plt.imshow(img)
plt.xticks([]), plt.yticks([]) # hide ticks
plt.show()

# benefits: xy, configurations of plots, png

cv2.waitKey(0)
cv2.destroyAllWindows()


