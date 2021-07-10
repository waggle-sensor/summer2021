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
| Name | Data Type | Input Shapes | torch2trt kwargs | Max Error | Throughput (PyTorch) | Throughput (TensorRT) | Latency (PyTorch) | Latency (TensorRT) |
|------|-----------|--------------|------------------|-----------|----------------------|-----------------------|-------------------|--------------------|
| alexnet | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.16E-02 | 912 | 3.72e+03 | 1.18 | 0.346 |
| squeezenet1_0 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.14E+00 | 255 | 4.53e+03 | 3.85 | 0.299 |
| squeezenet1_1 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.49E+00 | 255 | 4.82e+03 | 3.85 | 0.275 |
| resnet18 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 5.49E+00 | 251 | 3.05e+03 | 3.99 | 0.401 |
| resnet34 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.66E+02 | 142 | 1.63e+03 | 7.04 | 0.654 |
| resnet50 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 6.35E+01 | 105 | 1.53e+03 | 9.52 | 0.734 |
| resnet101 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 0.00E+00 | 52.4 | 813 | 19.1 | 1.08 |
| resnet152 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 0.00E+00 | 35.3 | 558 | 28.3 | 1.47 |
| densenet121 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.06E+00 | 45.1 | 342 | 21.2 | 2.91 |
| densenet169 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.46E+00 | 34.1 | 181 | 29.5 | 5.53 |
| densenet201 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.81E+00 | 27.9 | 121 | 35.7 | 8.24 |
| densenet161 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.91E+00 | 33.9 | 185 | 29.2 | 5.68 |
| vgg11 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 4.01E-01 | 681 | 1.71e+03 | 1.73 | 0.571 |
| vgg13 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.50E-01 | 567 | 1.64e+03 | 2 | 0.692 |
| vgg16 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.93E-01 | 452 | 1.28e+03 | 2.46 | 0.709 |
| vgg19 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.97E-01 | 377 | 1.11e+03 | 2.86 | 0.802 |
| vgg11_bn | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.26E-01 | 538 | 1.72e+03 | 2.1 | 0.557 |
| vgg13_bn | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.58E-01 | 444 | 1.52e+03 | 2.47 | 0.613 |
| vgg16_bn | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.57E-01 | 362 | 1.28e+03 | 2.98 | 0.713 |
| vgg19_bn | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.71E-01 | 305 | 1.11e+03 | 3.52 | 0.799 |
| mobilenet_v2 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 0.00E+00 | 127 | 3.13e+03 | 7.79 | 0.396 |

### FP32 to Precision INT8:

| Name | Data Type | Input Shapes | torch2trt kwargs | Max Error | Throughput (PyTorch) | Throughput (TensorRT) | Latency (PyTorch) | Latency (TensorRT) |
|------|-----------|--------------|------------------|-----------|----------------------|-----------------------|-------------------|--------------------|
| alexnet | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.42E-02 | 1.02e+03 | 3.8e+03 | 1.23 | 0.34 |
| squeezenet1_0 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.84E+00 | 297 | 4.6e+03 | 3.32 | 0.297 |
| squeezenet1_1 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.44E+00 | 300 | 4.99e+03 | 3.33 | 0.271 |
| resnet18 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 6.83E+00 | 310 | 3.07e+03 | 3.12 | 0.338 |
| resnet34 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.18E+02 | 177 | 1.68e+03 | 5.62 | 0.572 |
| resnet50 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.28E+02 | 128 | 1.73e+03 | 7.8 | 0.592 |
| resnet101 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.29E+05 | 59.4 | 851 | 17 | 1.05 |
| resnet152 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 5.79E+07 | 46.2 | 648 | 21.5 | 1.47 |
| densenet121 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.48E+00 | 46.8 | 315 | 22.6 | 3.17 |
| densenet169 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.88E+00 | 32.2 | 169 | 30.9 | 5.94 |
| densenet201 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 4.45E+00 | 28.9 | 121 | 34.4 | 8.28 |
| densenet161 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.25E+00 | 34.6 | 175 | 27.9 | 5.75 |
| vgg11 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.08E-01 | 383 | 1.73e+03 | 2.52 | 0.571 |
| vgg13 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.48E-01 | 310 | 1.76e+03 | 2.91 | 0.624 |
| vgg16 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.99E-01 | 254 | 1.53e+03 | 3.57 | 0.729 |
| vgg19 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.27E-01 | 224 | 1.34e+03 | 4.23 | 0.817 |
| vgg11_bn | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.19E-01 | 375 | 2.03e+03 | 2.48 | 0.556 |
| vgg13_bn | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.26E-01 | 304 | 1.84e+03 | 3.09 | 0.622 |
| vgg16_bn | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.98E-01 | 234 | 1.28e+03 | 3.83 | 0.728 |
| vgg19_bn | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.40E-01 | 204 | 1.24e+03 | 4.47 | 0.824 |
| mobilenet_v2 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 4.91E-09 | 144 | 3.21e+03 | 6.92 | 0.395 |

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

