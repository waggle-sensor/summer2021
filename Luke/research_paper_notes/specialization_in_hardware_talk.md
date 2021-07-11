## Specialization in Hardware Architectures for Deep Learning

- Talk: *https://www.youtube.com/watch?v=LUPWZ-LC0XE*
- FINN is a compiler that takes neural network layer configurations (encoded in some specific format) and converts that to a HLS and then to hardware
- With FPGA's you can throw as many resources at a problem that you need, possibly to obtain inferencing up to the clock rate
  - Mixed precision options are also available
- Brevitas is a tool that reduces the precision but retains accuracy
- FINN can "unroll" memory so that no BRAMs or URAMs are used (external memories on the board), but only on-chip memories are used
  - Fine-grained sparsity also leads to a speed-up because zero-weight computations are removed