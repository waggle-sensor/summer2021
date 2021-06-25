## Resources

- CUDA Reference w/ diagrams: https://developer.nvidia.com/blog/cuda-refresher-cuda-programming-model/
- `nvprof` usage
  - `sysmem_read_throughput` is a metric for measuring the throughput between the GPU and RAM?
  - To run in the background and pipe output into files: `-o nvprof_%p_out --log-file nvprof_%p_log &`
  - 