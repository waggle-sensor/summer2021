import cv2
import glob
import time
import os

from extract_color import split_image, extract_rgb, classify_color, read_images
from otsu_pole import run_mid_otsu, run_right_otsu
from canny_pole import run_mid_canny, run_right_canny
from kmeans_pole import run_mid_kmeans, run_right_kmeans


# runs functions from other programs
def detect_mid_pole(name, img, cat):
    if cat == None:
        return None
    elif cat == "OTSU":
        print("----------Running Otsu----------")
        res = run_mid_otsu(name, img)
        # print(res)
        if res == False:
            print("----------Running K-Means----------")
            res = run_mid_kmeans(name, img)
            # print(res)              
            return res 
        return res
    else: # CANNY
        print("----------Running Canny----------")
        res = run_mid_canny(name, img)
        # print(res)
        if res == False:
            print("----------Running K-Means----------")
            res = run_mid_kmeans(name, img)
            # print(res)
            return res 
        return res  
    
# runs functions from other programs
def detect_right_pole(name, img, cat):
    if cat == None:
        return None
    elif cat == "OTSU":
        print("----------Running Otsu----------")
        res = run_right_otsu(name, img)
        # print(res)        
        if res == False:
            print("----------Running K-Means----------")
            res = run_right_kmeans(name, img)
            # print(res)            
            return res 
        return res
    else: # CANNY
        print("----------Running Canny----------")
        res = run_right_canny(name, img)
        # print(res)
        if res == False:
            print("----------Running K-Means----------")
            res = run_right_kmeans(name, img)
            # print(res)
            return res 
        return res  
    
def main():
    
    start_time = time.time()   
    
    # create directories where the results will be saved
    os.mkdir("C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/images")    
    os.mkdir("C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/contours")
    os.mkdir("C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/labels")
    
    # extract images from directory
    files = glob.glob ("C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/pole_extraction_algorithm/training_process/*.JPG")
    
    names, img_data = read_images(files)
    
    count = 0
    for i in range(len(img_data)):
        count += 1
        print(count, names[i])
    
        cvt_img = cv2.cvtColor(img_data[i], cv2.COLOR_BGR2RGB) 
        chunks = split_image(cvt_img)
        row = extract_rgb(chunks)
        # print(row)
        
        cat = classify_color(row)
        detect_mid_pole(names[i], img_data[i], cat)
        detect_right_pole(names[i], img_data[i], cat)
        
    end_time = time.time()
    print("Total runtime of the program is: ", end_time - start_time)

if __name__=="__main__":
   main()    