HELLO
This plugin can predict the LCL Temperature with 97.8% accuracy
This model takes two inputs
The first has three measurement. The three measurements, in order, are Relative Humidity, Sea Level Pressure, and Wet Bulb Temperature
The second is a 252x336 temperature array, trained on data from a MOBOTIX camera.



Here's some information about the model
Keras Sequential
Epochs to train =1000
Validation split =.2
Learning rate = default
Optimier = RMSprop
Loss= "mean squared error"

Architecture

Input layer A (3)                           Input layer B(252,336,)
Dense(64, activation='relu'),               Dense(64, activation='relu'),
Dense(32, activation='relu'),               Dense(32, activation='relu'),
Dense(4, activation='relu'),                Dense(4, activation='relu'),
Flatten()                                   Flatten
     |                                           |
     |                                           |
     |                                           |
    ||---------------->Concat<--------------------||

              Dense(64, activation='relu'),
              Dense(64, activation='relu'),
              Dense(32, activation='relu'),
              output layer = Dense(1)
