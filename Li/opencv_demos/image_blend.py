'''

Sources: 
OpenCV Python Tutorial For Beginners 22
https://www.youtube.com/watch?v=HfM9s2ehErE&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=25

More Readings:
https://docs.opencv.org/master/dc/dff/tutorial_py_pyramids.html
    
'''

import cv2
import numpy as np
apple = cv2.imread('apple.jpg')
orange = cv2.imread('orange.jpg')
print(apple.shape) # (512, 512, 3)
print(orange.shape) # (512, 512, 3)

# adding two halves together -- frankenfruit
# hstack: Stack arrays in sequence horizontally (column wise).
apple_orange = np.hstack((apple[:, :256], orange[:, 256:]))


# Five Steps
# 1) load two images of apple and orange
# 2) find gaussian pyramids for apple and orange (ex: 6))
# 3) from gauss pyraids, find laplacian pyramids
# 4) join left half of apple and right half of orange in each levels of laplacian
# pyramid
# 5) reconstruct original image from joint image pyramids


# same as last video notes/code

# generate Gaussian pyramid for apple
apple_copy = apple.copy() # copy
gp_apple = [apple_copy]
for i in range(6):
    apple_copy = cv2.pyrDown(apple_copy)
    gp_apple.append(apple_copy)

# generate Gaussian pyramid for orange
orange_copy = orange.copy() # copy
gp_orange = [orange_copy]
for i in range(6):
    orange_copy = cv2.pyrDown(orange_copy)
    gp_orange.append(orange_copy)

# generate Laplacian Pyramid for apple
apple_copy = gp_apple[5]
lp_apple = [apple_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_apple[i])
    laplacian = cv2.subtract(gp_apple[i-1], gaussian_expanded)
    lp_apple.append(laplacian)

# generate Laplacian Pyramid for orange
orange_copy = gp_orange[5]
lp_orange = [orange_copy]
for i in range(5, 0, -1):
    gaussian_expanded = cv2.pyrUp(gp_orange[i])
    laplacian = cv2.subtract(gp_orange[i-1], gaussian_expanded)
    lp_orange.append(laplacian)



# Now add left and right halves of images in each level
apple_orange_pyramid = []
n = 0

for apple_lap, orange_lap in zip(lp_apple, lp_orange): # zip lp apple, lp orange
    n += 1 # increment n
    cols, rows, ch = apple_lap.shape
    
    # combine two halves
    laplacian = np.hstack((apple_lap[:, 0:int(cols/2)], orange_lap[:, int(cols/2):]))
    apple_orange_pyramid.append(laplacian)
    
    
# now reconstruct
apple_orange_reconstruct = apple_orange_pyramid[0]
for i in range(1, 6):
    apple_orange_reconstruct = cv2.pyrUp(apple_orange_reconstruct)
    apple_orange_reconstruct = cv2.add(apple_orange_pyramid[i], apple_orange_reconstruct)


cv2.imshow("apple", apple)
cv2.imshow("orange", orange)
cv2.imshow("apple_orange", apple_orange)
cv2.imshow("apple_orange_reconstruct", apple_orange_reconstruct)
cv2.waitKey(0)
cv2.destroyAllWindows()