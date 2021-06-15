'''

Sources: 
OpenCV Python Tutorial For Beginners 27
https://www.youtube.com/watch?v=sghglbXyjHc&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=31


More Readings:

    
'''

# template matching: finding template image in large image

import cv2
import numpy as np


img = cv2.imread("messi5.jpg")
grey_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #  convert to grayscale first
template = cv2.imread("messi_face.jpg", 0) # load as gray 

# shape of your template: -1 --> columns and row in reverse order
w, h = template.shape[::-1]


# several matching formulas: we use tm ccorr normed, try others
res = cv2.matchTemplate(grey_img, template, cv2.TM_CCORR_NORMED ) 
print(res)

# brightest point -- filter out points that do not follow threshold
threshold = 0.99; # try adjusting the threshold and see what happens
loc = np.where(res >= threshold) 
print(loc)

# for multiple points
for pt in zip(*loc[::-1]):
    # draw on original image
    cv2.rectangle(img, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()