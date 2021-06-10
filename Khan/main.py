import cv2
import numpy as np

def detect_hsv():
    file_path = 'images/image1.jpg'
    image = cv2.imread(file_path, 1)

    # Default values that can be used for lower and upper limit of hsv
    lower_hue = 90
    upper_hue = 160
    lower_sat = 0
    upper_sat = 255
    lower_val = 0
    upper_val = 255

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_limit = np.array([lower_hue, lower_sat, lower_val])
    upper_limit = np.array([upper_hue, upper_sat, upper_val])

    mask = cv2.inRange(hsv, lower_limit, upper_limit)

    res = cv2.bitwise_and(image, image, mask = mask)

    cv2.imshow("image", image)
    cv2.imshow("mask", mask)
    cv2.imshow("res", res)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

def main():
    detect_hsv()

if __name__ == '__main__':
    main()
