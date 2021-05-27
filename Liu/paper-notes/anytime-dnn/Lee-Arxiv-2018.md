### Anytime Neural Prediction via Slicing Networks Vertically
Author: Hankook Lee, Jinwoo Shin

 - While most existing approaches have focused on training multiple shallow sub-networks jointly, we study training thin sub-networks instead. 
 - To this end, we first build many inclusive thin sub-networks (of the same depth) under a minor modification of existing multi-branch DNNs, and found that they can significantly outperform the state-of-art dense architecture for anytime prediction.
 - This is remarkable due to their simplicity and effectiveness, but training many thin sub-networks jointly faces a new challenge on training complexity.
 - propose a novel DNN architecture by forcing a certain sparsity pattern on multi-branch network parameters, making them train efficiently for the purpose of anytime prediction.

#### Motivations:
 - the heavy models are often not suitable for real-world applications due to their resource budgets, e.g., limited memory in mobile devices, low latency for autonomous driving and real-time constraints for Internet video delivery.
 - targeting a single resource budget constraint: network pruning, transfer learning
 - if an application should work under various resource budgets adaptively or the computing power of clients’ device is heterogeneous, then all models of various sizes should be ready separately. It is too inefficient to train and store.

#### Anytime/Adaptive Prediction
 - **use intermediate features of DNN**:
   - Branchynet: Fast inference via early exiting from deep neural networks, ICPR 2016.
   - Deciding How to Decide: Dynamic Routing in Artificial Neural Networks, ICML 2017.
   - Adaptive Neural Networks for Efficient Inference, ICML 2017.
   - Spatially Adaptive Computation Time for Residual Networks, CVPR 2017.
   - NestedNet: Learning Nested Sparse Structures in Deep Neural Networks, CVPR 2018.
   - Multi-scale dense convolutional networks for efficient prediction, ICLR 2018.
   - <span style="color:red">However, joint-training all such sub-networks together is not easy since shallower ones cannot capture level features, and deeper ones might be badly trained if one forces intermediate layers to produce the final outputs.</span>.
 - **multi-scale inputs/features**:
   - Deciding How to Decide: Dynamic Routing in Artificial Neural Networks, ICML 2017.
   - Multi-scale dense convolutional networks for efficient prediction, ICLR 2018.
 - **dense connections**:
   - Multi-scale dense convolutional networks for efficient prediction, ICLR 2018. 