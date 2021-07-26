import random
# from scipy import ndarray
import skimage as sk
from skimage import transform
from skimage import util
from detect_features import display
import cv2
import os
import numpy as np
import pandas as pd
from detect_features import find_mean_hsv
from detect_features import find_standard_deviation_hsv
from detect_features import find_edge_density
from detect_features import find_straight_edge_density
from detect_features import find_entropy
from detect_features import append_df_to_excel
import random
from pathlib import Path

def fill(image, h, w):
    image = cv2.resize(image, (h, w), cv2.INTER_CUBIC)
    return image

def horizontal_shift(image, ratio = 0.0):
    # ratio needs to be less than 1 and greater than 0

    ratio = random.uniform(-ratio, ratio)
    h, w = image.shape[:2]
    to_shift = w * ratio
    if (ratio > 0):
        image = image[:, :int(w - to_shift), :]

    if (ratio < 0):
        image = image[:, int(-1 * to_shift):, :]

    image = fill(image, h, w)
    return image

def vertical_shift(image, ratio = 0.0):
    # ratio needs to be less than 1 and greater than 0

    ratio = random.uniform(-ratio, ratio)
    h, w = image.shape[:2]
    to_shift = h * ratio
    if (ratio > 0):
        image = image[:int(h-to_shift), :,:]

    if (ratio < 0):
        image = image[int(-1 * to_shift):, :, :]

    image = fill(image, h, w)
    return image

def random_rotation(image):
    # pick a random degree of rotation between 25% on the left and 25% on the right
    random_degree = random.uniform(-25, 25)
    return sk.transform.rotate(image, random_degree)

def random_noise(image):
    # add random noise to the image
    return sk.util.random_noise(image)

def brightness(img, value):
    #value = random.uniform(low, high)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = np.array(hsv, dtype = np.float64)
    hsv[:,:,1] = hsv[:,:,1]*value
    hsv[:,:,1][hsv[:,:,1]>255]  = 255
    hsv[:,:,2] = hsv[:,:,2]*value
    hsv[:,:,2][hsv[:,:,2]>255]  = 255
    hsv = np.array(hsv, dtype = np.uint8)
    img = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
    return img

def channel_shift(img, value):
    value = int(random.uniform(-value, value))
    img = img + value
    img[:,:,:][img[:,:,:]>255]  = 255
    img[:,:,:][img[:,:,:]<0]  = 0
    img = img.astype(np.uint8)
    return img

def zoom(img, value):
    value = random.uniform(value, 1)
    h, w = img.shape[:2]
    h_taken = int(value*h)
    w_taken = int(value*w)
    h_start = random.randint(0, h-h_taken)
    w_start = random.randint(0, w-w_taken)
    img = img[h_start:h_start+h_taken, w_start:w_start+w_taken, :]
    img = fill(img, h, w)
    return img

def change_hsv(image):
   hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

   hsv_image[:,:, 0] -= random.randint(1, 5)   # change hue/sat/val by change_value pixels
   hsv_image[:,:, 1] += random.randint(1, 5)
   hsv_image[:,:, 2] -= random.randint(1, 5)


   image = cv2.cvtColor(hsv_image, cv2.COLOR_HSV2BGR)
   return image

def add_augmented_images_to_dataframe():
    df = pd.read_excel(
        r'C:\Users\SamaahMachine\Documents\Argonne\Images with Ratings\augmented_images.xlsx')


    for i in range(len(df)):

        image_name = df.loc[i].at["originalName"]
        folder = "training_images/MIT_images/"
        file_path = folder + image_name

        my_file = Path(file_path)
        if (my_file.is_file()):

            image = cv2.imread(file_path)

            print(i)

            # randomly pick which data augmentations you want to do
            image = change_hsv(image)
            image = brightness(image, 1.2)
            image = horizontal_shift(image, 0.5)

            # horizontal shift,
            # change brightness
            # change

            # once you do those image transformations, you have new image

            # calculate all the features using this new image

            hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

            mean_hsv = find_mean_hsv(hsv_image)
            standard_dev_hsv = find_standard_deviation_hsv(hsv_image)
            edge_density = find_edge_density(image)
            straight_edge_density = find_straight_edge_density(image)
            image = cv2.imread(file_path)
            entropy = find_entropy(image)

            # replace values with the features that I computed
            df.loc[i, 'Mean Hue'] = mean_hsv[0]
            df.loc[i, 'Mean Sat'] = mean_hsv[1]
            df.loc[i, 'Mean Value'] = mean_hsv[2]
            df.loc[i, 'sdHue'] = standard_dev_hsv[0]
            df.loc[i, 'sdSat'] = standard_dev_hsv[1]
            df.loc[i, 'sdValue'] = standard_dev_hsv[2]
            df.loc[i, 'ED'] = edge_density
            df.loc[i, 'SED'] = straight_edge_density
            df.loc[i, 'Entropy'] = entropy

            append_df_to_excel(r'C:\Users\SamaahMachine\Documents\Argonne\Images with Ratings\augmented_images.xlsx', df,
                               startrow=0)



def main():
    # file_path = 'training_images/MIT_images/47644824_3ffc0d6af2_o.jpg'
    # image = cv2.imread(file_path, 1)
    #
    # display(image)
    add_augmented_images_to_dataframe()




    # folder_path = 'training_images/TFK'
    # num_files_desired = 1000
    #
    # # gather list of all the images in folder
    # images = [os.path.join(folder_path, f) for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    #
    # num_generated_files = 0
    # while num_generated_files <= num_files_desired:
    #     # random image from folder
    #     image_path = random.choice(images)
    #
    #     image_to_transform = cv2.imread(file_path, 1)
    #
    #     available_transformations = {
    #         'rotate': random_rotation,
    #         'noise': random_noise,
    #         'horizontal_flip': horizontal_flip
    #     }
    #
    #     # random num of transformations to apply
    #     num_transformations_to_apply = random.randint(1, len(available_transformations))
    #     num_transformations = 0
    #     transformed_image = None
    #     while num_transformations <= num_transformations_to_apply:
    #         # choose a random transformation to apply for a single image
    #         key = random.choice(list(available_transformations))
    #         transformed_image = available_transformations[key](image_to_transform)
    #         num_transformations += 1
    #
    #
    #
    # print(images)

if __name__ == '__main__':
    main()

