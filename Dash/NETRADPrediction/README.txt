HELLO
This plugin can predict the net solar irradiance with 94.8% accuracy
This model takes 11 inputs, but only 8 different values
The first is Air Temperature
The second and third are Wind Direction
The third is Sigma Direction
The fourth is relative humidity
the fifth is dew point
the sixth is air temperature
the seventh and eighth are wind direction
the ninth is sigma direction
the tenth is air pressure
the eleventh is precipitation
The twelfth is a 252x336 temperature array

Here's some information about the model
Keras Functional
Epochs to train =1000
Validation split =.2
Learning rate = default
Optimier = RMSprop
Loss= "mean absolute error"
metric  = "mean absolute error"

Architecture

Input layer A (11)                           Input layer B(252,336,)
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
               Dense(32, activation='relu'),
                Dense(64, activation='relu'),
              output layer = Dense(1)
