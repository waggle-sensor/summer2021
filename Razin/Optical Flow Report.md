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
![mov](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK%20algo%20validation%20trimmed.mov)



## Reflectivity Data
I began by using the same .avi videos as those I used for the dense optical flow algorithm. However, I quickly realized the plots in these videos were not well-suited to this algorithm (Fig. 14-15). In particular, all the starting point for the flow began on the plot boundaries, title, labels, or legend. This likely has to do with the `cv.goodFeaturesToTrack()` method, which decides the points to track. So, I manually cropped the five images then re-ran the algorithm (Fig. 16-17). This yielded better results, as the points that were being tracked appeared to be register movement. However, the points were not in our region of interest, about 25 meters above the radar. So, I further cropped the images of the radar data (Fig. 18), to little improvement. I did start to see substantial improvement in tracking after adding a non-null `mask` parameter, which [specifies an optional region of interest](https://docs.opencv.org/3.4/dd/d1a/group__imgproc__feature.html#ga1d6bb77486c8f92d79c8793ad995d541) for corner detection, to the aforementioned `cv.goodFeaturesToTrack()` method. Specifically, I changed the default:

`p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)` 

to:

`p0 = cv.goodFeaturesToTrack(cv.cvtColor(old_frame[start:end], cv.COLOR_BGR2GRAY), mask = cv.cvtColor(old_frame[start:end], cv.COLOR_BGR2GRAY), **feature_params)`,

where `start:end` specifies the range of height pixels where tracking corners are identified. Results for several LK algorthim runs with non-null masks are shown (Fig. 19-26), as are gifs of the most promising ones (Fig. 27-30). I toggled parameters, such as `qualityLevel` (Fig. 21-22), for the [Shi-Tomasi corner detection](https://docs.opencv.org/3.4/d8/dd8/tutorial_good_features_to_track.html), as well.


 

|  |  |
|---|---|
|![14](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_cropped_output_opticalhsv_0b.png) ***Figure 14.** Preliminary attempt at Lucas-Kanade (LK) algorithm with reflectivity data.* | ![15](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_cropped_output_opticalhsv_0.png) ***Figure 15.** Preliminary attempt at LK algorithm with reflectivity data zoomed into the region less than 25 meters above the radar, our area of interest.*|
|![16](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_uncropped_cropped_output_opticalhsv_0.png) ***Figure 16.** First run at LK algorithm on cropped images.*|![17](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_cropped_output_opticalhsv.png) ***Figure 17.** First run at LK algorithm on cropped, zoomed-in images.*|
|![18](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_2.png)  ***Figure 18.** Run at LK algorithm, recropped. Mask = None.* | ![19](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_0_100.png) ***Figure 19.** Mask = 0:100.*|
|![20](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_100_200.png) ***Figure 20.** Mask = 100:200*| ![21](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_100_300.png) ***Figure 21.** Mask = 100:300.*|
|![22](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_100_300_2.png) ***Figure 22.** Mask = 100:300; qualityLevel = 0.4 instead of default, 0.2.* |![23](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_200_300.png) ***Figure 23.** Mask = 200:300.*|
|![24](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_300_400.png))***Figure 24.** Mask = 300:400*| ![25](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_300_420.png) ***Figure 25.** Mask = 300:420.*|
|![26](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_output_opticalhsv_0_420.png)***Figure 26.** Mask = 0:420, the entire height of the images. This mask gives the same flow as shown in Fig. 18, which doesn't have a mask.*|![27](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_100_200.gif)***Figure 27.** Mask = 100:200.*|
|![28](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_100_300.gif) ***Figure 29.** Mask = 100:300*|![29](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_300_400.gif) ***Figure 29.** Mask = 300:400*|
|![30](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_tripple_cropped_300_420.gif)***Figure 30.** Mask = 300:420*||


|  |  |
|---|---|
|![31](https://drive.google.com/uc?export=view&id=1FPanTRr5pfqJtpEdwPconr4VG1dhdvdd)***Figure 30.** Mask = 200:550, ref above 25*||



# Questions to Investigate
 - Will there be any practical difference in how we process LiDAR data compared to these RADAR data?
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
