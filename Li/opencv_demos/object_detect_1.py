'''
STILL IMAGE

Sources: 
OpenCV Python Tutorial For Beginners 13
https://www.youtube.com/watch?v=3D7O_kZi8-o&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=14
More Readings:
https://docs.opencv.org/master/df/d9d/tutorial_py_colorspaces.html
https://www.pyimagesearch.com/2021/01/19/image-masking-with-opencv/


'''

# HSV
# Hue corresponds to color components
# Saturation is amount of color (depth of pigment or dominance of hue)
# Value is brightness of color

import cv2
import numpy as np

# dummy function
def nothing(x):
    pass

# trackbar to adjust lower and upper foundation
cv2.namedWindow("Tracking")

cv2.createTrackbar("LH", "Tracking", 0, 255, nothing) #Lower Hue 0/255
cv2.createTrackbar("LS", "Tracking", 0, 255, nothing) #Lower Sat
cv2.createTrackbar("LV", "Tracking", 0, 255, nothing) #Lower Value
cv2.createTrackbar("UH", "Tracking", 255, 255, nothing) #Upper Hue
cv2.createTrackbar("US", "Tracking", 255, 255, nothing) #Upper Sat
cv2.createTrackbar("UV", "Tracking", 255, 255, nothing) #Upper Value

while True:
    frame = cv2.imread('smarties.png')

    # converts bgr to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 
    l_h = cv2.getTrackbarPos("LH", "Tracking")
    l_s = cv2.getTrackbarPos("LS", "Tracking")
    l_v = cv2.getTrackbarPos("LV", "Tracking")

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking")

    # lower range and upper values of HSV of image 
    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])


    # ex: blue mask + frame = res with only blue

    # mask allows us to focus only on the portions of the image that interests us
    mask = cv2.inRange(hsv, l_b, u_b)

    # frame + mask = result
    res = cv2.bitwise_and(frame, frame, mask = mask)

    cv2.imshow("frame", frame) # original
    cv2.imshow("mask", mask) # mask 
    cv2.imshow("res", res) # res

    key = cv2.waitKey(1)
    if key == 27:
        break

cv2.destroyAllWindows()