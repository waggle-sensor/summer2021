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

### July 8 
- Weekly Clouds and CV group meeting
    * Want to grab a 10 x 10 array of pixels over the SGP site rather than a single pixel so maybe we can look at flow over the top
- DOE Office of Science Seminar
- Tutorial/office hours for plugin development/getting code on ECR
    * Learned how to get code onto ECR (used the numpy example template on github) 
    * Definitely want to make a plugin --> we want to collect data from GOES and NEXRAD at the nodes which can be input to ML codes (could be useful for ex. Seongha's recent work: https://www.osti.gov/biblio/1798308)
    * Will try to edit the example with some of my code next week and ask questions

### July 9 
- Worked on converting the x,y coords to lat/lon
- Tried converting using the equations given in: https://www.goes-r.gov/users/docs/PUG-L1b-vol3.pdf, then added lat/lon to the dataframe. Didn’t seem like there’s a straightforward way to select by lat/lon
- Tried pyproj
    * Made a map object for the geostationary projection and then transformed the           
    * Coordinates to lat/lon. Lat/lon values really close to the above method
- Tried using Cartopy
    * For basic georeferenced plotting want geostationary projection
    * To return a pixel value for a given lat/lon: https://stackoverflow.com/questions/66433948/get-nearest-pixel-value-from-satellite-image-using-latitude-longitude-coordinate 
- Next week:
    * Figure out lat/lon conversion so can select 10x10 pixels (do we want just the pixel values or the pixels themselves?)
    * Work on getting radar code into ECR

## Week 7 
### July 12
- Midpoint Presentations (round 1)
- Writing Coach Meeting: Workshop for Writing Abstracts
- Read Seongha's paper 
- Read about Amazon S3
- Trying to extract pixels/pixel values based on converted (lat/lon) coordinates
    * Converted x,y satellite coords (in radians) to lat/lon using Cartopy
 
 ### July 13
 - Kayak event

### July 14
 - EDU Weekly Seminar: Science Innovations for a Circular Economy Initiative at Argonne
 - TRACER Meeting
 - Satellite code - select and download GOES 16 or 17 images by band/channel between the desired start and end time from AWS S3 
    * Fixed time selection in satellite code, cleaned it up
    * Made very similar script but with the option to download all 16 bands (ABI-L2-MCMIPC) rather than just one at a time 
    * Made some basic georeferenced sat plots with cartopy
    * Still stuck on extracting pixels around the SGP lat/lon

### July 15
 - CELS Student Lecture Series 
 - Clouds/CV Meeting
 - Started the powerpoint for Monday's midpoint presentation
 - Finally figured out a method to extract 10x10 grids (based on: https://github.com/blaylockbk/pyBKB_v3/blob/master/demo/Nearest_lat-lon_Grid.ipynb)

### July 16 
 - Worked on midpoint presentation PowerPoint for Monday
 - Forecasting and meeting for TRACER
 - Required SEC 160 TMS Training
 - Next steps:
    * Clean up the code for the grids
    * Get code into ECR
    * Work with Seongha to look at that day at the SGP
    * Do optical flow on the data and compare it to what Matt is seeing
        -> Does the motion we see from the ground match up with what we see with GOES? 
 - Q: What GOES 16 band/bands would work best for optical flow?

## Week 8 
### July 19
 - Practiced/gave midpoint presentation
 - Required EVS Safety Orientation
 - TRACER Meeting
 - Cleaned up and tested the code for extracting the array of pixels

### July 20
 - Reading on optical flow: https://learnopencv.com/optical-flow-in-opencv/; Farneback: https://www.diva-portal.org/smash/get/diva2:273847/FULLTEXT01.pdf
 - Finding/reading literature on optical flow on satellite data including:
    * Deriving AMVs from Geostationary Satellite Images Using Optical Flow Algorithm Based on Polynomial Expansion: https://journals.ametsoc.org/view/journals/atot/33/8/jtech-d-16-0013_1.xml 
        -- Used Farneback algorithm on Himawari-7; for cloud motion vectors used IR (5km spatial resolution, 30 minute temporal resolution)
    * https://www.star.nesdis.noaa.gov/star/documents/meetings/2020JPSSGOES/Posters/B_23_Apke_GPGS_2020_Poster.pdf (research poster on applying optical flow to satellite data)
    * General thoughts: Seems like people have used IR and/or visible bands to get cloud motion vectors). Band two has the highest resolution so I think I’ll try that first. From what I’ve seen in the literature so far, dense optical flow (DOF) seems to be the way to go. Other people have used Farneback with success so that’s where I’ll start algorithm-wise.  
 - TRACER meeting
 - Made a video with a few images that I'll try to feed that through Matt's code

### July 21
 - EDU Weekly Seminar
 - Student Connects meeting
    * Need one slide (2 min) presentation for next week
 - Writing Coach Meeting: Workshop on Oral and Poster Presentations
 - Spent most of the day trying to get my video of 5 satellite images to work with Matt's optical flow code
     * Mostly seems to work at this point, just need to figure out one error at the end. However, most of the motion is at the edge of the images so I'd eventually like to play around with something other than the default Farneback algorithm parameters. Also going to experiment with different sized images and maybe different satellite bands.
 - TRACER meeting

### June 22
 - Clouds and CV meeting
 - Got code into the ECR (not a working plugin yet); updated the Dockerfile, sage.yaml, requirements.txt. 
      * The basic satellite plugin will download GOES 16 or 17 images between a start and an end time for a particular channel
 - Selected a different time period (17:22-19:03Z) with more scattered clouds for dense OF because I think that’ll work better than the times I was testing it with originally (clouds were pretty stationary)
 - Made a movie of those times and tried OF on band 2 (visible)
    * Tried it on a couple different sized visible satellite images (5x5, 20x20, 80x80 km); it seems like the larger ones do a much better job of capturing the larger scale motion
 - TRACER meeting

### June 23 
 - Working on the SULI deliverables (paper)
 - Next week:
    * More optical flow reading - look into adjusting parameters from defaults and how to get flow in real units rather than pixel units
    * Maybe try the Lucas-Kanade method or a mask to get better OF results 
    * Final presentation for the Waggle group
    * More work on deliverables

## Week 9
### June 26
 - Got ARM ceilometer data and sounding data from Lamont, OK for 11/21/2019; will compare motion from optical flow to these observations
 - Haven't found anything thus far on how to convert pixel units to m/s or knots
    * (Magnitude in pixel units * length of pixel in meters) / time in seconds between images?
 - Tried dense OF on IR for 17-19Z period
    * Looks pretty similiar to dense OF on the larger
 - More reading: https://journals.ametsoc.org/view/journals/atot/33/8/jtech-d-16-0013_1.xml#bib30, https://www.diva-portal.org/smash/get/diva2:273847/FULLTEXT01.pdf

### June 27
 - Made final presentation for Waggle/Sage group 
 - Working on deliverables

### June 28
- EDU Weekly Seminar
- Practiced/gave final presentation
- Converted the magnitude of the motion output by optical flow to m/s to compare to actual observations at the SGP site
    * Using the 18Z sounding out of Lamont, OK
    * From Skew-T it looks like winds are between 5-10 m/s. Winds are out of the north in the cloud layer and out of west-southwest just above
    * Optical flow is giving average speeds over the two hour (17-19Z) period of around 5.8 m/s. I'm using the 2 hour average because there's huge varability in the speed between consecutive images (<0.1 m/s to 40 m/s for some pixels). Also a lot of variability from pixel to pixel.
    * Average wind direction from optical flow over 2 hour period is 127 degrees. Which appears to be WSW according to: https://stackoverflow.com/questions/41824305/what-is-the-reference-point-for-measuring-angles-in-opencv. Couldn't find any actual documentation on the reference point for direction.

### June 29
- Clouds/CV meeting
- CLeaned up most code/wrote as functions
- Finished optical flow results. Ended up averaging the motions per pixel over the length of the video. Values range from 3.5 m/s to 8.3 m/s (average of 5.85 m/s) in the 5 by 5 km region over the site. At the pixel directly over the site the average speed is 5.8 m/s. 

### June 30
- Working on deliverables

## Week 10
### August 2
- Finished draft of the paper over the weekend
- Finished final powerpoint for Learning Off the Lawn presentation
- Uploaded final powerpoint and a recording of the presentation
- Wrote the 3 required abstracts (paper, general audience, presentation)
- To do:
    * More paper edits
    * Format references
    * Write the blog for Sage site
    * Update ECR meta folder
    * Clean up radar code and get it into ECR
    * Final presentation & peer review paper

### August 3/4
- Wrote/edited Sage blog
- Edited all 3 abstracts which are done along with the powerpoint
- Post internship survey on Workday
- Post internship survey on on WDTS portal
- Finished ecr-meta files for the satellite plugin
- Cleaned up both versions of the radar code and the optical flow code
- Attended and presented at Learning Off the Lawn Day 1
- To do:
    * Format references
    * Post Sage blog
    * Finish paper edits
    * Peer review

