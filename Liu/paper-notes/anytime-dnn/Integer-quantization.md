### [Integer Quantization for Deep Learning Inference: Principles and Empirical Evaluation](https://arxiv.org/abs/2004.09602)

Authors: Hao Wu, Patrick Judd, Xiaojie Zhang, Mikhail Isaev, Paulius Micikevicius1 (NVIDIA)

#### Summary
 - this paper review the mathematical aspects of quantization parameters and evaluate their choices on a wide range of neural network models for different application domains, including vision, speech, and language
 - focus on quantization techniques that are amenable to acceleration by processors with high-throughput integer math pipelines
 - a workflow for 8-bit quantization that is able to maintain accuracy within 1% of the floating-point baseline on all networks studied

#### Performance benefits for lower-precision formats
 - many processors provide **higher throughput** math pipelines the low-bit formats, which can speed up **math-intensive operations**, such as **convolutions** and **matrix multiplications**
 - smaller word sizes **reduce memory bandwidth pressure**, improving performance for bandwidth-limited computations
 - smaller word sizes lead to **lower memory size requirements**, which can improve cache utilization as well as other aspects of memory-system operation

#### Quantization fundamentals:
 - Two steps of unifrom quantization
   - First, choose the range of the real numbers to be quantized, clamping the values outside this range. 
   - Second, map the real values to integers representable by the bit-width of the quantized representation (round each mapped real value to the closest integer value).
 - Two fundamental operations:
   - Quantize: convert a real number to a quantized integer representation (e.g. from fp32 to int8)
   - Dequantize:convert a number from quantized integer representation to a real number (e.g. from int32 to fp16)
 - Affine quantization
 - Scale quantization

#### Tensor quantization granularity
 - At the coarsest, per-tensor granularity, the same quantization parameters are shared by all elements in the tensor. The finest granularity would have individual quantization parameters per element. Intermediate granularities reuse parameters over various dimensions of the tensor - per row or per column for 2D matrices, per channel for 3D (image-like) tensors, etc.
 - Integer matrix multiplication is possible as long as the quantization granularity is per-row or per-tensor for activations and per-column or per-tensor for weights
 - For maximum performance, activations should use per-tensor quantization granularity.
 - While both affine and scale quantization enable the use of integer arithmetic, affine quantization leads to more computationally expensive inference.
