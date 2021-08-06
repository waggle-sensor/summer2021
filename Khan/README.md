# Measuring Visual Disorder

#### Author: Samaah Khan
#### Collaborators: Dr. Nicola Ferrier

## Description / Abstract for General Audience
The broken window theory suggests that disordered environments 
are correlated with rule-breaking and social disorder. To aid 
social scientists in studying this hypothesis, I created software 
that can measure visual disorder in urban environments. Using computer 
vision techniques, I extracted features (mean and standard deviation
of hue, saturation, and value, entropy, edge density, and straight 
edge density) from images which I then used to create a random forest model 
that can predict the disorder rating of an image with a 71 percent
accuracy. This software was then deployed on geographically distributed
Sage nodes with cameras used to capture images that are un through the 
machine learning model to predict the disorder of the area captured. 
My results revealed that mean saturation and mean hue were the most important 
low - level features in determining what makes an urban environment 
disorderly while entropy and standard deviation of value were the least 
important. Most features were found to have little correlation with 
each other. 

For more information on project visit https://sagecontinuum.org/science/measuring-visual-disorder/ 

## Package Requirements
Following are the PyPi Packages that are required to run this project:
* opencv-contrib-python == 4.5.2.54
* opencv-python == 4.5.2.52  
* scikit learn == 0.23.1
* pandas == 1.2.5
* numpy == 1.20.3

## Executing Program
To run the random forest classifier, run the `main.py` file. Currently main file runs random forest.
If you wish to run gaussian mixture model, change `MODEL_TYPE` variable to equal `gaussian_mixture_model`

 



