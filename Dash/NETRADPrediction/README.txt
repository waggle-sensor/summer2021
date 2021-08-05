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
Here's the code

from keras.layers import Activation, Dense, Input
from keras.layers import concatenate
import tensorflow as tf
from tensorflow import keras
inputA = keras.Input(shape=(12, ))
inputB = keras.Input(shape=(252,336,))
x = keras.layers.Dense(64, activation="relu")(inputA)
x = keras.layers.Dense(32, activation="relu")(x)
x = keras.layers.Dense(4, activation="relu")(x)
x= keras.layers.Flatten()(x)
x = keras.Model(inputs=inputA, outputs=x)
y = keras.layers.Dense(64, activation="relu")(inputB)
y = keras.layers.Dense(32, activation="relu")(y)
y = keras.layers.Dense(4, activation="relu")(y)
y = keras.layers.Flatten()(y)
y = keras.Model(inputs=inputB, outputs=y)
combined = concatenate([x.output, y.output])
z =  keras.layers.Dense(64, activation="relu")(combined)
z =  keras.layers.Dense(64, activation="relu")(z)
z = keras.layers.Dense(32, activation="relu")(z)
z = keras.layers.Dense(32, activation="relu")(z)
z = keras.layers.Dense(64, activation="relu")(z)
z = keras.layers.Dense(1)(z)
model = keras.Model(inputs=[x.input, y.input], outputs=z)
model.summary()
model.compile(
    loss= 'mean_absolute_error',
    optimizer=keras.optimizers.rMSprop(),
    metrics=["mean_absolute_error"],
)
history = model.fit([np.array(X_train), np.array(thermalimagestrain)],np.array(y_train).astype("float64"), batch_size=64, epochs=1000, validation_split=0.2, verbose=0)
import matplotlib.pyplot as plt
from sklearn.metrics import explained_variance_score
from sklearn.metrics import mean_squared_error
test_labels= list(y_test)
test_predictions = model.predict([np.array(X_test).astype("float64"), np.array(thermalimagestest)]).flatten()
a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values')
plt.ylabel('Predictions')
lims = [250, 500]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims, lims)
accneigh = explained_variance_score(test_labels, test_predictions)
msegpc = mean_squared_error(test_labels, test_predictions, squared=False)
print("ACC: " + str(accneigh))
print("MSE: " + str(msegpc))
