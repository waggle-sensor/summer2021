'''
Sources: 
OpenCV Python Tutorial For Beginners 5
https://www.youtube.com/watch?v=V1aMDD5583k&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=6

More Readings:
https://www.geeksforgeeks.org/python-opencv-cv2-line-method/
'''

import numpy as np
import cv2

#read in image
img = cv2.imread('lena.jpg', 1)

# filling the complete image with zeros results in a black image
# img = np.zeros([512, 512, 3], np.uint8) 


# get dimensions of image
dimensions = img.shape

# height, width, number of channels in image
height = img.shape[0]
width = img.shape[1]
channels = img.shape[2]
 
print('Image Dimension    : ',dimensions) # 512 x 512
print('Image Height       : ',height) # 512
print('Image Width        : ',width) # 512
print('Number of Channels : ',channels) # 3
"------------------------------------------------------------------------------"
"Covered shapes: lines, arrowed lines, circles, rectangle, ellipse"
"Others: font and text"
"------------------------------------------------------------------------------"
# line arguments: image, starting pt, ending pt, color, thickness
# coordinates in the form of tuple
# color: (B, G, R) 255 max (google rgb color picker)
# thickness: 1- 10

# img = cv2.line(img, (0,0), (255,255), (147, 96, 44), 10) # 255, 0, 0 == pure blue
# img = cv2.arrowedLine(img, (0,255), (255,255), (255, 0, 0), 10)

# coordinates upper left, bottom right
img = cv2.rectangle(img, (384, 0), (510, 128), (0, 0, 255), 10)

# img, center, radius, color, thickness
# img = cv2.circle(img, (447, 63), 63, (0, 255, 0), -1)


# font
font = cv2.FONT_HERSHEY_SIMPLEX

# image, text, starting point, font, font size, color of font,thickness, line type
# img = cv2.putText(img, 'OpenCv', (10, 500), font, 4, (0, 255, 255), 10, cv2.LINE_AA)

# img, Point center, Size axes, double angle, double startAngle, 
# double endAngle, const Scalar &color, int thickness=1,
# img = cv2.ellipse(img, (256,256), (100,50), 0, 0, 180, 255, -1)

# pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
# pts = pts.reshape((-1,1,2))
# img = cv2.polylines(img,[pts],True,(0,255,255))
cv2.imshow('image', img)

cv2.waitKey(0)
cv2.destroyAllWindows()