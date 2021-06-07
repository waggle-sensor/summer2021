'''
Source: 
OpenCV Python Tutorial For Beginners 3
https://www.youtube.com/watch?v=TGQcDaZ56ao&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=3

More Readings:
https://www.geeksforgeeks.org/python-opencv-cv2-imread-method/
https://www.geeksforgeeks.org/python-opencv-cv2-imshow-method/
https://www.geeksforgeeks.org/reading-image-opencv-using-python/

'''

import cv2

# reads image: -1: unchanged, 0: grayscale, 1: color
img = cv2.imread('lena.jpg', -1) 
# img = cv2.imread('lena.jpg', 0) 
# img = cv2.imread('lena.jpg', 1) 

# print(img) #prints matrices

# window will open up as string name "image"
cv2.imshow('image', img) 

# To hold the window on screen, we use cv2.waitKey method
# First Parameter is for holding screen for specified milliseconds
# It should be positive integer. If 0 pass an parameter, then it will
# hold the screen until user close it.
k = cv2.waitKey(0) 


if k == 27: # escape key
    cv2.destroyAllWindows()
elif k == ord('s'): # accepts a string argument; s key
    cv2.imwrite('lena_copy.png', img) #  create copy
    cv2.destroyAllWindows()