| Name | Data Type | Input Shapes | torch2trt kwargs | Max Error | Throughput (PyTorch) | Throughput (TensorRT) | Latency (PyTorch) | Latency (TensorRT) |
|------|-----------|--------------|------------------|-----------|----------------------|-----------------------|-------------------|--------------------|
| alexnet | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.50E-02 | 263 | 382 | 3.23 | 3.14 |
| squeezenet1_0 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.69E+00 | 135 | 905 | 7.68 | 1.41 |
| squeezenet1_1 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.60E+00 | 147 | 1.02e+03 | 6.67 | 1.25 |
| resnet18 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 5.35E+00 | 145 | 869 | 7.2 | 1.36 |
| resnet34 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.21E+02 | 83.9 | 591 | 12.3 | 2.23 |
| resnet50 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.04E+02 | 60 | 371 | 16.6 | 2.76 |
| resnet101 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 0.00E+00 | 30.2 | 260 | 31.9 | 4.01 |
| resnet152 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 0.00E+00 | 21.5 | 169 | 46.6 | 6.07 |
| densenet121 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.64E+00 | 25.5 | 133 | 38.7 | 6.48 |
| densenet169 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.02E+00 | 16 | 72.1 | 61.4 | 13.7 |
| densenet201 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.57E+00 | 14.7 | 44.3 | 66.1 | 18.8 |
| densenet161 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.87E+00 | 18.6 | 58.1 | 53.2 | 14.8 |
| vgg11 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.02E-01 | 112 | 163 | 9.28 | 6.47 |
| vgg13 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.23E-01 | 89.6 | 151 | 11.2 | 6.95 |
| vgg16 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.26E-01 | 71.5 | 132 | 13.5 | 7.76 |
| vgg19 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.87E-01 | 59.6 | 129 | 18.8 | 10.1 |
| vgg11_bn | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.11E-01 | 110 | 162 | 9.52 | 6.46 |
| vgg13_bn | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.62E-01 | 77.5 | 150 | 11.8 | 7.15 |
| vgg16_bn | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.98E-01 | 69.6 | 139 | 14.4 | 7.55 |
| vgg19_bn | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.09E-01 | 60.7 | 128 | 16.9 | 8.16 |
| mobilenet_v2 | float16 | [(1, 3, 224, 224)] | {'int8_mode': True} | 0.00E+00 | 70 | 1.01e+03 | 14 | 1.3 |

### FP32 to Precision with INT8:

| Name | Data Type | Input Shapes | torch2trt kwargs | Max Error | Throughput (PyTorch) | Throughput (TensorRT) | Latency (PyTorch) | Latency (TensorRT) |
|------|-----------|--------------|------------------|-----------|----------------------|-----------------------|-------------------|--------------------|
| alexnet | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.17E-02 | 215 | 383 | 5.69 | 2.9 |
| squeezenet1_0 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 5.19E+00 | 122 | 986 | 8.2 | 1.23 |
| squeezenet1_1 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.96E+00 | 138 | 868 | 7.29 | 1.29 |
| resnet18 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 6.34E+00 | 81.5 | 1.11e+03 | 12.4 | 1.19 |
| resnet34 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 1.89E+02 | 44.9 | 623 | 22.1 | 1.87 |
| resnet50 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 4.87E+01 | 40.3 | 482 | 23 | 2.44 |
| resnet101 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 5.67E+04 | 22.5 | 273 | 44 | 3.94 |
| resnet152 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 8.15E+07 | 14.6 | 190 | 64.4 | 5.66 |
| densenet121 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.95E+00 | 20.5 | 150 | 48.7 | 6.53 |
| densenet169 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.48E+00 | 14.6 | 81.7 | 67.9 | 12.2 |
| densenet201 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 4.06E+00 | 12.3 | 45.5 | 80.5 | 21.8 |
| densenet161 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.62E+00 | 15.5 | 69.5 | 64.6 | 14.8 |
| vgg11 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.30E-01 | 44.1 | 160 | 22.8 | 6.47 |
| vgg13 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.88E-01 | 34.5 | 150 | 29.2 | 7.06 |
| vgg16 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.45E-01 | 25.6 | 136 | 39.1 | 7.64 |
| vgg19 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.14E-01 | 20.7 | 128 | 48.5 | 8.1 |
| vgg11_bn | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.12E-01 | 42.3 | 160 | 23.6 | 6.57 |
| vgg13_bn | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.53E-01 | 32.6 | 150 | 30.6 | 6.97 |
| vgg16_bn | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 2.86E-01 | 24.9 | 136 | 40.1 | 7.59 |
| vgg19_bn | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 3.93E-01 | 17.4 | 128 | 49.8 | 8.11 |
| mobilenet_v2 | float32 | [(1, 3, 224, 224)] | {'int8_mode': True} | 4.21E-09 | 70.6 | 951 | 13.9 | 1.41 |