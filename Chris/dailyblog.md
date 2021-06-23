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
- [An Automated Tool Profiling Service for the Cloud](https://dl-acm-org.turing.library.northwestern.edu/doi/10.1109/CCGrid.2016.57)
- Perforamce Co-Pilot

## Week 2 (6/14-6/18)

### Monday 6/14
- Big Group Presentations

### Tuesday 6/15
- ECR meeting

### Wednesday 6/16
- Developed Sample python ml script(just something simple to begin profiling)
- Looking into NVidia NGC catalog
- Trying to get TAU or PAPI to work with example script, plan to build up from there
- A simple wrapper should be doable this week

### Thursday 6/17
- Still trying to get TAU working... Not sure of the problem
- Tomorrow I will just try using pytau instead of the automatic instrumentation
- This should at least give me some stats

### Friday 6/18
- Got TAU working after much trial and error
- TAU works manually and with automatic instrumentation in python

## Week 3 (6/21-6/25)

### Monday 6/21
- Sucussfully built a TAU wrapper for Python
  - tau.run calls main in the example program
  - speaking of which, is there an example ml program I can test on
- Morning presentation went well, need to fill out my one page slide/card thing
- Met with Aji to define/discuss the profiler and how knobs will interact
- Installed cuda on my local vm to connect that with TAU
- Reconfiguring TAU to work with -PROFILEMEMORY arg

### Tuesday 6/22
- ECR meeting with Yomi, Aji, Luke, and Yongho
- Built simple, custom stress test in python(CPU), now for a RAM one
- Wrapper works for this new test
- Some trouble getting the -PROFILEMEMORY TAU option to work
- After some time working with cuda/tau, I think it needs to be installed separately and use tau_exec
- export TAU_TRACK_MEMORY_FOOTPRINT=1 seems to give some memory sampling
- tau setup
  - download and unzip tau
  - download and unzip pdt and etc
- my commands:
  - ./configure  -bfd=download -dwarf=download -unwind=download -iowrapper -pdt=/home/ckraemer/Documents/Argonne/pdtoolkit-3.25.1 -pythoninc=/usr/include/python3.8 -pythonlib=/usr/lib/x86_64-linux-gnu
  - make install
  - export TAU_TRACK_MEMORY_FOOTPRINT=1


