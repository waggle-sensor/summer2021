'''
1) Change the image to grayscale.
2) Implement blur filter.
3) Implement canny transformation.
4) Implement dilate transformation.
5) Find contours.
6) Determine if contours can be found. If yes, continue.
    a) If no, return nothing End.
7) Find contours and create minimum-area rectangle. 
8) Determine if rectangle meets conditions (i.e., it actually detects the pole). 
   If yes, continue.
    a) If no, return nothing End.
9) Fill rectangle. Pole detected and annotated. End.
'''

import os   
import cv2
import glob
import numpy as np

# read images from files and extract names from directory
def read_images(files):
    # lists for name and image data
    names, img_data = [], []
    # iterates through all images in folder
    for myFile in files:
        img = cv2.imread(myFile)
        img_data.append(img)
        # take the name of the image from directory
        _ , name = os.path.split(myFile) 
        names.append(name)
    return names, img_data


def mid_canny(name, img):
    
    imgcopy = img.copy() # clone image     
    blank_image = 255 * np.ones_like(img , dtype = np.uint8)      
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    blur = cv2.bilateralFilter(gray_img, 11, 21, 7) # optimized parameters
    edged = auto_canny(blur) 
    edged = cv2.dilate(edged, None, iterations=1) # optimized parameters
    contours, _ = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    if len(contours) == 0: # no contours detected
        print("CANNY: No contours found, nothing returned.")
        return None
    else: # contours detected
        # extract contour with the greatest length
        # we assume this would be the pole
        contour = max(contours, key = len) 
        #contourImg = cv2.drawContours(imgcopy, contour, -1, (0, 0, 255), 3)
        rect = cv2.minAreaRect(contour)
        
        # extract width and height, swap if w > h
        w, h = rect[1][0], rect[1][1]
        if w > h:
            w, h = swap(w, h)        
        area = (w * h) # determine area
        #print(area, w, h)   

        if area > 35000 or w > 70 or h < 180:
            # pole not detected
            print("CANNY: Box is not ideal size, nothing returned.")
            return False
        else:    
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            boxed_img = cv2.fillPoly(imgcopy, [box], (0, 0, 255)) #RED    
            blank_image = cv2.fillPoly(blank_image, [box], (0, 0, 255)) #RED                
            mask = mask_maker(blank_image, 139, 139)
            print("CANNY: Successful middle pole detection.")
            
            path = 'C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/images'
            cv2.imwrite(os.path.join(path , name + '_Mid.jpg'), img)
            
            path = 'C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/contours'
            cv2.imwrite(os.path.join(path , name + '_Mid_Canny.jpg'), boxed_img)
            
            path = 'C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/labels'             
            cv2.imwrite(os.path.join(path, name + '_Mid_Mask.jpg'), mask)          
            return True       
    
def right_canny(name, img):
    
    imgcopy = img.copy() # clone image     
    blank_image = 255 * np.ones_like(img , dtype = np.uint8)      
    
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)    
    blur = cv2.bilateralFilter(gray_img, 11, 21, 7) # optimized parameters
    edged = auto_canny(blur) 
    edged = cv2.dilate(edged, None, iterations=1) # optimized parameters
    contours, _ = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

    if len(contours) == 0: # no contours detected
        print("CANNY: No contours found, nothing returned.")
        return None
    else: # contours detected
        # extract contour with the greatest length
        # we assume this would be the pole
        contour = max(contours, key = len) 
        #contourImg = cv2.drawContours(imgcopy, contour, -1, (0, 0, 255), 3)
        rect = cv2.minAreaRect(contour)
        
        # extract width and height, swap if w > h
        w, h = rect[1][0], rect[1][1]
        if w > h:
            w, h = swap(w, h)        
        area = (w * h) # determine area
        # print(area, w, h)   

        if area > 35000 or area < 2000 or w > 70 or h < 300:
            # pole not detected
            print("CANNY: Box is not ideal size, nothing returned.")
            return False
        else:    
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            boxed_img = cv2.fillPoly(imgcopy, [box], (0, 0, 255)) #RED    
            blank_image = cv2.fillPoly(blank_image, [box], (0, 0, 255)) #RED                
            mask = mask_maker(blank_image, 139, 139)
            print("CANNY: Successful right pole detection.")
            
            path = 'C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/images'
            cv2.imwrite(os.path.join(path , name + '_Right.jpg'), img)
            
            path = 'C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/contours'
            cv2.imwrite(os.path.join(path , name + '_Right_Canny.jpg'), boxed_img)
            
            path = 'C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/labels'             
            cv2.imwrite(os.path.join(path, name + '_Right_Mask.jpg'), mask)
            
            return True       

def mask_maker(boxed_img, l_s, l_v):
    hsv = cv2.cvtColor(boxed_img, cv2.COLOR_BGR2HSV)
    # lower range and upper values of HSV of image 
    l_b = np.array([0, l_s, l_v])
    u_b = np.array([255, 255, 255])
    mask = cv2.inRange(hsv, l_b, u_b)
    return mask

def auto_canny(image, sigma=0.33):
    # Calculate the median of single channel pixel intensity
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged

def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y

def run_mid_canny(name, img):
    mid = img[125:125 + 450, 650:650 + 200]
    res = mid_canny(name, mid)
    return res

def run_right_canny(name, img):
    right = img[275:275 + 450, 875:875 + 200]
    res = right_canny(name, right)
    return res

# def main():
    
#     files = glob.glob ("C:/Users/hp/Desktop/notes_CV/tests/organized/steelblue/*.JPG")
#     names, img_data = read_images(files)

#     count = 0
#     for i in range(len(img_data)):
#         count += 1
#         print(count, names[i])
#         run_mid_canny(names[i], img_data[i])
#         run_right_canny(names[i], img_data[i])
        
        
# if __name__=="__main__":
#     main()    