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

### Wednesday 6/23
- Updated TAU wrapper to take filename.py as input
- Met with Luke to discuss plans for the profiler
  - build MVP(minimum viable profiler) first
  - Get black box profiler that
    - Gives min, max, avg, std dev of:
      - GPU (luke, NVidia tool)
      - CPU (Chris, tau)
      - RAM (Chris, tau)
    - Input and Outputs args and profile data in JSON key, value pairs
- Trying to get the object dectection test to work
  - Made need access to an NX
  - Not having much luck building locally (linux/amd64)

### Thursday 6/24
- Not as much progress as I would have hoped for today
  - Spent most of the day trying to configure the object detector plugin to work locally on my linux/amd64 machine
    - I was able to build the docker container with some modifications to the dockerfile, but it fails when it uses the RUN command(/bin/sh vs /bin/bash)
- Modified wrapper to test ram by loading in a large file
- Found a python script for stress testing ram
  - Couldn't get this to work with my wrapper for some reason, lots of NameErrors

### Friday 6/25
- Updated wrapper to work with new custom memory and cpu stress test
  - wrapper can handle CLI args now too
- Met with Luke, Sean, and Yongho
  - discussed pywaggle instrumentation
  - Mapped out how ECR team will collab with pywaggle
  - On the radar -> unix socket and JSON
- Got access to NXs (thank you Yongho!)
  - setting up object counter plugin to begin experimenting with TAU on it

## Week 4 (6/28 - 7/2)

How is it week 4 already!?

### Monday (6/28)
- Troubleshooting and trial and error to setup object detector plugin on NX
- Makefile didn't work
- Pulling didn't work
- Messaged Luke and Aji for help
  - need to run playback server
- Messaged Yongho
  - config.json had to be changed on the nx
- I can sucussfully run the object detector plugin docker image now! Ready to be profiled
- Installing TAU
  - everything is downloaded on NX
  - weird install bug after make install(configure was fine)
  - Hopefully I can fix this tomorrow

### Tuesday (6/29)
- ECR meeting this morning
  - follow up meeting on Thursday from 2-4pm
- After about a day of troubleshooting I finallly got tau installed on the NX
  - couldn't install pdt but that shouldn't be necessary
  - auto.py and manual.py both work, meaning that auto and manual instrumentation of tau for python works
  - pprof also works and parses the profile output
  - Now to test my wrapper tomorrow morning(with my example test) then with object detector plugin
    
### Wednesday (6/30)
- my wrapper works on the nx
  - tested with simple custom test
  - not sure how to set it up with the docker container
  - need to be able to build the container manaully, then should be as simple as changing the entrypoint in the dockerfile
- wrote and pushed Tau setup and wrapper.py to custom branch on app_profile git repo

### Thursday (7/1)
- Tried adding memory profiling to TAU tool
  - Compiler errors and I'm not sure how to fix them, likely an include problem
  - edited some file for TauUserEvent
  - says no type
- Reinstalled base version
- Presented tool and wrapper in meeting with Yongho, Yomi, Luke, and Aji
  - I have a better idea of the pipeline now
  - Top objective for me is to begin getting high level stats because I have access to source code, Luke already seems to easily get CPU, GPU, and RAM
- Attempted to run object-counter plugin through wrapper
  - Yongho mentioned in the meeting that I should only need to modify the Dockerfile but that didn't seem to do anything
    - I believe I need to build a new image with my changes to the dockerfile
    - had to uninstall and reinstall docker to the latest version
    - error: RUN sage-cli.py storage files download BUCKET_ID_MODEL coco_ssd_resnet50_300_fp32.pth --target /app/coco_ssd_resnet50_300_fp32 pth:                                                               
        #10 1.656 EXCEPTION IN (/usr/local/bin/sage-cli.py, LINE 320 "sage_storage.downloadFile(host=ctx.obj['SAGE_STORE_URL'], token=ctx.obj['TOKEN'], bucketID=bucket_id, key=key,  target=target)"):            
        #10 1.656 Invalid URL 'HOST/api/v1/objects/BUCKET_ID_MODEL/coco_ssd_resnet50_300_fp32.pth': No schema supplied. Perhaps you meant http://HOST/api/v1/objects/BUCKET_ID_MODEL/coco_ssd_resnet50_300_fp32.pth?
        ------
        error: failed to solve: rpc error: code = Unknown desc = executor failed running [/bin/sh -c sage-cli.py storage files download ${BUCKET_ID_MODEL} coco_ssd_resnet50_300_fp32.pth --target /app/coco_ssd_resnet50_300_fp32.pth]: exit code: 1
        Makefile:8: recipe for target 'image' failed
        make: *** [image] Error 1

### Friday (7/2)

- Working on running the wrapper on the app within the object counter container
- Tried editing the dockerfile and running
  - I had a good feeling this would not work but wanted to try anyway
