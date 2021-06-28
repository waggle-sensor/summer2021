(currently working on this file; should be done by 6/28)

![alt text](https://github.com/waggle-sensor/summer2021/blob/main/Razin/Dense%20Optical%20Flow%20in%20OpenCV%20on%20Radar%20Data/ref_cropped_opticalhsv.png)


### Questions to Investigate
 - Will there be any practical difference in how we process LiDAR data compared to this RADAR data?
 - What's the significance (if any) of the particular colors in these dense optical flow images?
 - What is the most useful measurement/data type for diagnosing optical flow: reflectivity data, differential reflectivity data, or velocity data?
    - What's the differnce between reflectivity data and differential reflectivity data?
 - How are these data (or rather, the images we generate from them) both well-suited (+) and ill-suited (-) for diagnosing optical flow?
    - +: there's a finite range of colors and each color has a pre-determined meaning/value
    - +: based on the above, there won't be issues of brightness in these shifting images 
    - +: scans are collected with relatively high frequency, making them easier to stitch together for optical flow
    - -: by definition of optical flow, they are proxies to the actual physical movement of aerosol particles
 - What are the pros and cons of each of OpenCV's two optical flow methods, particularly in this use case?
    - the Lucas-Kanade method may be less suited for this application because we're not really tracking a single object but instead shifts in color (?).
 - On Optimizations
    - How do we reduce noise? In the case of the dense optical flow images, ...
