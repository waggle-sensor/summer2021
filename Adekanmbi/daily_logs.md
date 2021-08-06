# Daily Progress Report

### Project Goals ###

- [X] Create how to test app after docker build
- [X] Trigger app profiling per app/input
- [ ] Send defined profile metric to scheduler
- [X] Integrate app profiler into ECR
- [ ] Send App profile to scheduler

### Week 1 ###

------------

#### Tuesday June 1, 2021 ####

- Completed new student orientation day 1
- Completed new student tile

#### Wednesday June 2, 2021 ####

- Completed new student orientation day 2
- Attended student connect
- Started JHQ training (3/8)
- Request for LCRC access permission

#### Thursday June 3, 2021 ####

- Filled Dayforce time log
- Attended CELS Student Lecture Series on "Detecting COVID in wastewater"
- Can connect to LCRC
- Completed JHQ training (8/8)
- Studying the SAGE ECR source code

#### Friday June 4, 2021 ####

- Attended SAGE Sprint Demo and Retrospective
- Ran successfully Sage ECR Locally as well as trying out API specifications


### Week 2 ###

------------

#### Monday June 7, 2021 ####

- Studied how to use and implement pytest to test apps/plugins on ECR
- Used jenkins to create CI tasks

#### Tuesday June 8, 2021 ####

- Meeting on App Scheduling and Profiling
- Wrote a function to run a docker app using a dockerfile

#### Wednesday June 9, 2021 ####

- Attended Edu weekly Seminar on "How to get into Graduate School"
- Started the implementation of ML App Plugin for ECR App Testing

#### Thursday June 10, 2021 ####

- Created a [Test-Plugin](https://github.com/aabayomi/test-plugin)
- Read Docker documentation on running containers and shell commands

#### Friday June 11, 2021 ####

- Completed the implementation for ECR App testing in Jenkins pipeline.



### Week 3 ###

------------

#### Monday June 14, 2021 ####

- Completed First intern presentation
- Read about Docker in Docker virtualization


#### Tuesday June 15, 2021 ####

- Got feedback on the implementation of app testing in Jenkins
- Read the [Flock](https://dl.acm.org/doi/abs/10.1145/2461381.2461402) paper


#### Wednesday June 16, 2021 ####

- Attended the EDU Weekly Seminar
- Attended DOE Office of Science Seminar



#### Thursday June 17, 2021 ####

- Read the paper on [Image Classification on IoT Edge Devices: Profiling and Modeling](https://arxiv.org/abs/1902.11119)
- Attended Quantum Computing tutorial



#### Friday June 18, 2021 ####

- Modifying ECR code accept docker entrypoints in application specification YAML




### Week 4 ###

------------

#### Monday June 21, 2021 ####

- Modifying ECR code accept docker entrypoints in application specification YAML

#### Tuesday June 22, 2021 ####

- Attended DOE Seminar
- Worked on adding test command in application specification YAML to prevent Shell Injection.

#### Wednesday June 23, 2021 ####

- Attended Student EDU Weekly seminar series 
- Worked on implementing multi-platform build in Jenkins

#### Thursday June 24, 2021 ####


- Worked on implementing multi-platform build in Jenkins

#### Friday June 25, 2021 ####

- Testing and debugging Jenkins Application Test feature.


### Week 5 ###

------------

#### Monday June 28, 2021 ####

- Testing and debugging Jenkins Application Test feature..

#### Tuesday June 29, 2021 ####

- Testing and debugging Jenkins Application Test feature.

#### Wednesday June 30, 2021 ####

- Testing and debugging Jenkins Application Test feature.
- Read through [Jenkins Handbook](https://www.jenkins.io/user-handbook.pdf) on building pipelines

#### Thursday July 1, 2021 ####

- Testing and debugging Jenkins Application Test feature..


#### Friday July 2, 2021 ####

- Completed Testing and debugging Jenkins Application Test feature..

- Started working on Profiling pipeline in Jenkins


### Week 6 ###

------------

#### Tuesday July 6, 2021 ####

- Presented and Discussed my work on Testing and Profiling.
- Created the application testing diagram


#### Wednesday July 7, 2021 ####

- Created a PR for testing on ECR
- Received a feedback to implement test-build loop in Jenkins

#### Thursday July 8, 2021 ####

- Working on implementing a profiling endpoint

#### Friday July 9, 2021 ####

- Completed test-build loop in Jenkins



### Week 7 ###

------------

#### Monday July 12, 2021 ####

- Mid-internship Presentation

#### Tuesday July 13, 2021 ####

- Worked in implementing API Endpoint to trigger app profiling

#### Wednesday July 14, 2021 ####

- Worked in implementing API Endpoint to trigger app profiling

#### Thursday July 15, 2021 ####

- Completed the API endpoint to trigger a Jenkins agent

#### Friday July 16, 2021 ####

- Working on connecting to the Nvidia NX through Jenkins
- Working on Integrating Luke`s Jenkins Code in ECR


### Week 8 ###

------------
#### Monday July 19, 2021 ####

- Started Integration of Luke's Profiler into ECR

#### Tuesday July 20, 2021 ####

- Working in implementing API Endpoint to trigger app profiling

#### Wednesday July 21, 2021 ####

- Working in implementing API Endpoint to trigger app profiling

#### Thursday July 22, 2021 ####

- Completed and Test feature is merged in ECR

#### Friday July 23, 2021 ####

- Integrated Luke`s Jenkins Code in ECR.
- Additional Things work on

       - Check if Jenkins can collect files ?

       - Have the pipeline upload the results to ECR, only the pipeline know a the password to upload file (store using secret)

       - if profiling output is small enough to include in log file output (maybe base64)


### Week 9 ###

------------

#### Monday July 26, 2021 ####

- Debug of shared volume between Application and Jenkins directory to store profiling outputs. 

#### Tuesday July 27, 2021 ####

- Worked on final internship power point presentation  

#### Wednesday July 28, 2021 ####

- Final internship presentation on Sage: Edge Code Repository Application testing and profiling


#### Thursday July 29, 2021 ####

- Worked on integrating profiler in ECR

#### Friday July 30, 2021 ####

Completed profiling in Jenkins and storing results in sage-ecr_db 



### Week 10 ###

------------

#### Monday August 2, 2021 ####

- Created a Video presentation for Learning of the Lawn.

#### Tuesday August 3, 2021 ####

- Demoed app profiling in ECR

#### Wednesday August 4, 2021 ####

- final presentation learning off the lawn
- Created a PR profile code in [branch](https://github.com/sagecontinuum/sage-ecr/tree/profiling-feature-draft)

#### Thursday August 5, 2021 ####

- Completed profile documentation
- Writing white paper

#### Friday August 6, 2021 ####

- last day meeting


### Learning Resources and References ###

1. [Understanding Jenkins Pipeline](https://www.jenkins.io/doc/book/pipeline/)
2. [Effective testing for machine learning systems](https://www.jeremyjordan.me/testing-ml/)
3. [Docker Documentation](https://docs.docker.com/engine/reference/builder/)
4. [ECR Application Testing flow diagram](https://drive.google.com/file/d/1rnv8dIyr29y6SvSCzZHq5Z-5J0xo3wlz/view?usp=sharing)
5. [ECR Discussion](https://docs.google.com/document/d/135ZKehdaxrsKMNi4CTNVXJbzZDDNMD9sIFfVVf5NzMc/edit)
6. [Mid Internship](https://docs.google.com/presentation/d/16kiERiqq-tQBJg4YgfQn4j4VF1rrl0aUIJVfkSNFwoo/edit?usp=sharing)

