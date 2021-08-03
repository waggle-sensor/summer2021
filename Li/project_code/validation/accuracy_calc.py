import numpy as np
import cv2
import torch
import glob

def iou(imageA, imageB):
    intersection = np.logical_and(imageA, imageB)
    union = np.logical_or(imageA, imageB)
    iou_score = np.sum(intersection) / np.sum(union)
    return iou_score


def read_images(files):

    img_data = []
    # iterates through all images in folder
    for myFile in files:
        img = cv2.imread(myFile)
        img_data.append(img)

    return img_data

    
def main():

    gt = glob.glob ("C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/unet/unet_testing/acc_ground_truth/*.JPG")    
    pred = glob.glob ("C:/Users/jeffr/Desktop/SULI_2021/notes_CV/tests/unet/unet_testing/acc_predicted/*.JPG")       
    
    gt_list = read_images(gt)
    pred_list = read_images(pred)

    count = 0
    total = 0
    for i in range(len(gt_list)):
        count += 1
        res = iou(gt_list[i], pred_list[i])
        total = total + res
    print(total)
    print(total/count)


if __name__=="__main__":
   main()    