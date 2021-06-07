'''
Sources: 
OpenCV Python Tutorial For Beginners 6
https://www.youtube.com/watch?v=FVnA3xpqEKY&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=7

More Readings:
https://www.geeksforgeeks.org/python-opencv-cv2-line-method/
'''
import cv2


cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# 3 for width. 4 for height

# set to arbitrarily large number -- > goes to maximum resolution of screen
# i.e. 1280 x 720
cap.set(3, 3000)
cap.set(4, 3000)

print(cap.get(3))
print(cap.get(4))
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