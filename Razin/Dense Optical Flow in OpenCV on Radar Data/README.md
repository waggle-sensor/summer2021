(currently updating this file)

# Dense Optical Flow 
Below are images generated using [OpenCV's Dense Optical Flow algorithm](https://docs.opencv.org/3.4/d4/dee/tutorial_optical_flow.html).

## Reflectivity Data

Here's what the RADAR reflectivity data looks like:

![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_uncropped_animation.gif)
*Figure 1.*

Here's the dense optical flow from the five images in that .GIF:

![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_uncropped_opticalhsv.png)
*Figure 2.*

Here's the same relectivity data shown above, just zoomed into the bottom left region, our area of interest: 

![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/reflectivity_animation.gif)
*Figure 3.*

Here's the dense optical flow from the five images in that .GIF:

![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_cropped_opticalhsv.png)
*Figure 4.*

Here's the dense optical flow from just the first two images in that .GIF:

![Fig. 5](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_cropped_two_opticalhsv.png)
*Figure 5.*

## Differential Reflectivity Data


# Questions to Investigate
 - Will there be any practical difference in how we process LiDAR data compared to this RADAR data?
 - What's the significance (if any) of the particular colors in these dense optical flow images? How should we interpret these colors? OpenCV gives little information about this, and their example is much more simple.
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
