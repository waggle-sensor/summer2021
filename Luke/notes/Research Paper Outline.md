### Paper Outline

- Abstract
  - *Will write later*
- Introduction *(Provide literature review for problem at hand)*
  - Why is edge computing relevant?
  - What are the open problems with running multiple neural networks on one device?
- Profiling Tools
  - Tau
    - This tool is helpful to attribute a run cost to each function of an app.
  - Nvprof
  - Self-reporting probes for computing high-level metrics
    - This is helpful for reaching science rules (if an algorithm needs to run at a minimum frame rate)
    - Latency is a necessary metric for the feedback controller to know about
- Profiling Sessions (data analysis on metric usage over time)
  - Automated with Jenkins, Docker, and complete on Nvidia NX hardware
- Live Profiling (real-time planning)
  - Emphasize the novelty of a scientist-friendly framework to deploy edge applications without system interference
  - Results of live profiling
    - Able to build a prototype of an app that computes an inference, reports its status, and sends its status to the metric collector



### The Novelty of Our Approach

- The massive deployment of a variety of edge AI apps on the Sage ecosystem is unlike any other sensor network
- The infrastructure requires a resource management system, both to predict an app's stress and to reconfigure apps on the fly
- AI multi-tenancy is a relatively new concept too

