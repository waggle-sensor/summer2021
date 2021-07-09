## torch2trt results on Chameleon Cloud

### Precison with FP16:

| Name | Data Type | Input Shapes | torch2trt kwargs | Max Error | Throughput (PyTorch) | Throughput (TensorRT) | Latency (PyTorch) | Latency (TensorRT) |
|------|-----------|--------------|------------------|-----------|----------------------|-----------------------|-------------------|--------------------|
| alexnet | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 7.06E-05 | 720 | 2.68e+03 | 1.45 | 0.46 |
| squeezenet1_0 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 1.95E-03 | 241 | 3.8e+03 | 3.92 | 0.344 |
| squeezenet1_1 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 9.77E-04 | 239 | 4.42e+03 | 3.95 | 0.307 |
| resnet18 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 7.81E-03 | 250 | 2.37e+03 | 4.01 | 0.489 |
| resnet34 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 1.41E-01 | 140 | 1.3e+03 | 7.08 | 0.743 |
| resnet50 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 9.38E-02 | 105 | 1.19e+03 | 9.48 | 0.873 |
| resnet101 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 0.00E+00 | 50.2 | 620 | 20.5 | 1.35 |
| resnet152 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 0.00E+00 | 30.8 | 426 | 32.3 | 1.93 |
| densenet121 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 3.17E-03 | 40.8 | 267 | 24.3 | 3.82 |
| densenet169 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 3.91E-03 | 33.5 | 163 | 29.8 | 6.12 |
| densenet201 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 3.91E-03 | 27.5 | 110 | 36.3 | 9.1 |
| densenet161 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 3.91E-03 | 29.4 | 141 | 33.8 | 7.14 |
| vgg11 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.26E-03 | 669 | 1.12e+03 | 1.78 | 0.977 |
| vgg13 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 1.91E-03 | 557 | 962 | 2.07 | 0.995 |
| vgg16 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.08E-03 | 452 | 816 | 2.42 | 1.14 |
| vgg19 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.01E-03 | 377 | 773 | 2.81 | 1.3 |
| vgg11_bn | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.27E-03 | 519 | 1.12e+03 | 2.12 | 0.861 |
| vgg13_bn | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 1.77E-03 | 458 | 961 | 2.43 | 0.976 |
| vgg16_bn | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.59E-03 | 365 | 802 | 2.97 | 1.12 |
| vgg19_bn | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 3.42E-03 | 308 | 685 | 3.47 | 1.3 |
| mobilenet_v2 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 0.00E+00 | 128 | 2.66e+03 | 7.7 | 0.453 |

### Precision with INT8:


## torch2trt results on Jetson AGX:

### Precision with FP16:

| Name | Data Type | Input Shapes | torch2trt kwargs | Max Error | Throughput (PyTorch) | Throughput (TensorRT) | Latency (PyTorch) | Latency (TensorRT) |
|------|-----------|--------------|------------------|-----------|----------------------|-----------------------|-------------------|--------------------|
| alexnet | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 1.14E-04 | 272 | 619 | 3.83 | 1.91 |
| squeezenet1_0 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 9.77E-04 | 98.7 | 812 | 9.72 | 1.54 |
| squeezenet1_1 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 4.88E-04 | 107 | 886 | 9.23 | 1.26 |
| resnet18 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 1.95E-02 | 105 | 527 | 9.7 | 2.22 |
| resnet34 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 1.25E-01 | 61.5 | 376 | 16.1 | 3 |
| resnet50 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 1.25E-01 | 44.2 | 328 | 22.7 | 3.56 |
| resnet101 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 0.00E+00 | 23.3 | 168 | 41.8 | 6.01 |
| resnet152 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 0.00E+00 | 17.4 | 81.7 | 56 | 9.41 |
| densenet121 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 9.77E-03 | 21.7 | 104 | 45.9 | 8 |
| densenet169 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 4.88E-03 | 15.9 | 58.2 | 59.3 | 15.7 |
| densenet201 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 1.27E-02 | 14 | 42.7 | 70 | 22.9 |
| densenet161 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 9.77E-03 | 18 | 58.1 | 54.9 | 14.9 |
| vgg11 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.62E-03 | 91.1 | 185 | 9.1 | 5.7 |
| vgg13 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.38E-03 | 91.3 | 155 | 11.1 | 6.8 |
| vgg16 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.96E-03 | 61.7 | 131 | 13.3 | 8.16 |
| vgg19 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.87E-03 | 39.9 | 115 | 15.7 | 9.18 |
| vgg11_bn | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.99E-03 | 87.1 | 187 | 9.45 | 5.6 |
| vgg13_bn | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 3.20E-03 | 77.3 | 140 | 13.6 | 8.54 |
| vgg16_bn | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.72E-03 | 62.2 | 113 | 18.4 | 8.25 |
| vgg19_bn | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 2.93E-03 | 54.5 | 104 | 17.1 | 9.56 |
| mobilenet_v2 | float16 | [(1, 3, 224, 224)] | {'fp16_mode': True} | 0.00E+00 | 69.2 | 830 | 14.4 | 1.53 |

### Precision with INT8:
