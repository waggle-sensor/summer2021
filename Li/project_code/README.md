## Python Programs

This section is dedicated to programs I worked on during the summer. A brief description of each folder is shown below. 

* [pole_extraction_algorithm](./pole_extraction_algorithm): Distinguishes the foreground object (the snow rod) from the background using tools from OpenCV.
* [unet_testing](./unet_testing): Generates rod segmentations from U-Net model.
* [unet_training](./unet_training): Trains U-Net model with labeled images.
* [validation](./validation): Calculates mean Interception over Union (mIoU) score. 

Required modules:
    cv2
    glob
    time
    os
    sklearn
    collections
    webcolors
    torch
    tqdm
    argparse
    sys
    numpy
    torchvision
    PIL
    logging



Below is a flow chart of the proposed algorithm. The first step is automatically generating labels for images. The second step is using labeled images to traing the U-Net model. The third step is calculating snow depth. As of August 6, 2021, steps one and two have been completed. One method for calculating snow depth has been assessed by Kopp et al. in their [paper](https://doi.org/10.1016/j.scitotenv.2019.134213).

![Flow Chart](./fig01.png )

