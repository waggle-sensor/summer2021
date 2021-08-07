## Image Segmentation Accuracy using mIoU

The image segmentation accuracy was calculated through mean Interception over Union score. It is the area of the overlap between the two binary images over the area of union. Images labeled by the algorithm were used as the ground truth. Images predicted by the U-Net model were used as testing. The image datasets can be found [here](https://drive.google.com/drive/folders/1l8YpzCzYUpjlQGFN_8riOImDrLZHAbg5?usp=sharing). More information regarding mIoU can be found [here](https://www.pyimagesearch.com/2016/11/07/intersection-over-union-iou-for-object-detection/).

### How to Run

    run main.py
