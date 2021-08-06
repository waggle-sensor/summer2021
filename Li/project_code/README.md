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



Here is a flow chart of the proposed algorithm. The third step has not been completed due to time constraints.

![Flow Chart](./fig3.png =500x)


