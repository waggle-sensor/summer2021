'''
Sources: 
OpenCV Python Tutorial For Beginners 12
https://www.youtube.com/watch?v=fM6ff3VEviI&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=13
More Readings:
https://blog.electroica.com/trackbar-in-opencv-python/



'''

import numpy as np
import cv2 as cv

def nothing(x):
    print(x)

# trackbar with two switches
cv.namedWindow('image')
cv.createTrackbar('CP', 'image', 10, 400, nothing)
switch = 'color/gray' # boolean: color / gray
cv.createTrackbar(switch, 'image', 0, 1, nothing)

# when switched to 1
while(1):
    img = cv.imread('lena.jpg')
    
    # position of trackbar CP
    pos = cv.getTrackbarPos('CP', 'image')
    font = cv.FONT_HERSHEY_SIMPLEX
    cv.putText(img, str(pos), (50, 150), font, 6, (0, 0, 255), 10)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        break
    s = cv.getTrackbarPos(switch, 'image')
    if s == 0:
       pass
    else:
       img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

    img = cv.imshow('image',img)

cv.destroyAllWindows()