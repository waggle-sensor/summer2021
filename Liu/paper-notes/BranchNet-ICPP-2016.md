### BranchyNet: Fast Inference via Early Exiting from Deep Neural Networks

Author: Surat Teerapittayanon (Harvard University) Bradley McDanel (Harvard University) H.T. Kung (Harvard University)

 - Deep neural networks are state of the art methods for many learning tasks due to their ability to extract increasingly better features at each network layer. 
 - However, the improved performance of additional layers in a deep network comes at the cost of added latency and energy usage in feedforward inference. As networks continue to get deeper and larger, these costs become more prohibitive for real-time and energy-sensitive applications. 
 - To address this issue, we present BranchyNet, a novel deep network architecture that is augmented with additional side branch classifiers. **The architecture allows prediction results for a large portion of test samples to exit the network early via these branches when samples can already be inferred with high confidence.** 
 - **BranchyNet exploits the observation that features learned at an early layer of a network may often be sufficient for the classification of many data points**. For more difficult samples, which are expected less frequently, BranchyNet will use further or all network layers to provide the best likelihood of correct prediction. 
 - We study the BranchyNet architecture using several well-known networks (LeNet, AlexNet, ResNet) and datasets (MNIST, CIFAR10) and show that it can both improve accuracy and significantly reduce the inference time of the network.

At each exit point, BranchyNet uses the **entropy of a classification result** (e.g., by softmax) as a measure of confidence in the prediction.
 - If the entropy of a test sample is below a learned threshold value, meaning that the classifier is confident in the prediction, the sample exits the network with the prediction result at this exit point, and is not processed by the higher network layers. 
 - If the entropy value is above the threshold, then the classifier at this exit point is deemed not confident, and the sample continues to the next exit point in the network. 
 - If the sample reaches the last exit point, which is the last layer of the baseline neural network, it always performs classification.
