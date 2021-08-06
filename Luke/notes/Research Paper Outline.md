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



### Conferences to Submit To

- Hybrid Systems: Computation and Control (HSCC 2022)
  - Focus: "Security, privacy, and resilience for cyber-physical systems with focus on computation and control"
  - Submission deadline: Oct. 29, 2021
  - Acceptance/rejection notifications: January 17, 2022
  - *Should we submit our paper as a regular paper or a case study?*
- International Conference on Engineering of Complex Computer Systems (ICECCS 2022)
  - Focus: "1) Adaptive, self-managing and multi-agent systems 2) Cyber-physical systems and IoT"
  - Abstract submission deadline: Oct. 1, 2021
  - Acceptance/rejection notifications: December 20, 2021
- International Parallel and Distributed Processing Symposium (IPDPS 2022)
  - Focus: "Experiments on the use of novel commercial or research architectures ... performance modeling and analysis of parallel and distributed systems ... **system software support for scientific workflows**"
  - Abstract submission deadline: Oct. 1, 2021
  - Preliminary decision deadline: December 3, 2021

