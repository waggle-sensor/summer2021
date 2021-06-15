'''

Sources: 
OpenCV Python Tutorial For Beginners 25
https://www.youtube.com/watch?v=mVWQNeY1Pb4&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=29

More Readings:

    
'''
import numpy as np
import cv2

img = cv2.imread('shapes.jpg')
imgGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(imgGrey, 240, 255, cv2.THRESH_BINARY) # trackbar
contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

cv2.imshow("img", img)

# iterate through all contours
for contour in contours:
    # approximate polygon through curves (contours)
    # second argument: epsilon -- accuracy
    approx = cv2.approxPolyDP(contour, 0.01* cv2.arcLength(contour, True), True)
    # index 0 : bc we are only working with one contour at a time
    cv2.drawContours(img, [approx], 0, (0, 0, 0), 5) 
    x = approx.ravel()[0]
    # the -5 is to shift the text
    y = approx.ravel()[1] - 5
    
    
    if len(approx) == 3:
        cv2.putText(img, "Triangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 4:
        x1 ,y1, w, h = cv2.boundingRect(approx)
        aspectRatio = float(w)/h
        print(aspectRatio)
        
        # room for noise
        if aspectRatio >= 0.95 and aspectRatio <= 1.05:
          cv2.putText(img, "square", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
        else:
          cv2.putText(img, "rectangle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    
    
    elif len(approx) == 5:
        cv2.putText(img, "Pentagon", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    elif len(approx) == 10:
        cv2.putText(img, "Star", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))
    else:
        cv2.putText(img, "Circle", (x, y), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0))


cv2.imshow("shapes", img)
cv2.waitKey(0)
cv2.destroyAllWindows()