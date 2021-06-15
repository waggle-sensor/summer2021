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
    frame = cv2.imread('snow_test.jpg')

    # converts bgr to hsv
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 
    l_h = cv2.getTrackbarPos("LH", "Tracking") # 59
    l_s = cv2.getTrackbarPos("LS", "Tracking") # 57
    l_v = cv2.getTrackbarPos("LV", "Tracking") # 0 

    u_h = cv2.getTrackbarPos("UH", "Tracking")
    u_s = cv2.getTrackbarPos("US", "Tracking")
    u_v = cv2.getTrackbarPos("UV", "Tracking") #75

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

    k = cv2.waitKey(1) 
    
    
    if k == 27: # escape key
        break
    elif k == ord('s'): # accepts a string argument; s key
        cv2.imwrite('test.jpg', res) #  create copy
        cv2.destroyAllWindows()
cv2.destroyAllWindows()


