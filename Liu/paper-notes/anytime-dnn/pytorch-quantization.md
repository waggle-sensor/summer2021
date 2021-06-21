### Introduction to PyTorch Quantization

Quantization refers to techniques for **performing computations and storing tensors at lower bitwidths than floating point precision**. A quantized model executes **some or all of the operations on tensors with integers rather than floating point values.** This allows for a more compact model representation and the use of high performance vectorized operations on many hardware platforms. **PyTorch supports INT8 quantization compared to typical FP32 models allowing for a 4x reduction in the model size and a 4x reduction in memory bandwidth requirements. Hardware support for INT8 computations is typically 2 to 4 times faster compared to FP32 compute.** Quantization is primarily a technique to speed up inference and only the forward pass is supported for quantized operators.

PyTorch supports multiple approaches to quantizing a deep learning model. In most cases the model is trained in FP32 and then the model is converted to INT8. In addition, PyTorch also supports quantization aware training, which models quantization errors in both the forward and backward passes using fake-quantization modules. Note that the entire computation is carried out in floating point. At the end of quantization aware training, PyTorch provides conversion functions to convert the trained model into lower precision.

At lower level, PyTorch provides a way to represent quantized tensors and perform operations with them. They can be used to directly construct models that perform all or part of the computation in lower precision. Higher-level APIs are provided that incorporate typical workflows of converting FP32 model to lower precision with minimal accuracy loss.

PyTorch supports the following backends for running quantized operators efficiently:
 - x86 CPUs with AVX2 support or higher (without AVX2 some operations have inefficient implementations)
 - ARM CPUs (typically found in mobile/embedded devices)


### Reference
 - https://pytorch.org/docs/stable/quantization.html
 - https://pytorch.org/blog/introduction-to-quantization-on-pytorch/