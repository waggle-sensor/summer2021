'''
1) Perform Kmeans clustering for image segmentation.
2) Change the image to grayscale.
3) Implement blur filter.
4) Implement canny transformation.
5) Implement dilate/open transformation.
6) Find contours.
7) Determine if contours can be found. If yes, continue.
    a) If no, return nothing End.
8) Find contours and create minimum-area rectangle. 
9) Determine if rectangle meets conditions (i.e., it actually detects the pole). 
   If yes, continue.
    a) If no, return nothing End.
10) Fill rectangle. Pole detected and annotated. End.
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

def mid_kmeans(name, img):
    
    imgcopy = img.copy() # clone image    
    blank_image = 255 * np.ones_like(img , dtype = np.uint8)       
    img_km = kmeans(img)
    
    gray_img = cv2.cvtColor(img_km, cv2.COLOR_BGR2GRAY)    
    blur = cv2.blur(gray_img, (1, 1)) # optimized parameters
    edged = auto_canny(blur)
    kernel = np.ones((3,3),np.uint8) # optimized parameters
    edged = cv2.dilate(edged, None, iterations=1) # optimized parameters
    edged = cv2.morphologyEx(edged, cv2.MORPH_CLOSE, kernel)
    contours, _ = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    if len(contours) == 0: # no contours detected
        print("KMEANS: No contours found, nothing returned.")
        return None
    else: # contours detected
        # extract contour with the greatest length
        # we assume this would be the pole
        contour = max(contours, key = len) 
        #contourImg = cv2.drawContours(imgcopy, contour, -1, (0, 255, 0), 3)
        rect = cv2.minAreaRect(contour)
        
        # extract width and height, swap if w > h
        w, h = rect[1][0], rect[1][1]
        if w > h:
            w, h = swap(w, h)        
        area = (w * h) # determine area
        #print(area, w, h)   
                      
        if area > 35000 or w > 70 or h < 180:
            # pole not detected
            print("KMEANS: Box is not ideal size, nothing returned.")
            return False
        else:    
            box = cv2.boxPoints(rect)
            box = np.int0(box)         
            boxed_img = cv2.fillPoly(imgcopy, [box], (0, 255, 0))  #GREEN  
            blank_image = cv2.fillPoly(blank_image, [box], (0, 255, 0))  #GREEN  
            mask = mask_maker(blank_image, 170, 170)
            print("CANNY: Successful middle pole detection.")
            
            path = 'C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/images'
            cv2.imwrite(os.path.join(path , name + '_Mid.jpg'), img)
            
            path = 'C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/contours'
            cv2.imwrite(os.path.join(path , name + '_Mid_Canny.jpg'), boxed_img)
            
            path = 'C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/labels'             
            cv2.imwrite(os.path.join(path, name + '_Mid_Mask.jpg'), mask) 

def right_kmeans(name, img):

    imgcopy = img.copy() # clone image         
    blank_image = 255 * np.ones_like(img , dtype = np.uint8)      
    img_km = kmeans(img)
    
    gray_img = cv2.cvtColor(img_km, cv2.COLOR_BGR2GRAY)    
    blur = cv2.blur(gray_img, (1, 1)) # optimized parameters
    edged = auto_canny(blur)
    edged = cv2.dilate(edged, None, iterations=1) # optimized parameters
    contours, _ = cv2.findContours(edged,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)    
     
    if len(contours) == 0: # no contours detected
        print("KMEANS: No contours found, nothing returned.")
        return None
    else: # contours detected
        # extract contour with the greatest length
        # we assume this would be the pole
        contour = max(contours, key = len) 
        #contourImg = cv2.drawContours(imgcopy, contour, -1, (0, 255, 0), 3)
        rect = cv2.minAreaRect(contour)
        
        # extract width and height, swap if w > h
        w, h = rect[1][0], rect[1][1]
        if w > h:
            w, h = swap(w, h)        
        area = (w * h) # determine area
        #print(area, w, h)   
        
        if area > 35000 or area < 2000 or w > 70 or h < 300:
            # pole not detected
            print("KMEANS: Box is not ideal size, nothing returned.")
            return False
        else:    
            box = cv2.boxPoints(rect)
            box = np.int0(box)
            boxed_img = cv2.fillPoly(imgcopy, [box], (0, 255, 0))  #GREEN  
            blank_image = cv2.fillPoly(blank_image, [box], (0, 255, 0))  #GREEN  
            mask = mask_maker(blank_image, 170, 170)
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
        
def swap(x, y):
    temp = x
    x = y
    y = temp
    return x, y

def create_ROIs(img):
    img_crop_arr = []
    img_crop_arr.append(img[125:125 + 450, 650:650 + 200])
    img_crop_arr.append(img[275:275 + 450, 875:875 + 200])   
    return img_crop_arr

def auto_canny(image, sigma=0.33):
    # Calculate the median of single channel pixel intensity
    v = np.median(image)
    lower = int(max(0, (1.0 - sigma) * v))
    upper = int(min(255, (1.0 + sigma) * v))
    edged = cv2.Canny(image, lower, upper)
    return edged

def kmeans(img): 
    # Reshaping the image into a 2D array of pixels and 3 color values (RGB)
    pixel_vals = img.reshape((-1,3))
    # Convert to float type
    pixel_vals = np.float32(pixel_vals)
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.85)
    k = 5
    retval, labels, centers = cv2.kmeans(pixel_vals, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)
    # convert data into 8-bit values
    centers = np.uint8(centers)
    segmented_data = centers[labels.flatten()]
    # reshape data into the original image dimensions
    segmented_image = segmented_data.reshape((img.shape))
    return segmented_image

def run_mid_kmeans(name, img):
    mid = img[125:125 + 450, 650:650 + 200]
    res = mid_kmeans(name, mid)
    return res

def run_right_kmeans(name, img):
    right = img[275:275 + 450, 875:875 + 200]
    res = right_kmeans(name, right)
    return res      

# def main():
    
#     files = glob.glob ("C:/Users/hp/Desktop/notes_CV/tests/photos/*.JPG")
#     names, img_data = read_images(files)

#     count = 0
#     for i in range(len(img_data)):
#         count += 1
#         print(count, names[i])
#         run_mid_kmeans(names[i], img_data[i])
#         run_right_kmeans(names[i], img_data[i])
        
        
# if __name__=="__main__":
#     main()    