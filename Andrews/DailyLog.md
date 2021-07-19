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
- Thought I may have figured out time-height plots but I didn't

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
- Started modifying some of his code to work for the reflectivity time-height arrays I need

### June 24
- Sage CV and Clouds Group Meeting
- CELS Student Lecture Series
- Writing Coach Meeting: Principles of Scientific Communication
- Writing plugins for Waggle nodes Tutorial
- Reflectivity time-height arrays: 
    * Code mostly works for 1 volume scan
    * Running into an issue with the xarray dimensions

### June 25
- Fixed code for the time-height arrays with Bobby's help
    * Finally able to get a usable xarray dataset for the reflectivity, lat, lon, and height of the gates closest to a select site for x number of volume scans
- Next week: make/clean up a few plots, probably switch axis from sweeps to gate height, remove double sweeps at low levels due to SAILS

## Week 5 
### June 28
- Writing Coach Meeting: Writing a Scientific Research Paper
- Changed nexrad code to allow for easier selection of times
- Got my code to work for some groups of volume scans but not most of them
    * Looked into dealing with different VCPs
    * Any “nan” values in my Xarray dataset are causing most of the issues
        Matplotlib won’t plot pcolormesh type plots if there are any nans
        Almost all the groups of volume scans I’ve tested are producing at least a handful with my current code
        Experimented with workarounds

### June 29
- Tested out a different way of grabbing radar data from AWS
    * Thought it would fix an issue with certain radar scans and missing days but it turns out it had the same issues
    * Sticking with the nexradaws library because it’s easy to use
    * Note: the day we wanted to work with 11/21/19 doesn’t exist in the AWS nexrad bucket - looks like KVNX was down through 11/25/19
- Rewrote the code to deal with the scans at the top of the hour ending in MDM as PyART cannot read them in

### June 30
- EDU Weekly Seminar: Pathways to Science Career Panel
- Made the required mini-presentation for the Student Connects meeting tomorrow
- Asked Bobby for help dealing with the “nans” in xarray dataset creating the plotting issue with matplotlib
    * One solution: create x amount of evenly spaced height bins for an array of size time by number of height bins. Array will hold scan times and the average reflectivity between 2 height bins
    * Code works for all the days and sets of scans I’ve tested thus far
- Cleaned up the plots

### July 1 
- Weekly Clouds/CV group meeting
- Student Connects presentations
- CELS Student Lecture Series
- Looked into numpy.interp() and scipy.interpolate()
    * Scott suggested it could be useful for the height axis
    * Seems like it certainly could be useful because as VCP changes the heights of the gates will change and the number of sweeps in a scan can also change
    * Can't figure out how I'd apply it to my code
- xarray has interpolation functions too

### July 2
- Found a better way to get rid of the duplicate sweeps from SAILS
    * I want the first of the sweeps (one has radial velocity and one does not)
    * Tried selecting only the sweeps with radial velocity data first --> I suspect it won't work for all cases (SAILS) and it gives the second sweep for a given gate height so this didn't work
    * Tried using the median of the elevation angles in each sweep to identify the unique sweeps and then extract_sweeps to get a radar object with only the unique sweeps (based on: https://gist.github.com/deeplycloudy/d5d4f137dd7496434e09f1fbc2122b0f). Tested it on a few sets of scans and it seems to works well. 
- Still trying to figure out how to best use interpolation

## Week 6 
### July 6 
 - Testing to make sure everything in code works
    * Nexradaws fails if there are tar files in amazon bucket
    * Rewrote code without nexradaws library 
    * Everything else seems to work
 - Next steps:
    * Still need to interpolate to a constant height 
    * For the same pixel (lat/lon of sites) we want data from GOES
    * Want to clean up and get code on the edge code repository (ECR)
    * Looked into ECR plugin example on GitHub: https://github.com/waggle-sensor/plugin-numpy-example 
- Mid-Point Visit with Student Connects leader

### July 7 
 - EDU Weekly Seminar: Creating Effective Oral & Poster Presentations
 - Adjusted code for GOES 16 data from AWS to account for the fact that the default scan mode of the ABI changed in April 2019
    * Now can grab both scan modes (and therefore dates pre April 2019) without issue
 - Want level 1b data (not level 2)
    * Channel 16 (13.3 microns) → 13 micron brightness temps 
    * Channel 1 (0.47 microns) → albedo
    * Channel 13 (10.3 microns) → clean IR temps at ~10 microns
    * Level 1b data just gives us raw radiances, do we have to convert to something else (reflectance/brightness temp) or are we just using the raw values?
 - The native ABI coordinates are East/West scanning angle and North/South elevation angle, both in radians relative to where the satellite is. We want lat/lon coordinates
    * Working on convert to lat/lon so I can grab the pixel closest to the lat/lon of the two sites we’re interested in 
    * 
- Helpful satellite links for reference:
    * https://www.goes-r.gov/downloads/resources/documents/Beginners_Guide_to_GOES-R_Series_Data.pdf 
    * https://www.goes-r.gov/mission/ABI-bands-quick-info.html 


