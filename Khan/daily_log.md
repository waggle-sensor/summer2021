# Daily Log #

-----

## Week 1 ##
### 6/1/2021 ###
* Attended new student orientation
* Meeting with mentor
* Set up Argonne email
* Created and set up slack account

### 6/2/2021 ###
* Read through directions for new students on github
* Followed direction to connect to lcrc
    * Debugged issues with connecting to lcrc
* Attended CELS Coffee Chat
    
### 6/3/2021 ### 
* Continued to debug issues with connecting to lcrc
* Read half of research paper "The Nature-Disorder Paradox: A Perceptual Study on How
                                Nature Is Disorderly Yet Aesthetically Preferred"
* Familarized myself with the project  

### 6/4/2021
* Meeting with mentor about project details
* Finished most training assignments 
* Continued debugging issues with connecting to lcrc
* Completed mandatory pre-survey

----

## Week 2 ##
### 6/7/2021 ###
* Watched Youtube tutorials on OpenCV
    * Downloaded openCV library and set up local enviroment
    * learned how to read and write to files on openCV
    * learned how to detect objects based on hue, saturation, value of objects
* Cloned github project onto local enviroment, created daily_log, and README
* Uploaded sample images from google (one that seemed ordered and the other which seemed disordered)
  onto repository
* Created a method that detects the hue, saturation, and value of the images
* Read second half of research paper "The Nature-Disorder Paradox: A Perceptual Study on How
                                      Nature Is Disorderly Yet Aesthetically Preferred"
  
### 6/8/2021 ###
* Started Udacity course on Computer Vision
  * Watched introduction lectures
* Computed mean hsv of image
* Used Canny Edge Detection to detect the edges of given images
    * TODO: use this to detect density of edges
* Read research paper "The Nature-Disorder Paradox: A Perceptual Study on How Nature is
                        Disorderly Yet Aesthetically Preferred"
    * Found out that I should calculate mean and SD of hsv
* Finished Last 2 training assignments
* TODO:
    * Find Standard Deviations of hsv
    * Add Track bars
    
### 6/9/2021 ### 
* Attended seminar on "How and When Do I Go To Graduate School" (9- 10am)
* Had meeting with Writing coach                                (10:30 - 11:30 am)
* Continued Watching Udacity videos on Computer Vision
    * "Images as Functions" lecture
* Updated Payroll information on Workday
* Found standard deviations of hsv 
* Wrote test cases
    * Computing mean of hsv
    * Computing Standard Deviation of hsv
      * Still need to work on finding best way to test the standard deviation function
    
### 6/10/2021 ###
* Attended student connect meeting
* Wrote more test cases for standard deviation
* Watched Udacity video on canny edge detection
* Debugged logging into lcrc and was finally able to correcty log into lcrc through PuTTY :)
    * On Windows I should be using PuTTY instead of Command Prompt
      to log into lcrc
* Wrote method on finding edge density
    * Wrote test cases for finding edge density to make sure I calculated it correctly
    * Failed one test case where both images had very high edge densities
    * TODO:
        * Need to debug edge density calculations
        * Also need to contact Nicola to make sure I am understanding edge density 
          correctly and my thought process is correct about that for clarification
    
### 6/11/2021 ###
* Prepare presentation about project for Monday
* Attend meeting with team
* Research machine learning techniques I can use, and watch 
 videos introducing machine learning so I can start preparing for the second part of the project
  after detecting features
* Corrected issues with mean hue so that caluclations took into account that hue is in a circle 
* TODO:
    * Look back at how I did canny edge detection and make sure I understand it and the threshholds
    
----

## Week 3 ##
    
###  6/14/2021 ###
* Practiced Presentation
* Attended meeting where I learned about other projects and gave presentation on my project
* Understand the canny edge detection threshold thing and understand canny edge detection
* Update presentation for what I understand so far
* Researched and calculated Entropy. Need to research more on finding the best way to do so.
    * There should be an easy function call for it, cant find it?
* GOAL for end of week:
    * Be completely done computing features
    * Have a good grasp on how to use Support Vector Machines
    
### 6/15/2021 ###
* Attended meeting with CV team
* Used Hough Line Transform to detect straight edges and compute straight edge density.
    * Am running into issues about finding the best threshold values to use in order to 
      detect all the straight lines
* Wrote a couple of test cases for straight edge density computation
* Wrote test cases for entropy -> Need to debug find_entropy function

