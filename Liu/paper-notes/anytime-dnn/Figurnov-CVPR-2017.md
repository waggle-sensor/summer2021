## Spatially Adaptive Computation Time for Residual Networks

Authors: Michael Figurnov, Maxwell D. Collins, Yukun Zhu, Li Zhang, Jonathan Huang, Dmitry Vetrov, Ruslan Salakhutdinov

This paper proposes **a deep learning architecture based on Residual Network that dynamically adjusts the number of executed layers for the regions of the image**.

### Spatially Adaptive Computation Time (SACT)
 - SACT is an end-to-end trainable architecture that incorporates attention into Residual Networks. It learns a deterministic policy that stops computation in a spatial position as soon as the features become “good enough”.
 - maintains the alignment between the image and the feature maps, it is well-suited for a wide range of computer vision problems, including multi-output and per-pixel prediction problems

### Residual Network
 - ResNet-101 ImageNet classification architecture
   - extended for object detection, image segmentation
 - The first two layers of ResNet-101 are a convolution and a max-pooling layer which together have a total stride of four.
 - Then, a sequence of four blocks is stacked together, each block consisting of multiple stacked residual units. ResNet-101 contains four blocks with 3, 4, 23 and 3 units, respectively.
 - A residual unit has a form F (x) = x + f (x), where the first term is called a shortcut connection and the second term is a residual function.