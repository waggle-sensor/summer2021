# Overview
Below are images of optical flow generated from RADAR data (i.e., reflectivity, differential reflectivity, and mean doppler velocity data) collected by the [CACTI campaign](https://www.arm.gov/research/campaigns/amf2018cacti) in Cordoba, Argentina. These optical flow images were generated using [OpenCV's](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html) Dense Optical Flow algorithm and Lucas-Kanade Method algorithm. Gifs of the original RADAR data are also included.

# Dense Optical Flow 
Dense optical flow fields are created using the `cv.calcOpticalFlowFarneback()` method. They compute the optical flow for all points in the frame. [This article](https://www.geeksforgeeks.org/python-opencv-dense-optical-flow/) explains the implementation well.

## Reflectivity Data

|  |  |
|---|---|
| ![1](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_uncropped_animation.gif) ***Figure 1.** RADAR reflectivity data.* |  ![2](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_uncropped_opticalhsv.png) ***Figure 2.** Dense optical flow from the five images in the Fig. 1 gif.* |
|![3](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/reflectivity_animation.gif) ***Figure 3.** Same relectivity data shown above (Fig. 1), just zoomed into the region less than 25 meters above the radar, our area of interest.* | ![4](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_cropped_opticalhsv.png) ***Figure 4.** Dense optical flow from the five images in the Fig. 3 gif.* |
||![5](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_cropped_two_opticalhsv.png) ***Figure 5.** Dense optical flow from just the first two images in the Fig. 3 gif.* |



## Differential Reflectivity Data

|  |  |
|---|---|
| ![6](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/diff_ref_uncropped_animation.gif) ***Figure 6.** RADAR differential reflectivity data.*| ![7](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/diff_ref_uncropped_output_opticalhsv.png) ***Figure 7.** Dense optical flow from the five images in the Fig. 6 gif.*|
|![8](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/diff_reflectivity_animation.gif) ***Figure 8.** Same differential relectivity data shown above (Fig. 6), just zoomed into the region less than 25 meters above the radar, our area of interest.*| ![9](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/diff_ref_cropped_output_opticalhsv.png) ***Figure 9.** Dense optical flow from the five images in the Fig. 8 gif.*|


## Mean Doppler Velocity Data

|  |  |
|---|---|
|![10](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/vel__uncropped_animation.gif) ***Figure 10.** RADAR velocity data.*| ![11](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/vel_uncropped_output_opticalhsv.png) ***Figure 11.** Dense optical flow from the five images in the Fig. 10 gif.*|
| ![12](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/vel_animation.gif) ***Figure 12.** Same velocity data shown above (Fig. 10), just zoomed into the region less than 25 meters above the radar, our area of interest.*| ![13](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/vel_cropped_output_opticalhsv.png) ***Figure 13.** Dense optical flow from the five images in the Fig. 12 gif.*|


## Observations
- Fig. 4 appears to have less noise than Fig. 5 (?), suggesting the inclusion of the three other relfectivity data images produced a better model.
- Fig. 4 and 9 appear relatively similar, suggesting little difference in the optical flow diagnositcs extractable from reflectivity and differential reflectivity data, respectively.
- Fig. 11 and 13 appear very noisy, suggesting MDV may not be optimal for diagnosing optical flow.


# Lucas-Kanade Optical Flow

LK optical flow fields are created using the `cv.calcOpticalFlowPyrLK()` method. This algorithm is meant for sparser feature sets.
I used a short clip of my pen moving across a white background to do some basic validation of my slightly modified LK algorithm:
![movie](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK%20algo%20validation%20trimmed.mov)



## Reflectivity Data
I began by using the same .avi video as those I used for the dense optical flow algorithm. However, I quickly realized these plots were not well-suited to this algorithm (Fig. 14-15). In particular, all the starting point for the flow began on the plot boundaries, title, labels, or legend. This likely has to do with the `cv.goodFeaturesToTrack()` method, which decides the points to track. So, I manually cropped the five images then ran the algorithm (Fig. 16-17). This yielded better results, as the points that were being tracked appeared to be register movement. However, they points were not in our region of interest, about 25 meters above the radar. So, I further cropped the images of the radar data (Fig. 18).


Changed:
`p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)` (Figure 18)

To:

`p0 = cv.goodFeaturesToTrack(cv.cvtColor(old_frame[100:200], cv.COLOR_BGR2GRAY), mask = cv.cvtColor(old_frame[100:200], cv.COLOR_BGR2GRAY), **feature_params)` (Figure 19)

To:

`p0 = cv.goodFeaturesToTrack(cv.cvtColor(old_frame[0:200], cv.COLOR_BGR2GRAY), mask = cv.cvtColor(old_frame[0:200], cv.COLOR_BGR2GRAY), **feature_params)` (Figure 20)

To: 
`p0 = cv.goodFeaturesToTrack(cv.cvtColor(old_frame[0:420], cv.COLOR_BGR2GRAY), mask = cv.cvtColor(old_frame[0:420], cv.COLOR_BGR2GRAY), **feature_params)` (Figure 21, back where we started with unfocused `goodFeaturesToTrack()` function)

|  |  |
|---|---|
|![14](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_cropped_output_opticalhsv_0b.png) ***Figure 14.** First attempt at Lucas-Kanade (LK) algorithm with reflectivity data.* | ![15](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_cropped_output_opticalhsv_0.png) ***Figure 15.** First attempt at LK algorithm with reflectivity data zoomed into the region less than 25 meters above the radar, our area of interest.*|

|![16](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_cropped_output_opticalhsv.png) ***Figure 16.** Cropped, zoomed-in first run at LK algorithm.*|![17](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_uncropped_cropped_output_opticalhsv_0.png) ***Figure 17.** Uncropped, zoomed-in first run at LK algorithm.*|

|![18](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_2.png)  ***Figure 18.*** |![19](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_3.png)  ***Figure 19.** Focusing `goodFeaturesToTrack()`.*|

|![20](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_4.png)  ***Figure 20.***| ![21](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_5.png)  ***Figure 21.***|

|||



# Questions to Investigate
 - Will there be any practical difference in how we process LiDAR data compared to this RADAR data?
 - What's the significance (if any) of the particular colors in these dense optical flow images? How should we interpret these colors? OpenCV gives little information about this, and their example is much more simple with just three distinct color regions.
 - What is the most useful measurement/data type for diagnosing optical flow: reflectivity data, differential reflectivity data, or velocity data?
    - What's the differnce between reflectivity data and differential reflectivity data? "Differential Reflectivity is the logarithm ratio of the horizontally polarized reflectivity to the vertically polarized reflectivity."
 - How are these data (or rather, the images we generate from them) both well-suited (+) and ill-suited (-) for diagnosing optical flow?
    - +: there's a finite range of colors and each color has a pre-determined meaning/value
    - +: based on the above, there won't be issues of brightness in these shifting images 
    - +: scans are collected with relatively high frequency, making them easier to stitch together for optical flow
    - -: by definition of optical flow, they are proxies to the actual physical movement of aerosol particles
 - What are the pros and cons of each of OpenCV's two optical flow methods, particularly in this use case?
    - the Lucas-Kanade method may be less suited for this application because we're not really tracking a single object but instead shifts in color (?).
 - On Optimizations
    - How do we reduce noise? In the case of the dense optical flow images, how do we reduce the number of colors used and their spread?
    - How much should we zoom into the area of interest in the images?
