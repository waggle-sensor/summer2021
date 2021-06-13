# Chris Daily Blog  
For keeping records of progress.  

## Week 1 (6/7-6/11)  

### Monday 6/7  
- Orientation  
- Onboarding  
- Met with Yongho and Luke  

### Tuesday 6/8
- ECR meeting with Wolfgang, Yongho, Yomi, and Luke  
- Onboarding
- Literature review for profiling  

### Wednesday 6/9
- Onboarding(why are there so many TMS trainings?)
- Papers on profiling
- [FlockLab](https://dl.acm.org/doi/abs/10.1145/2461381.2461402)
- [Clairvoyant](https://dl.acm.org/doi/abs/10.1145/1322263.1322282)
- [Passive diagnosis for wireless sensor networks](https://ieeexplore.ieee.org/abstract/document/5356174)
- [Declarative Tracepoints](https://dl.acm.org/doi/abs/10.1145/1460412.1460422)
- [Caliper](https://ieeexplore.ieee.org/abstract/document/7877125)

### Thursday 6/10
- Onboarding (should be) complete
- Should probably schedule a meeting to further discuss profiling
- Compilers are a good route for profiling
- [Amulet](https://dl.acm.org/doi/10.1145/2994551.2994554)
- [NOELLE](https://arxiv.org/abs/2102.05081)
    - Profiler (PRO). NOELLE provides several code profilers,the ability to embed their results into IR files, and abstractions to facilitate high-level queries on such data. Examples
      of queries that can be performed are the hotness of a code region (e.g., a loop, an SCC of a dependence graph), loopspecific information (e.g., loop iteration count, average loop iteration count per invocation), and function-specific information (e.g., the average number of times that an invocation of a function invokes another).
    - NOELLE uses LLVM so a python frontend/wrapper would be needed, we can probably find one though.
- Important metrics:
  - hot path
  - memory leaks
  - what uses the most CPU
  - how many times each function gets called
- Good tool to look at: [Valgrind](https://valgrind.org/)

### Friday 6/11
- Experimenting with Valgrind
