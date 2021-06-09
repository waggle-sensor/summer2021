'''
Sources: 
OpenCV Python Tutorial For Beginners 12
https://www.youtube.com/watch?v=fM6ff3VEviI&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=13
More Readings:
https://blog.electroica.com/trackbar-in-opencv-python/
https://www.geeksforgeeks.org/python-opencv-bgr-color-palette-with-trackbars/
'''

# GUI element that let the user to select a specific value within a range of values by 
# sliding a slider linearly trackbars will either call a function or update variable
# value based on slider position

# Create a black window with three color channels with resolution 512 x 512. 
# Then create three ‘B’ ‘G’ ‘R’ trackbars using predefined functions of OpenCV library

import numpy as np
import cv2 as cv

# trackbar callback function does nothing but required for trackbar
def nothing(x):
    print(x)



# Create a black image, a window
img = np.zeros((300,512,3), np.uint8)
cv.namedWindow('image')

# able to control color through sliding
# parameters: trackbarname, winname, value, count, callback

# represents one for each channel in BGR order
cv.createTrackbar('B', 'image', 0, 255, nothing) 
cv.createTrackbar('G', 'image', 0, 255, nothing)
cv.createTrackbar('R', 'image', 0, 255, nothing)

switch = '0 : OFF\n 1 : ON' # boolean: on/off
cv.createTrackbar(switch, 'image', 0, 1, nothing)

# when switched to 1
while(1):
    # image show and quit procedure
    cv.imshow('image',img)
    k = cv.waitKey(1) & 0xFF
    if k == 27: #esc
        break

    # values of blue, green, red
    b = cv.getTrackbarPos('B', 'image')
    g = cv.getTrackbarPos('G', 'image')
    r = cv.getTrackbarPos('R', 'image')
    
    
    s = cv.getTrackbarPos(switch, 'image')

    if s == 0:
       img[:] = 0
    else:
       img[:] = [b, g, r]


cv.destroyAllWindows()