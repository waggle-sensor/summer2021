'''
Sources: 
OpenCV Python Tutorial For Beginners 7
https://www.youtube.com/watch?v=rRSyg9kYfcU&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=8

More Readings:
https://www.geeksforgeeks.org/python-datetime-module-with-examples/
https://www.geeksforgeeks.org/python-opencv-cv2-puttext-method/
'''

import cv2
import datetime


cap = cv2.VideoCapture(0)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # width
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) # height


while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True:

       font = cv2.FONT_HERSHEY_SIMPLEX
       
       # concatanate string: width + height
       # putText(image, text, org, font, fontScale, color, thickness, linetype

       text = 'Width: '+ str(cap.get(3)) + ' Height:' + str(cap.get(4))
       frame = cv2.putText(frame, text, (10, 50), font, 1,
                           (0, 255, 255), 2, cv2.LINE_AA)
       
       #  now() function returns the current local date and time
       datet = str(datetime.datetime.now())
       frame = cv2.putText(frame, datet, (10, 100), font, 1,
                           (0, 255, 255), 2, cv2.LINE_AA)
       
       
       cv2.imshow('frame', frame)

       # stop procedure
       if cv2.waitKey(1) & 0xFF == ord('q'):
         break
    else:
        break

cap.release()
cv2.destroyAllWindows()