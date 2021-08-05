#!/usr/bin/env python
# coding: utf-8

import cv2 # pip3 install opencv-python
import os
from glob import glob
import random
import numpy as np # pip3 install numpy

import random
import skimage as sk # pip3 install scikit-image
from skimage import transform, util


def augment_image(pic_path, dest_pic_path, noise=True):
    """
        Augments an image at location 'pic_path', saving
        the resulting image at 'dest_pic_path'.
        
        Parameters:
            pic_path: the path to the image to be augmented
            dest_pic_path: the path of the image to be created
    """
    
    pic = cv2.cvtColor(cv2.imread(pic_path),cv2.COLOR_BGR2RGB)
    
    # random horizontal/vertical flip:
    if bool(random.getrandbits(1)):
        pic = np.array(np.fliplr(pic))
    if bool(random.getrandbits(1)):
        pic = np.array(np.flipud(pic))
    
    # random rotations:
    random_degree = random.uniform(-45, 45)
    pic = sk.transform.rotate(pic, random_degree)
    
    # add noise:
    if noise and bool(random.getrandbits(1)):
        pic = sk.util.random_noise(pic)
    
    pic = pic.astype(np.float32) * 255.
    cv2.imwrite(dest_pic_path, cv2.cvtColor(pic, cv2.COLOR_RGB2BGR))
    
    # ensure file is written:
    assert os.path.isfile(dest_pic_path)
    

def augment_dataset(pic_dir_path, dest_pic_dir_path, scale=2):
    """
        Augments an entire directory full of images, saving
        the augmented images to another directory.
        
        Parameters:
            pic_dir_path: path to directory with pictures
            dest_pic_dir_path: path to directory where augmented
                               pictures will be saved
            scale: how many augmented images to produce per image
    """
    assert os.path.isdir(pic_dir_path)
    assert os.path.isdir(dest_pic_dir_path)
    
    for extension in ['.png', '.jpg', '.jpeg']:
        pics = glob(os.path.join(pic_dir_path, f'*{extension}'))
        
        for pic in pics:
            pic_name = os.path.splitext(os.path.basename(pic))[0]

            for i in range(scale):
                new_pic_name = f'{pic_name}_aug{i}{extension}' 
                dest_pic_path = os.path.join(dest_pic_dir_path, new_pic_name)

                augment_image(pic, dest_pic_path)

def main():
	augment_dataset(pic_dir_path='./test_images', 
		        dest_pic_dir_path='./augmented_images',
		        scale=2)


if __name__ == '__main__':
	main()



