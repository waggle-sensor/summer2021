'''
Sources: 
OpenCV Python Tutorial For Beginners 8,9
https://www.youtube.com/watch?v=rrh-4NtuK-w&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=9
https://www.youtube.com/watch?v=a7_dBO3EAng&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=10

More Readings:
https://www.geeksforgeeks.org/handle-mouse-events-in-python-opencv/
'''
import numpy as np
import cv2


'''

"Example 1: Output Coordinates, Color "

# function which inputs mouse clicks and determines output
def click_event(event, x, y, flags, param):
    # left click
    if event == cv2.EVENT_LBUTTONDOWN:
        # x y coordinates of click
        print(x,', ' , y)
        font = cv2.FONT_HERSHEY_SIMPLEX 
        strXY = str(x) + ', '+ str(y) # concatanate
        
        # add text to image, show coordinates
        cv2.putText(img, strXY, (x, y), font, .5, (255, 255, 0), 2)
        cv2.imshow('image', img)
        
    # right click
    if event == cv2.EVENT_RBUTTONDOWN:
        
        # B G R : blue is first channel (0), etc
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        
        print(blue,', ' , green, ', ', red)        
        
        font = cv2.FONT_HERSHEY_SIMPLEX
        
        
        strBGR = str(blue) + ', '+ str(green) + ', '+ str(red)
        cv2.putText(img, strBGR, (x, y), font, .5, (0, 255, 255), 2)
        cv2.imshow('image', img)

'''

# '''
"Example 2: Output Dots, Connect Them, Create Lines"

# function which inputs mouse clicks and determines output
def click_event(event, x, y, flags, param):
    # left click
    if event == cv2.EVENT_LBUTTONDOWN:

        cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        points.append((x,y))
        if len(points) >= 2: # connect two points
            # uses last point and 2nd to last point of array
            # starting pt: last pt, ending pt: 2nd to last pt
            
            print("starting pt: ", points[-1], " ending pt: ", points[-2])
            cv2.line(img, points[-1], points[-2], (255, 0, 0), 5) 
        cv2.imshow('image', img)

# '''

# '''

"Example 3: Output Image/Window of Color"

# function which inputs mouse clicks and determines output
def click_event(event, x, y, flags, param):
    # left click
    if event == cv2.EVENT_LBUTTONDOWN:

        # B G R : blue is first channel, etc
        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        
        
        mycolorImage = np.zeros((512,512,3), np.uint8) # data type of image
        # this contains the three channels used to create the color image 
        mycolorImage[:] = [blue, green, red]
        
        
        cv2.imshow('color', mycolorImage)

# '''

"-----------------------------------------------------------------------------"

#img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('lena.jpg')
cv2.imshow('image', img)


points = []

# main function for click events --> effect/return
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
