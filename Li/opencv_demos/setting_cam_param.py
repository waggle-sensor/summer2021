'''
Sources: 
OpenCV Python Tutorial For Beginners 6
https://www.youtube.com/watch?v=FVnA3xpqEKY&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=7

More Readings:
https://docs.opencv.org/master/dd/d43/tutorial_py_video_display.html
'''
import cv2


cap = cv2.VideoCapture(0)

# obtain actual dimensions
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # width
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # height

# 3 for width. 4 for height

# set to arbitrarily large number -- > goes to maximum resolution of screen
# i.e. 3000 x 3000 --> 1280 x 720

# set(proid, value) where propId is a number from 0 to 18. Each number denotes 
# a property of the video (if it is applicable to that video)
cap.set(3, 3000)
cap.set(4, 3000)

print(cap.get(3))
print(cap.get(4))


# recording and quitting procedure
while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
       cv2.imshow('frame', gray)

       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()