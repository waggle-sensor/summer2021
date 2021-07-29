HELLO
This plugin can predict the LCL Pressure with 99.8% accuracy
The three parameters, in order, are Relative Humidity, Sea Level Pressure, and Wet Bulb Temperature
Here's some information about the model
Keras Sequential
Epochs to train =100
Validation split =.2
Learning rate = .001
Optimier = Adam
Loss= "mean absolute error"

Architecture

Input layer(3)
Dense(64, activation='relu'),
Dense(64, activation='relu'),
Dense(270, activation='relu'),
output layer = Dense(1)
