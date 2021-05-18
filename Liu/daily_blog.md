# Daily Notes - Liangkai Liu

## Week 1 (May 10 to May 14)

### May 10, 2020
#### Work Done:
 - I-20 CPT paperwork modification
 - Remote I-9 E-verify
 - Background check
 - Walk through Pytorch tutorials

### May 11, 2020
#### Work Done:
 - Set up account access to LCRC and JLSE 
 - Pytorch tutorial
 - Read papers on anytime DNN
 - Training anytime NN provided from "Anytime Neural Prediction via Slicing Networks Vertically" 

Github: https://github.com/hankook/IResNeXt

<img src="images/anytime-training.jpg" width="200">

### May 12, 2020
#### Work Done:
 - Read papers on anytime DNN ([Zilberstein-AAAI-1996](../Liu/paper-notes/Zilberstein-AAAI-1996.md), [Dietterich-MCS-2000](paper-notes/Dietterich-MCS-2000.md), and [Lee-Arxiv-2018](paper-notes/Lee-Arxiv-2018.md))
 - Get anytime NN models for CIFAR10 and CIFAR100 provided from "Anytime Neural Prediction via Slicing Networks Vertically" 

CIFAR10:             |  CIFAR100:
:-------------------------:|:-------------------------:
![](images/cifar10.png)  |  ![](images/cifar100.png)

