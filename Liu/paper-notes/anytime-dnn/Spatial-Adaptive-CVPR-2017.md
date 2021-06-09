### Spatially Adaptive Computation Time for Residual Networks

Authors: Michael Figurnov, Maxwell D. Collins, Yukun Zhu, Li Zhang, Jonathan Huang, Dmitry Vetrov, and Ruslan Salakhutdinov

#### Key idea
 - dynamically adjusts the number of executed layers for the regions of the image
 - end-to-end trainable, deterministic and problem-agnostic

#### Motivations:
 - A major drawback of deep convolutional networks is their huge computational cost
   - using attention to guide the computation
   - unsuitable for multi-output problems (generating box proposals in object detection) and per-pixel prediction problems (image segmentation, image generation)
   - choosing the glimpse positions requires designing a separate prediction network or a heuristic procedure
   - soft spatial attention models require evaluating the model at all spatial positions to choose per-position attention weights