import cv2
import numpy as np
from matplotlib import pyplot as plt


     
def main():

    # originally ran object detection but snow and poles are very similar

    # '''
    img = cv2.imread("snow_test.jpg", cv2.IMREAD_GRAYSCALE)
    
    # laplace
    lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3) # cv2.CV_64F float datatype
    lap = np.uint8(np.absolute(lap)) # abs val of laplacian transformation, convert back to 8bit
    
    # sobel; last two arguments: dx, dy
    # detect gradients in hor(x)/vert(y) directions
    sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0) 
    sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
    # abs val of sobel transformation, convert back to 8bit
    sobelX = np.uint8(np.absolute(sobelX))
    sobelY = np.uint8(np.absolute(sobelY))
    
    # combine, not the X_or
    sobelCombined = cv2.bitwise_or(sobelX, sobelY)
    
    # canny
    # img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)    
    canny = cv2.Canny(img, 52, 200) # can add a trackbar    
     
    
    titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'canny']
    images = [img, lap, sobelX, sobelY, sobelCombined, canny]
    for i in range(6):
        plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
        plt.title(titles[i])
        plt.xticks([]),plt.yticks([])
    
    plt.show()    


        
if __name__=="__main__":
   main()    