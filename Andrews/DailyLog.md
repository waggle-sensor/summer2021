# Daily Log 

## Week 1 
### June 1 
- Orientation 
- Small group meeting with Scott & Nicola
   * Introductions, project ideas
- Paperwork
- Account setup/most of the getting started tasks listed on Github

### June 2
- Orientation
- Student Connects Meeting
- Learned how to use Git/Github
   * https://guides.github.com/activities/hello-world/
   * https://www.youtube.com/watch?v=SWYqp7iY_Tc
- Reading
   * Cloud tracking with Optical Flow for Short-Term Solar Forecasting: https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.717.888&rep=rep1&type=pdf

### June 3 
- CELS Student Lecture Series
- Goal: narrow down a topic
- Found and read papers/articles related to the topic choices
   * The Computation of Cloud-Base Height from Paired Whole-Sky Imaging Cameras (1995): https://journals.ametsoc.org/view/journals/atot/13/1/1520-0426_1996_013_0097_tcocbh_2_0_co_2.xml?rskey=lBu1Lx&webtoken=6bb0d06f-f328-43d4-b598-96421070db16&tab_body=fulltext-display 
   * https://learnopencv.com/optical-flow-in-opencv/
   * Various other optical flow, thermography, lidar papers

### June 4 
- Completed all of the TMS training modules
- Picked topic
   * External feeds for Sage: Build a plug-in that scrapes public data sources to characterize the column over Argonne's Sage Greenhouse at the ATMOS site and ARM’s Southern Great Plains site. This includes fetching and extracting columns from NEXRAD, GOES16, and HRRR. Label dataset with meteorological phenomena. 

## Week 2 
### June 7 
- More reading
- Looking into where to get model/satellite/radar data for project
- Intro meeting with the writing coach
- Docker tutorial 

### June 8 
- More reading/looking at example code
- PyART Training/code
    * https://github.com/ARM-Development/PyART-Training
    * https://github.com/ARM-Development/PyART-Training/blob/main/2-Cloud_Examples/1-NEXRAD_on_Amazon.ipynb 
- Next steps:
    * Focus will be at Argonne's ATMOS site and ARM's Southern Great Plains site.
    * First thing to do is develop a snippet which will grab a WSR-88D volume from Amazon Web services.
    * Then code to extract a gate from each sweep closest to the lat/lon of the sites.
    * Then grab GOES 16 (S3 as well) and document cloud top temp and emissivity.
    * Look for literature: data fusion between NEXRAD and GOES and ground based sensors

### June 9
- Weekly student seminar: Grad School
- Worked on steps given yesterday
    * Developed code to read in and download WSR-88D volume scans from AWS
    * Extracted the gate closest to the ARM SGP site for each sweep

### June 10 
- Student Connects Meetings
- CELS Student Lecture Series
- Grabbed reflectivity values from the extracted gates
- Looked into reading in GOES 16 data from AWS

### June 11 
- Modified code to try to grab GOES 16 from AWS
    * Works for some products/times but not all
    * Eventually want to grab 13 micron brightness temperatures and albedo from vis
- Next week: make time-height array of NEXRAD data and plot 

## Week 3 
### June 14
- First round of introduction/goals presentations
- Worked on code for NEXRAD plots
    * Added a loop for the volume scans
    * Excluded any files ending in MDM as PyART can't seem to read them in
    * Why are there 2 consecutive sweeps with the same or nearly the same gate height but different reflectivity values? 

### June 15 
- Code for NEXRAD time-height plots
    * SAILS is causing the 2 consecutive sweeps at same gate height (one has radial velocity one doesn't). Use the first reflectivity value for plots
    * Code appears to work and is grabbing the correct values but need to figure out the best way to plot it - what I've tried isn't working

### June 16
- Weekly Student Seminar: Imposter Syndrome
- DOE Office of Science Seminar
- NEXRAD plots
- Searched for relevant literature

### June 17 
- Group meeting
    * Progress since the last meeting
- CELS Student Lecture Series
- Fixed (I think) code to read in GOES 16 data from AWS
    * 13 micron brightness = band 16?
    * Albedo from vis = ?

### June 18
- Made introduction presentation for Monday
- Made/updated this daily log 
- Tile in google slides
- Next week: 
    * Get the time-height plots done
    * Figure out what I need to grab from the satellite data
    * 

## Week 4 
### June 21
- Practiced/gave intro presentation
- 5 newly assigned TMS training courses
- Thought I may have finally figured out time-height plots but I didn't

### June 22
- Finish last four newly assigned training courses in TMS
- DOE Office of Science Seminar: Strategies for Remote Work
- Got example code from Bobby and Jeremy to use as a framework
    * Went through both of them
    * I think I'll use something similar to Bobby's code for making then Xarray dataset and Jeremy's VAD as an example for plotting
    * Will meet with Bobby and ask questions tomorrow

### June 23
- EDU Weekly Seminar: LinkedIn
- Student Connects Meeting
- Meeting with Bobby about his code
- Modified some of his code to work for the reflectivity time-height arrays I need
- 



