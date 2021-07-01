### Week 1: 6/14–6/18
- completed onboarding forms
- attended Dr. Collis' student lecture
- explored Waggle github
- read up on LIDAR, optical flow, Sage project
- reviewed literature on LIDAR optical flow algorithms
- wrote project summary
- prepared student presentation
- [Wavelet-Based Optical Flow for Two-Component Wind Field Estimation from Single Aerosol Lidar Data](https://journals.ametsoc.org/view/journals/atot/32/10/jtech-d-15-0010_1.xml)
- [LiDAR basics](https://www.neonscience.org/resources/learning-hub/tutorials/lidar-basics)
- [Aerosol](https://airbornescience.nasa.gov/instrument/Aerosol%20Lidar)/[atmostpheric](https://en.wikipedia.org/wiki/Atmospheric_lidar) LiDAR

### Week 2: 6/21–6/25
- Monday
    - delivered, watched student presentations
    - got assignment scaffolding from Dr. Collis: started looking at ARM data, code in python, looked more into optical flow
- Tuesday
    - worked on TMS tasks/courses
    - set up Docker
    - looked into [neural networks](https://www.youtube.com/watch?v=aircAruvnKk), more on optical flow from reflectivity/[radar images](https://www.scitepress.org/papers/2011/33326/33326.pdf)
    - parsed zsherman's Python code some more
- Wednesday
    - finished TMS tasks/courses (within 10 days of start date)
    - looked in to [OpenCV code](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) on optical flow
- Thursday
    - lab meeting with Dr. Collis, Dr. Ferrier, Dr. Sankaran, and rest of team
    - attended Dr. Bessac's lecture on statistical practices
    - met with Zach to go over code that generates .gif images of reflectivity data; built code to generate .png's instead
    - attended Sean's lecture on plug-ins for Waggle nodes
- Friday
    - worked on integrating [OpenCV optical flow code](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) into existing radar code data
        - don't understand the [cv.waitkey() code](https://stackoverflow.com/questions/35372700/whats-0xff-for-in-cv2-waitkey1) // and [here](https://technicalmasterblog.wordpress.com/2019/07/03/whats-0xff-for-in-cv2-waitkey1/)
        - began generating some images with similar features (i.e., color blobs) to the ones on OpenCV's Dense Optical Flow example, OpenCV's second optical flow example
        - reviewed documentation associated with [color space conversions](https://docs.opencv.org/3.4/d8/d01/group__imgproc__color__conversions.html)
        - [Common OpenCV Methods](https://medium.com/analytics-vidhya/top-5-inevitable-methods-for-beginners-in-opencv-using-python-9ff8e7ddb5ae)
        - [Managing Environments in Anaconda](https://conda.io/projects/conda/en/latest/user-guide/tasks/manage-environments.html#creating-an-environment-with-commands)
    - attended CELS student social

### Week 3: 6/28–7/2
- Monday
  - continued working on optical flow code
     - uploaded images of Dense Optical Flow generations to GitHub
          - experimented with different "zooms" (how zoomed-in we are to areas of interest in radar scans) and different numbers of frames (optical from from just two consecutive radar images vs. five) 
          - included README.md with questions, thoughts
          - also working on these generations for other the data, i.e., differential reflectivity and velocity, in addition to the reflectivity data
     - began working with code for method of [Lucas-Kanade Optical Flow in OpenCV](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html), OpenCV's first optical flow example 
   - looked into [difference between LiDAR and RADAR data](https://www.yellowscan-lidar.com/knowledge/lidar-vs-radar/)
- Tuesday
  - 
- Wednesday
  - worked on optimizing Lucas-Kanade optical flow models; roadblocks/issues include:
    - 
  - got more direction from Dr. Collis on work-arounds for Lucas-Kanade code
     - zoom into plot more
  - attended Outloud Public Lecture with presentations from Dr. Collis, Dr. Rotsch, Dr. Heitmann, and Dr. Kasthuri
- Thursday
  - lab meeting
  - weekly lecture with Aleksandr Obabko
  - (sharing progress, plots, code with team)
  - updating documentation of process
  - looking into [MatLab's optical flow algorithms](https://www.mathworks.com/discovery/optical-flow.html) and [Computer Vision Toolkit](https://www.mathworks.com/products/computer-vision.html)
- Friday





