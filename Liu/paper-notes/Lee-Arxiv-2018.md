### Anytime Neural Prediction via Slicing Networks Vertically
Author: Hankook Lee, Jinwoo Shin

 - While most existing approaches have focused on training multiple shallow sub-networks jointly, we study training thin sub-networks instead. 
 - To this end, we first build many inclusive thin sub-networks (of the same depth) under a minor modification of existing multi-branch DNNs, and found that they can significantly outperform the state-of-art dense architecture for anytime prediction.
 - This is remarkable due to their simplicity and effectiveness, but training many thin sub-networks jointly faces a new challenge on training complexity.
 - propose a novel DNN architecture by forcing a certain sparsity pattern on multi-branch network parameters, making them train efficiently for the purpose of anytime prediction.