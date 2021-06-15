'''

Sources: 
OpenCV Python Tutorial For Beginners 24
https://www.youtube.com/watch?v=MkcUgPhOlP8&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=28

More Readings:

    
'''
import cv2
import numpy as np

cap = cv2.VideoCapture('vtest.avi')
frame_width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH)) # 768
print(frame_width)

frame_height =int( cap.get( cv2.CAP_PROP_FRAME_HEIGHT)) # 576
print(frame_height)

fourcc = cv2.VideoWriter_fourcc('X','V','I','D')

out = cv2.VideoWriter("output.avi", fourcc, 5.0, (1280,720))
# '''


ret, frame1 = cap.read() # frame 1 
ret, frame2 = cap.read() # frame 2
print(frame1.shape) # (576, 768, 3)


while cap.isOpened():
    # finds abs difference between 2 frames
    diff = cv2.absdiff(frame1, frame2)
    # convert to gray scale --> easier to find contours
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    # gaussian blur: remove noise 
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY) # two colors 0/1
    
    # increases the white region in the image or size of foreground object increases
    dilated = cv2.dilate(thresh, None, iterations=3) 
    
    # find contours 
    contours, _ = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # remove noise (from rope), make rectangles
    for contour in contours:
        (x, y, w, h) = cv2.boundingRect(contour) 

        if cv2.contourArea(contour) < 900: # small area not accepted
            continue
        
        # draw rectangle (green)
        cv2.rectangle(frame1, (x, y), (x+w, y+h), (0, 255, 0), 2)
        # text indicating movement observed
        cv2.putText(frame1, "Status: {}".format('Movement'), (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 0, 255), 3)
    # cv2.drawContours(frame1, contours, -1, (0, 255, 0), 2)

    image = cv2.resize(frame1, (1280,720))
    out.write(image)
    cv2.imshow("feed", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break


cv2.destroyAllWindows()
cap.release()
out.release()
# '''