### 6/16/2021 ###
* Attended seminar on "Overcoming Imposter Syndrome"
* Accurately calculated entropy that passed test cases
* Computed vertical reflectional symmetry of image
* Wrote test cases for vertical reflectional symmetry of image
* Strengthened Hough Line Transform by using bilateralFilter which blurs the image while keeping
    edges sharp. Was able to more accurately compute the straight edge density this way
  
### 6/17/2021 ###
* Attended meeting with CV team
* Attended student connect meeting
* Instead of using Hough, changed my code to use opencv's Line Segment Detector in order to
    compute straight edge density because this more accurately finds straight edges and 
    runs much faster.
* Computed total length of all line segments combined in order to compute the straight edge density
* Watched videos on vector support machines

### 6/18/2021 ###
* Watched videos on machine learning and different machinen learning models
* I am a little confused on what machine learning algorithm to use and how to go about the second part of the project

---

## Week 4 ##

### 6/21/2021 ###
* Attended zoom meeting where I learned about other projects 
* Prepared slides for mid - point progress presentation on parts of the project that I have 
  already completed
* Researched and understood the math behind canny edge detection through Udacity computer vision videos
* Wrote additional test cases 
* Need to get started on second part of project, came up with a couple of questions to ask in tomorrows meeting
  about that
  
### 6/22/2021 ###
* Attended meeting with computer vision team
* Researched random forests machine learning model to use in project
* Fixed an issue with straight line detection

### 6/23/2021 ###
* Attended zoom meeting on "Connecting to a Career through Linkedln"
* Watched a couple more videos on random forests and decision trees.
* Wrote a simple program using random forests involving classifying different
  types of flowers in order to get a better grasp on random forests for project.
* Recieved images for data in project.

### 6/24/2021 ###
* Attended meeting with computer vision team 
* Attended student connect meeting           
* Attended Seans meeting on plugins
* Wrote random forest model using data given
    * Need to confirm if I am using the data correctly
    
### 6/25/2021 ###
* Finish Random Forest Tree Classifier
* Accuracy low, so researched on ways to improve accuracy of model
* Ask if I should be using computed features already in data given
  or if I should use features I computed
* TODO:
  * Need to use this to find out which faetures matter the most 
        towards visual disorder and which features matter the least
  * Still need to find out ways to improve accuracy for model
    
--- 
## Week 5 ##

### 6/28/2021 ###
* Need to ask: there were some images that were not urban, do I remove them from dataset
* Used images given to compute features and create own dataframe with my computed features
    and used this in random forest classifier --> still need to clarify if I am using my computed features
    or the ones given
* Spent most of the time debugging why some images were running into errors when trying to compute features
  I am still working on fixing some of those errors so that I can use my computed features in random forest 
* Need to work on fixing accuracy of random forest, will check what accuracy is after using my own features too.
  * Should check that training images have some from each classifications
    
### 6/29/2021 ###
* Attended meeting with CV team
* created new dataframe to input features
* Replaced classifications to 3 different groups instead of 7, so I can start off small
* Tried to compute features of all images --> was taking a long time
  Therefore in the meanwhile I prepared more slides for the next presentation.
* Ran into errors when computing straight edge density for some of the training images
  Working on debugging errors
* Ran into errors with some files not existing as images that I can use to compute features. 
* After computing all features plan on normalizing the data, then computing features again
so that they are normalized.

### 6/30/2021 ###
* Still running into bugs when creating dataframe with computed features
    * standard deviation of hue, saturation, and value show up as 0 on saved excel file 
      with data even though when testing and printing out the standard deviation, it prints not 0.
      All other features are put into the dataframe correctly.
    * After lots of debugging found out the issue was that when I call the function to compute mean hsv
      I change the values of hsv image which is then used in function for computing standard deviation
      of image as well
* Debugged the issue about when I tried to save all features into excel file again ran into a permission denied issue
* Changed the way that I saving my dataframe into excel file so that it doesnt all save at once at the very
  end but instead saves every couple of images so that if I run into an error again I do not need to start all over
* Mean hue is also showing up as different 
    * debugged it by using cv2.imread instead of io.imread
* Debugged the issue that rows with files that did not have images correlated with them were not being
  deleted from dataframe
* Was able to achieve a 63 percent accuracy, I am still working on getting accuracy higher
*