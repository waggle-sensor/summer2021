## U-Net Training

The U-Net CNN is trained using labeled images generated from the automatic labeling algorithm. The inputs are 200 x 450 labeled images and their corresponding 200 x 450 unprocessed images. The outputs are checkpoints, which are the models we will be using for testing. 




### How to Run

Download classicblue/pytorch_cv2.

    docker pull classicblue/pytorch_cv2

Run on Docker.

    docker run -ti --rm -v [UNet Training Directory]:/storage -v [Images Directory]:/data/train/images -v [Labeled Images Directory]:/data/train/labels classicblue/pytorch_cv2

After being redirected.

    cd storage

    pip3 install tensorboard
    
    python3 main.py


