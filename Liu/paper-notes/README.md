## Notes from Nicola:

1. Can improve inference time by statically reducing neural network model size (network compression) or using smaller capsule networks.  But this is a static solution. (have papers but didn’t include b/c not relevant)
 
2. There are adaptive inference methods that skip execution of parts of a network, based on an estimate of relevance computed for each input (e.g. McGill & Perona 2017) – these seem to be very specific to the application.
 
3. Anytime predictors is an idea from 1990s (Zilberstein, 1996). Prediction available at “any” compute time but with variable accuracy/confidence for the resulting prediction. 
    - Can use ensemble methods (Dietterich 2000) or cascade (as in Zilberstein).
    - NN using anytime predictors:
      - FractalNet, BranchyNet, …
      - Hu et al 2019, Huang et al 2017, Teerapittayanon et al 2016, McGill 2017, Wan et al

## Updates from 05/11/21 to 05/21/21
 - Read papers on anytime DNN ([Zilberstein-AAAI-1996](Zilberstein-AAAI-1996.md), [Dietterich-MCS-2000](Dietterich-MCS-2000.md), [BranchNet-ICPP-2016](BranchNet-ICPP-2016.md), [DistributedDNN-ICDCS-2017](DistributedDNN-ICDCS-2017.md), and [Lee-Arxiv-2018](Lee-Arxiv-2018.md))
 - Train the Anytime DNN model for IResNext and BranchNet based on their codes
 - Pick up neural network and deep learning knowledges by reviewing the [book](http://neuralnetworksanddeeplearning.com/) chapter1 to chapter3
   - stochastic gredient decent, backpropogation's prove
   - slow learning issue for quadratic loss function: cross-entropy, softmax with log-likelihood's prove
   - regularization to reduce overfitting: L1, L2 regularizations
   - dropout
   - weights and bias initilization
   - Hessian technique, Momentum-based gredient decent
   - other neurons: sigmoid, tanh, ReLU

## Questions to discuss (05/21/21)
 - Motivation of Anytime DNN: Compared with research activities in building more powerful hardware/accelerators and architectures to speed up the DNN’s inference time, anytime DNN seems to be less competitive. The usage of it seems to be limited to **resource-constraint scenarios** and there is **no penalty for performance degradation**.
   - Any specific application requirements from SAGE
 - Contradictions in building anytime DNN: According to Zilberstein’s paper (AAAI-1996), I think one of the core part of anytime algorithm is to set up the relationship between time/resources and results qualities, statistically or theoretically. On the other hand, as a black-box based approach, it is hard to explain how DNN learns, especially **the impact of intermediate results from sub layers**, which makes it hard to set up this kind of relationship between time/resources and results qualities for DNN.
   - How can we explain the DNN's learning?
   - Can we set up this relationship based on **explainable machine learning algorithms** (or ensembling explanable algorithms)
 - Decompose with applications and dataset: Customized designs for specific application and dataset to make it possible to be anytime is feasible. **The real challenge is to propose a general approach which decomposes with applications and datasets**.

## Anytime/Adaptive Prediction Algorithms
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

## Anytime DNN Design
 - Challenges for state-of-the-art and our solutions
   - Requires huge training of the original DNN model to support anytime behavior
     - post-optimization based: network pruning/compression, quantization
   - Limited support for spartial-adaptive and system-adaptive
     - adptive to input sparsity and system profiling results

## Updates June 28, 2021
 - Pytorch quantizations on more models
   - Works only for CPU, not GPU
   - Get errors of quantized layers treated as a zero-op
```
Warning: module ConvReLU2d is treated as a zero-op.
Warning: module Identity is treated as a zero-op.
Warning: module Conv2d is treated as a zero-op.
Warning: module ReLU is treated as a zero-op.
Warning: module QFunctional is treated as a zero-op.
Warning: module QuantizableBottleneck is treated as a zero-op.
Warning: module LinearPackedParams is treated as a zero-op.
Warning: module Linear is treated as a zero-op.
Warning: module Quantize is treated as a zero-op.
Warning: module DeQuantize is treated as a zero-op.
Warning: module QuantizableResNet is treated as a zero-op.
Computational complexity:       0.0 GMac
Number of parameters:           0
Traceback (most recent call last):
  File "train_quant.py", line 108, in <module>
    optimizer = optim.SGD(net.parameters(), lr=args.lr, momentum=0.9, weight_decay=5e-4)
  File "/home/cc/venv-adnn/lib/python3.6/site-packages/torch/optim/sgd.py", line 68, in __init__
    super(SGD, self).__init__(params, defaults)
  File "/home/cc/venv-adnn/lib/python3.6/site-packages/torch/optim/optimizer.py", line 47, in __init__
    raise ValueError("optimizer got an empty parameter list")
ValueError: optimizer got an empty parameter list
```
 - How quantization-aware training works
   - Fake quantization opeartions, first introduced in [paper](https://arxiv.org/pdf/1712.05877.pdf)
   - Derivations for step function: Straight-through Estimator (STE)
 - Quantization in TensorFlow
   - [Example code](../codes/tf-quantization-example.py)
   - [QKeras](https://github.com/google/qkeras)
 - Paper's idea:
   - An esemble framework with quantized models adpative to input sparsity and resource profiling

## Update July 12, 2021
 - QKeras's deployment on NVIDIA Jetson AGX/NX
   - Dependency is hard to satisfy: tensorflow>=2.5.0rc0
   - Not supported on Jetson board: https://docs.nvidia.com/deeplearning/frameworks/install-tf-jetson-platform-release-notes/tf-jetson-rel.html#tf-jetson-rel
 - TensorRT's strength
   - GPU supported multiple precision
   - support for majority of the ML frameworks
 - TensorRT-based optimizations:
   - Kernel fusion: combine kernels calls to imporve GPU utilization (vertically and horizontally)
   - Precision calibration: full precision (FP32), half precision (FP16), INT8
   - Kernel auto-tuning: select the optimal kernels based on parameter like batch size, filter-size, and input data size; based on target platform
 - Results on Pytorch TensorRT conversion
   - [torch2trt](https://github.com/NVIDIA-AI-IOT/torch2trt)
   - [Experimental results](../torch2trt-results.md)

```
def torch2trt(module, 
              inputs, 
              input_names=None, 
              output_names=None, 
              log_level=trt.Logger.ERROR, 
              max_batch_size=1,
              fp16_mode=False, 
              max_workspace_size=1<<25, 
              strict_type_constraints=False, 
              keep_network=True, 
              int8_mode=False, 
              int8_calib_dataset=None,
              int8_calib_algorithm=DEFAULT_CALIBRATION_ALGORITHM,
              int8_calib_batch_size=1,
              use_onnx=False,
              **kwargs)
```

### Update July 19, 2021
 - TensorRT model's structure and size
   - unable to access the structure and virtualize: https://stackoverflow.com/questions/65705710/how-can-i-visualize-tensorrt-network-graph
 - Results from ensemble learning in pytorch: https://ensemble-pytorch.readthedocs.io/en/stable/introduction.html
   - Fusion, voting, bagging, gradient boosting, snapshot
   - Image classification on MNIST dataset

 - LeNet with epoch=100:
```
FusionClassifier | Testing Acc: 79.01 % | Training Time: 2367.75 s | Evaluating Time: 1.70 s

VotingClassifier | Testing Acc: 78.48 % | Training Time: 11839.88 s | Evaluating Time: 1.50 s

BaggingClassifier | Testing Acc: 77.30 % | Training Time: 12244.02 s | Evaluating Time: 1.50 s

GradientBoostingClassifier | Testing Acc: 79.09 % | Training Time: 16477.36 s | Evaluating Time: 1.47 s

SnapshotEnsembleClassifier | Testing Acc: 71.01 % | Training Time: 1202.86 s | Evaluating Time: 1.46 s
```

 - Resnet50 with epoch=10:
```
FusionClassifier             | Testing Acc: 65.42 % | Training Time: 2233.73 s | Evaluating Time: 19.49 s

VotingClassifier             | Testing Acc: 71.06 % | Training Time: 3123.60 s | Evaluating Time: 19.63 s

BaggingClassifier            | Testing Acc: 67.01 % | Training Time: 2869.60 s | Evaluating Time: 19.51 s

GradientBoostingClassifier   | Testing Acc: 60.38 % | Training Time: 11111.49 s | Evaluating Time: 19.93 s

SnapshotEnsembleClassifier   | Testing Acc: 66.46 % | Training Time: 329.23 s | Evaluating Time: 19.74 s
```