### May 13, 2020
#### Work Done:
 - Read papers on anytime DNN ([Dietterich-MCS-2000](paper-notes/Dietterich-MCS-2000.md), and [Lee-Arxiv-2018](paper-notes/Lee-Arxiv-2018.md))
 - Implement the code from BranchyNet (https://github.com/kunglab/branchynet) and Distributed DNN (https://github.com/kunglab/ddnn).

### May 14, 2020
#### Work Done:
 - Read papers on anytime DNN ([BranchNet-ICPP-2016](paper-notes/BranchNet-ICPP-2016.md), and [DistributedDNN-ICDCS-2017](paper-notes/DistributedDNN-ICDCS-2017.md))
 - Set up access to Chameleon cluster and implement BranchyNet (https://github.com/kunglab/branchynet)
   - The code is based on Python2 and several dependent libraries' version are old
   - Error when running the code:
```
(branchnet) cc@llk-test:~/branchynet$ ./get_results.sh
Please download data from https://drive.google.com/file/d/0Byyuc5LmNmJPWUc5dVdUSms3U1E/view?usp=sharing and put it at datasets/data/pcifar10/data.npz
mkdir: cannot create directory ‘_models’: File exists
mkdir: cannot create directory ‘_figs’: File exists
/home/cc/anaconda3/envs/branchnet/lib/python2.7/site-packages/chainer/cuda.py:90: UserWarning: cuDNN is not enabled.
Please reinstall chainer after you install cudnn
(see https://github.com/pfnet/chainer#installation).
  'cuDNN is not enabled.\n'
Traceback (most recent call last):
  File "experiment_lenet_mnist.py", line 43, in <module>
    num_epoch=TRAIN_NUM_EPOCHS)
  File "/home/cc/branchynet/branchynet/utils.py", line 246, in train
    losses,accuracies = branchyNet.train_main(x,t)
  File "/home/cc/branchynet/branchynet/net.py", line 383, in train_main
    return self.train_model(self.main,x,t)
  File "/home/cc/branchynet/branchynet/net.py", line 356, in train_model
    loss = self.main.train(x,t)
  File "/home/cc/branchynet/branchynet/links/links.py", line 130, in train
    h = self(x,False,starti,endi)
  File "/home/cc/branchynet/branchynet/links/links.py", line 124, in __call__
    h = link(h)
  File "/home/cc/anaconda3/envs/branchnet/lib/python2.7/site-packages/chainer/links/connection/convolution_2d.py", line 101, in __call__
    x, self.W, self.b, self.stride, self.pad, self.use_cudnn)
  File "/home/cc/anaconda3/envs/branchnet/lib/python2.7/site-packages/chainer/functions/connection/convolution_2d.py", line 318, in convolution_2d
    return func(x, W, b)
  File "/home/cc/anaconda3/envs/branchnet/lib/python2.7/site-packages/chainer/function.py", line 197, in __call__
    outputs = self.forward(in_data)
  File "/home/cc/anaconda3/envs/branchnet/lib/python2.7/site-packages/chainer/function.py", line 309, in forward
    return self.forward_gpu(inputs)
  File "/home/cc/anaconda3/envs/branchnet/lib/python2.7/site-packages/chainer/functions/connection/convolution_2d.py", line 133, in forward_gpu
    cover_all=self.cover_all)
  File "/home/cc/anaconda3/envs/branchnet/lib/python2.7/site-packages/chainer/utils/conv.py", line 73, in im2col_gpu
    h, w, out_h, out_w, kh, kw, sy, sx, ph, pw, dy, dx, col)
  File "cupy/core/elementwise.pxi", line 545, in cupy.core.core.ElementwiseKernel.__call__ (cupy/core/core.cpp:35812)
  File "cupy/util.pyx", line 35, in cupy.util.memoize.decorator.ret (cupy/util.cpp:1259)
  File "cupy/core/elementwise.pxi", line 405, in cupy.core.core._get_elementwise_kernel (cupy/core/core.cpp:34288)
  File "cupy/core/elementwise.pxi", line 12, in cupy.core.core._get_simple_elementwise_kernel (cupy/core/core.cpp:27667)
  File "cupy/core/elementwise.pxi", line 32, in cupy.core.core._get_simple_elementwise_kernel (cupy/core/core.cpp:27489)
  File "cupy/core/carray.pxi", line 87, in cupy.core.core.compile_with_cache (cupy/core/core.cpp:27176)
  File "/home/cc/anaconda3/envs/branchnet/lib/python2.7/site-packages/cupy/cuda/compiler.py", line 153, in compile_with_cache
    cubin = nvcc(source, options, arch)
  File "/home/cc/anaconda3/envs/branchnet/lib/python2.7/site-packages/cupy/cuda/compiler.py", line 78, in nvcc
    _run_nvcc(cmd, root_dir)
  File "/home/cc/anaconda3/envs/branchnet/lib/python2.7/site-packages/cupy/cuda/compiler.py", line 56, in _run_nvcc
    raise RuntimeError(msg)
RuntimeError: `nvcc` command returns non-zero exit status.
command: ['nvcc', '--cubin', '-arch', 'sm_75', '/tmp/tmp5tgPag/kern.cu']
return-code: 1
stdout/stderr:
/tmp/tmp5tgPag/kern.cu(14): error: identifier "__float2half_rn" is undefined

/tmp/tmp5tgPag/kern.cu(17): error: identifier "__float2half_rn" is undefined

/tmp/tmp5tgPag/kern.cu(20): error: identifier "__float2half_rn" is undefined

/tmp/tmp5tgPag/kern.cu(23): error: identifier "__float2half_rn" is undefined

/tmp/tmp5tgPag/kern.cu(26): error: identifier "__float2half_rn" is undefined

/tmp/tmp5tgPag/kern.cu(29): error: identifier "__float2half_rn" is undefined

/tmp/tmp5tgPag/kern.cu(32): error: identifier "__float2half_rn" is undefined

/tmp/tmp5tgPag/kern.cu(35): error: identifier "__half2float" is undefined

8 errors detected in the compilation of "/tmp/tmpxft_00004622_00000000-6_kern.cpp1.ii".
```

## Week 2 (May 17 to May 21)

### May 17, 2020
#### Work Done:
 - Paperwork on Tax files
 - Walk through Pytorch tutorials
 - Read papers on anytime DNN ([BranchNet-ICPP-2016](paper-notes/BranchNet-ICPP-2016.md), and [DistributedDNN-ICDCS-2017](paper-notes/DistributedDNN-ICDCS-2017.md))
 - Work through the [Neural Networks and Deep Learning book's](http://neuralnetworksanddeeplearning.com/) chapter 2 and chapter 3
   - how stochastic gredient decent works
   - backpropogation's prove
   - Implementation codes using SGD and backpropogation

#### Questions and Thoughs for Anytime DNN:

 - Motivation of Anytime DNN: Compared with research activities in building more powerful hardware/accelerators and architectures to speed up the DNN’s inference time, anytime DNN seems to be less competitive. The usage of it seems to be limited to **resource-constraint scenarios** and there is **no penalty for performance degradation**.
 - Contradictions in building anytime DNN: According to Zilberstein’s paper (AAAI-1996), I think one of the core part of anytime algorithm is to set up the relationship between time/resources and results qualities, statistically or theoretically. On the other hand, as a black-box based approach, it is hard to explain how DNN learns, especially **the impact of intermediate results from sub layers**, which makes it hard to set up this kind of relationship between time/resources and results qualities for DNN. 
 - Decompose with applications and dataset: Customized designs for specific application and dataset to make it possible to be anytime is feasible. **The real challenge is to propose a general approach which decomposes with applications and datasets**.
