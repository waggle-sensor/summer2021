'''
Sources: 
OpenCV Python Tutorial For Beginners 4
https://www.youtube.com/watch?v=-RtVZsCvXAQ&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=6

More Readings:
https://www.geeksforgeeks.org/saving-operated-video-from-a-webcam-using-opencv/
https://docs.opencv.org/3.4/dd/d9e/classcv_1_1VideoWriter.html

'''

import cv2

cap = cv2.VideoCapture(0); # 0 is the source of camera

# FourCC is a 4-byte code used to specify the video codec. 
# The codecs for Windows is DIVX and for OSX is avc1, h263. FourCC code is 
# passed as cv2.VideoWriter_fourcc(*’MJPG’) for MJPG 
# and cv2.VideoWriter_fourcc(*’XVID’) for DIVX.

fourcc = cv2.VideoWriter_fourcc(*'XVID')

'''
# camera  capture 

# loop runs if capturing has been initialized
while(True):
    
    # reads frames from a camera 
    # ret checks return at each frame
    ret, frame = cap.read()

    print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # prints width 640
    print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # prints height 480

    # original input -- unaltered
    # cv2.imshow('frame', frame)
    
    # Converts to HSV color space, OCV reads colors as BGR
    # frame is converted to hsv (hue, saturation, value)
    # hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # cv2.imshow('frame', hsv)    
    
    # Converts to grayscale space, OCV reads colors as BGR
    # frame is converted to gray
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', gray)
    
    # q to quit
    if cv2.waitKey(1) & 0xFF == ord('q'): # & 0xFF for 64 bit machine
        break
    
cap.release()
cv2.destroyAllWindows()

'''

# if you want to configure dimensions ahead of time
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (100,100)) # dimension

print(cap.isOpened())  # boolean
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # prints width
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # prints height

        out.write(frame)

        # gray scale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        cv2.imshow('frame', gray)

        if cv2.waitKey(1) & 0xFF == ord('q'):
          break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()

