'''
Sources: 
OpenCV Python Tutorial For Beginners 10
https://www.youtube.com/watch?v=wSjB_iaQ1wE&list=PLS1QulWo1RIa7D1O6skqDQ-JZ1GGHKK-K&index=11


'''
import numpy as np
import cv2


# read images
messi = cv2.imread('messi5.jpg')

# image properties
# print(messi.shape) # (342, 548, 3)
# print(messi.size) # 562248
# print(messi.dtype) # uint8

# split in bgr order: different channels
b, g, r = cv2.split(messi)

# cv2.imshow("Red", r) # shows only red
# cv2.imshow("Green", b)
# cv2.imshow("Blue", g)

#  combine all the different channels --> basically get the og colored image
messi = cv2.merge((b,g,r))


# this is like photoshop
# location of the ball
ball = messi[280:340, 330:390]
# where to place new ball
messi[273:333, 100:160] = ball



logo = cv2.imread('opencv-logo.png')


# print(logo.shape) # (794, 600, 3)
# print(logo.size) # 1429200
# print(logo.dtype) # uint8


# cv2.imshow('image', messi)
# cv2.imshow('image2', logo)

# resize: can only combine two photos if the size of images are the same 
# image, new size
messi = cv2.resize(messi, (512,512))
logo = cv2.resize(logo, (512,512))

# combine the two photos together
# dst = cv2.add(messi, logo)

# weighted add: give a percentage value for each image
# dst(I)=saturate(src1(I)∗alpha+src2(I)∗beta+gamma)
dst = cv2.addWeighted(messi, 0.9 , logo, 0.1, 0)

cv2.imshow('combination', dst)



cv2.waitKey(0)
cv2.destroyAllWindows()