- Tried rebuilding the image locally
  - for the n-th time I still can do this, above output from yesterday is still as far as I've gotten
- Found a way to change the entrypoint from the docker run command
  - docker run --entrypoint "python3" options and stuff wrapper.py app.py more options
  - docker run -ti --rm  --entrypoint "python3" --name objcounter -v /home/nvidia/data-config.json:/run/waggle/data-config.json --runtime nvidia --network host waggle/plugin-objectcounter:0.0.0 wrappertest.py app.py -stream bottom_image -object person -interval 1 
  - This actually runs! (kinda)
  - TAU doesn't exist in the container, so import errors when wrappertest starts
  - working on importing tau into the container through docker cp and commit
    - docker cp file tempcontainer/path
    - docker commit tempcontainer image
  - can use -e to environment variables
- here but still errors. I probably have to install TAU into the container
  - docker run -ti --rm -e PATH="/app/tau-2.30.1/arm64_linux/bin:$PATH" -e PYTHONPATH="/app/tau-2.30.1/arm64_linux/lib/bindings-python" --entrypoint "python3" --name objcounter -v /home/nvidia/data-config.json:/run/waggle/data-config.json --runtime nvidia --network host waggle/plugin-objectcounter:0.0.0 wrappertest.py app.py -stream bottom_image -object person -interval 1 

  ## Week 5 (7/6-7/9)

  ### Tuesday (7/6)
  - docker run -ti --rm  --entrypoint "python3" --name objcounter -v /home/nvidia/data-config.json:/run/waggle/data-config.json -v /home/nvidia/Documents/tau-2.30.1:/app/tau --runtime nvidia --network host waggle/plugin-objectcounter:0.0.0 wrappertest.py app.py -stream bottom_image -object person -interval 1
    - AttributeError: module 'tau' has no attribute 'run'
  - docker run -ti --rm  --entrypoint "python3" --name objcounter -v /home/nvidia/data-config.json:/run/waggle/data-config.json -v /home/nvidia/Documents/tau-2.30.1:/app/tau -e "PYTHONPATH=/app/tau/arm64_linux/lib/bindings-python" --runtime nvidia --network host waggle/plugin-objectcounter:0.0.0 wrappertest.py app.py -stream bottom_image -object person -interval 1
    - closer
    - Traceback (most recent call last):
      File "wrappertest.py", line 1, in <module>
          import tau
      File "/app/tau/arm64_linux/lib/bindings-python/tau.py", line 7, in <module>
          import ctau_impl
      ImportError: libbfd-2.24-system.so: cannot open shared object file: No such file or directory
  
  ### Wednesday (7/7)
  - GREAT NEWS!
    - I found a way to install tau and get it working within the container itself
      - I set the entrypoint to bin/sh and configured from there after using volumes
      - I have to manually set path and pythonpath
      - and find all the appropriate libraries
    - The tool once configures works automatically like it does locally
    - outputs a profile.0.0.0 files and pprof parses it
  - Some problems with this approach
    - goes away when I close the container
      - need to find a way to make the install persistant
      - need to find a way to access profile output using docker cp
  - This is huge we can get the pipeline working now!

  ### Thursday (7/8)

  - Major dockerfile modifications
  - profiling pipelines works
    - make the image, run the container, get output, put output in volume
    - see readme.md in application-profiling repo
    - not seemless to setup but it will be once its running
    - Hooray!

### Friday (7/8)

- Met with Luke to discuss my pipeline
  - it works!
- Planning to make a docker repo so someone can just use FROM in the dockerfile


## Week 6 (7/12-7/16)

### Monday (7/12)

- Working on building my own image using the waggle cuda plugin base
- remember to us -ti to make it interactive
- new simple dockerfile with entrypoint set to /bin/sh can open up to terminal
  - great, I was a little worried that the plugin had the higher functionality, but this is plently to work with
- I hope using FROM waggle/plugin-base:1.1.1-ml-cuda10.2-l4t won't break things if someone else is using it as well (like in objectcounter)
  - I will have to test this, I assumed it would stack
  
### Tuesday (7/13)
- Successfully built a new docker image with a fresh dockerfile that comes with tau for python setup and installed
- created my own docker repo for this image
  - can be pulled at chrispkraemer/tauprofiler:0.0.0
- Tomorrow I will test if this can be layered with the base and/or the object plugin

### Wednesday (7/14)
- Lots of bugs to sort though while layering
  - also takes forever to build
  - I have to build both the tauprofile image and object counter image each time I change the tauprofile dockerfile(in a significant way)


### Thursday (7/15)
- I was able to successfully layer my chrispkraemer/tauprofiler:0.0.0 image with the object counter plugin
- the wrapper and app work
- tomorrow I will test the shell script and make things as automated as possible

