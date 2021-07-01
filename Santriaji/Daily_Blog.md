# Daily Blog
Contains daily updates on work done each day.

## Week 1 (06/14 - 06/18)
Goal : Adapting with Argonne environment and completing administration stuffs.

### Monday 06/14
- Attended virtual orientation.
- Attended group's presentation.
- Meeting with Yongho and Liangkai.

### Tuesday 06/15
- Attended erc meeting.
- Discussing how to get NX devices.
- Setting the github for waggle-sensor/summer2021.

### Wednesday 06/16
- Attended impostor seminar.
- Attended DOE seminar.
- Ordered NX devices.
- Learning Jenkins.
- Preparing slides for ERC group feedback.

### Thursday 06/17
- Attended student seminar.
- Learning the profiler block.

### Friday 06/18
- Meeting with Yongho about integration between controller and profiler.
- Meeting material https://docs.google.com/presentation/d/1cXbZWSa0d4oAzT6KGRvQu6rgubJJSXWwwxvnpMKEZUQ/edit?usp=sharing

## Week 2 (06/21 - 06/25)
Goal : Codesign profiling block with ECR Team (Week 2 and Week 3).

### Monday 06/21
- First presentation of intern project.
- Presentation material https://docs.google.com/presentation/d/1GbVx-CiXDouJIGK5lw5Nfc5NUtrbwix7_A0WknlYtOA/edit?usp=sharing
- Finishing TMS training.
- Meeting with Chris for profiling clarification.
- Preparing the profiler-controller design presentation for ECR meeting on the next day.

### Tuesday 06/22
- Meeting with ECR Team.
- Presentation material https://docs.google.com/presentation/d/1JwYcgYLhDVcX99O0ihHhzI8Yi3zKG0zDJZVXwpS8VlU/edit?usp=sharing

### Wednesday 06/23
- Went to Lemont to socialize.
- Read documents from Pete about Live, History and Spesific monitoring.

### Thursday 06/24
- Attended student seminar.
- Read paper about Real Time System in Docker.
- Attended plugin tutorial.
- Decided to start the scheduler with batch and time sharing knobs.

### Thursday 06/25
- Setting up NX for the experiments.

## Week 3 (06/28 - 07/02)
Goal : Codesign profiling block with ECR Team (Week 2 and Week 3).

### Monday 06/28
- Running object pedestrian plugin.
- Running live monitor for plugin.
- Designing the data buffer for plugin.
- Writing presentation for ECR meeting.

### Tuesday 06/29
- ECR Meeting. Slides: https://docs.google.com/presentation/d/1cT0J9ZG8lGCgVt9Xz3aJyh_DDZ2vF2zCuJ7eM1_MQoQ/edit?usp=sharing
- Build a simple live monitoring block with tegrastats, however there will be a problem to splitting and isolating the performance metrics. 

### Wednesday 06/30
- Lunch with team.
- Found out that we can ignore the resource allocation and can succesfully schedule the DNNs if they are running sequentially. 
- Based on this paper https://www.researchgate.net/profile/Zhe-Yang-62/publication/351348112_DeepRT_A_Soft_Real_Time_Scheduler_for_Computer_Vision_Applications_on_the_Edge/links/6092a53a92851c490fbb996f/DeepRT-A-Soft-Real-Time-Scheduler-for-Computer-Vision-Applications-on-the-Edge.pdf

### Thursday 07/01
- Meeting with ECR. Slides: https://docs.google.com/presentation/d/15NMMjdlLsyYLX8HQi8ZqNIiQkNedhJUy4pTkE0aS5LY/edit?usp=sharing
- Found that the assumption of what I can control and suggest for the scientist may differ from the one that is planned.
- To avoid misunderstood in assumption, I plan to write a really detail algorithm and design document such that we are in the same page.
