'''

Sources: 
OpenCV Python Tutorial For Beginners 26
https://www.youtube.com/watch?v=F9TZb0XBow0&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=30    
More Readings:

    
'''

import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread("lena.jpg")

# all black pixel
# all pixels will be zero
# 200 x 200 = 40000 so the histogram will have one peak at 0, intensity = 40000
#img = np.zeros((200,200), np.uint8) 

# input half white pixels
# see two peaks
#cv.rectangle(img, (0, 100), (200, 200), (255), -1)

# add gray color
#cv.rectangle(img, (0, 50), (100, 100), (127), -1)


# plain histogram
# plt.hist(img.ravel(), 256, [0, 256])

# adds colors through splitting into three channels
b, g, r = cv.split(img)
cv.imshow("img", img)
cv.imshow("b", b)
cv.imshow("g", g)
cv.imshow("r", r)

plt.hist(b.ravel(), 256, [0, 256])
plt.hist(g.ravel(), 256, [0, 256])
plt.hist(r.ravel(), 256, [0, 256])

hist = cv.calcHist([img], [0], None, [256], [0, 256])
plt.plot(hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()