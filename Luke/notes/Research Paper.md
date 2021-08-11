## Introduction

A feature of any scientific endeavor is data collection. Scientists need data to develop theories about our world and test predictions. Today, there is no shortage of data being produced by the devices around us. However, it can still be a challenge for scientists to get a hold of *relevant* data for their respective field. The Sage Project provides scientists with an innovative solution to data collection that involves computing at the edge.

Edge computing is a new paradigm of computing that brings algorithms closer to the data they process. Edge computing is growing in popularity as more software applications require lower latency responses. Technologies like self-driving cars, AI-infused wearables, and home security systems require this paradigm to operate efficiently, since their design demands low latency for proper function. The Sage Project has adopted this paradigm for its scientific computing initiatives. The Sage Project is a sensor network composed of computer nodes that will bring the strengths of edge computing to domain scientists. *(Background: Are there any other sensor networks like Sage?)*

The Sage network contains a few dozen computer nodes (with more nodes being deployed every month), each supplied with Nvidia NX compute capabilities and a host of environmental sensors. Behind these nodes is the Sage ecosystem, a cyberinfrastructure that manages the operation and deployment of edge applications onto the systems. Within the Sage ecosystem is the edge code repository, or ECR, which acts as a database and testing suite for applications written by scientists. The function of the ECR is critical to the reliable operation of the nodes, since it profiles each app that will be deployed onto the systems. These profiles describe the resource footprint of each application, describing quantities like RAM usage, CPU usage, and GPU bandwidth. It is necessary to obtain an understanding of how these edge applications will perform on profiling datasets before deploying them onto the sensor network, since multiple apps will be running on nodes at once, each consuming a certain quantity of resources. If a car tracking edge app needs X MB of GPU memory to load its model and Y GB/s GPU bandwidth to process frames in real-time, but cannot obtain those resources on a node, then it will not be able to process frames in real time. This will obstruct its science goal, to track cars effectively. On the other hand, if another edge app, say for example a visual anomaly detector, can operate at a lower framerate, say 1fps, but has allocated enough resources for processing at 30fps, then it is achieving its own science goals, but at the cost of other apps. In both situations, predicting the minimum resource requirements of the app is essential to the completion of all app science goals.

Therefore, my team proposes two systems of performance profiling: live profiling and historic profiling. Live profiling refers to the processing of and response to metrics streaming from an edge app in real time. Historic profiling refers to the accumulation and analysis of metrics from an edge app after it has finished executing. Both types of profiling inform scheduling and resource management, but with the nuance that live profiling is the real-time response of the system to a set of edge apps, whereas historic profiling is the predicted response of the system to a set of edge apps. To test the effectiveness of both systems, I developed software for both the ECR and edge nodes.

## Profiling Tools

My team utilized a variety of performance profiling tools in our edge profiling suite. For CPU metrics, we used the Tuning and Analysis Utilities toolkit, or TAU for short. According to TAU's website, "TAU ... is capable of gathering performance information through instrumentation of functions, methods, basic blocks, and statements as well as event-based sampling." **(Insert citation here)** Through Tau's instrumentation it is possible to attribute a run cost to each CPU function of an edge application. This is helpful feedback for scientists who may not be familiar with the run cost of using certain algorithms on our node hardware. Once again, many of the app developers for the Sage Project are scientists who are experts in their own environmental domains (hydrology, ecology, meteorology) but may lack advanced computer engineering knowledge. Providing these scientists with performance feedback will set their expectations for what algorithms can be run on our nodes and at what speed.

Another one of our profiling tools in our edge profiling suite is the Nvidia Profiler. This tool provides insights into application GPU-CPU coordination and how it can be improved. It provides warnings and tips to inform developers writing GPU code how to better utilize the hardware. Although this tool focuses on low-level kernel computations which may not be relevant if the developer is using a popular AI framework like Tensorflow, it can be useful to eliminate low-level overhead that may be slowing the application.

These two tools help monitor the performance of an AI application as it runs in a container. The advantage of using these tools is that neither of them require the scientist to fit a particular format for their application. These tools can simply run in the background and self-instrument the application, discovering which functions consume the most resources. However, to monitor high-level metrics like FPS requires the use of metric self-reporting.

The last profiling tool that we incorporated into our suite is a self-reporting metrics library. This tool, unlike the others, requires app developers to insert performance hooks into their code. The following is an example of how a developer might set up the metrics library and hook their own code:

```
from pywaggle.live_metrics import LiveMetrics
metrics_service = LiveMetrics(...)

metrics_service.start_timer('latency')
...  AI inference code ...
metrics_service.stop_timer('latency')
```



