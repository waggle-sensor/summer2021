# Dense Optical Flow 
Below are images of optical flow generated from RADAR data (i.e., reflectivity, differential reflectivity, and mean doppler velocity data) collected by the [CACTI campaign](https://www.arm.gov/research/campaigns/amf2018cacti) in Cordoba, Argentina. These optical flow images were generated using [OpenCV's Dense Optical Flow algorithm](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html). Gifs of the original RADAR data are also included.

## Reflectivity Data


Here's what the RADAR reflectivity data look like:
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_uncropped_animation.gif)
*Figure 1.*


Here's the dense optical flow from the five images in that gif:
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_uncropped_opticalhsv.png)
*Figure 2.*


Here're the same relectivity data shown above (Fig. 1), just zoomed into the bottom region, our area of interest: 
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/reflectivity_animation.gif)
*Figure 3.*


Here's the dense optical flow from the five images in the above gif (Fig. 3):
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_cropped_opticalhsv.png)
*Figure 4.*


Here's the dense optical flow from just the first two images in the gif (Fig. 3):
![Fig. 5](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_cropped_two_opticalhsv.png)
*Figure 5.*


## Differential Reflectivity Data


Here's what the RADAR differential reflectivity data look like:
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/diff_ref_uncropped_animation.gif)
*Figure 6.*


Here's the dense optical flow from the five images in the above gif (Fig. 6):
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/diff_ref_uncropped_output_opticalhsv.png)
*Figure 7.*


Here're the same differential relectivity data shown above (Fig. 6), just zoomed into the bottom region, our area of interest: 
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/diff_reflectivity_animation.gif)
*Figure 8.*


Here's the dense optical flow from the five images in the above gif (Fig. 8):
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/diff_ref_cropped_output_opticalhsv.png)
*Figure 9.*

## Mean Doppler Velocity Data


Here's what the RADAR velocity data look like:
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/vel__uncropped_animation.gif)
*Figure 10.*


Here's the dense optical flow from the five images in the above gif (Fig. 10):
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/vel_uncropped_output_opticalhsv.png)
*Figure 11.*


Here're the same velocity data shown above (Fig. 10), just zoomed into the bottom region, our area of interest: 
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/vel_animation.gif)
*Figure 12.*


Here's the dense optical flow from the five images in the above gif (Fig. 12):
![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/vel_cropped_output_opticalhsv.png)
*Figure 13.*


## Observations
- Fig. 4 appears to have less noise than Fig. 5 (?), suggesting the inclusion of the three other relfectivity data images produced a better model.
- Fig. 4 and 9 appear relatively similar, suggesting little difference in the optical flow diagnositcs extractable from reflectivity and differential reflectivity data, respectively.
- Fig. 11 and 13 appear very noisy, suggesting MDV may not be optimal for diagnosing optical flow.


# Lucas-Kanade Optical Flow

## Reflectivity Data
I began by using the same .avi video as those I used for the dense optical flow algorithm. However, I quickly realized these plots were not well-suited to this algorithm (Fig. 14-15). In particular, all the starting point for the flow began on the plot boundaries, title, labels, or legend. I'm not sure why this is. 

![alt](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_cropped_output_opticalhsv_0b.png)
*Figure 14.*

![alt](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_cropped_output_opticalhsv_0.png)
*Figure 15.*

![alt](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Lucas-Kanade%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/LK_vel_cropped_output_opticalhsv.png)
*Figure 16.*


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
