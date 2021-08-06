This plugin can predict the net solar irradiance with 92.5% accuracy
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

The model architecture is 
Loss = "mean absolute error"
learning rate = .001
optimizer  = Adam 

Input(11,) 
Dense(64) - activation = "relu"
Dense(64) - activation = "relu"
Dense(270)- activation = "relu"
Dense(1)




This is the code- it contains all relevant information when it comes to model architecture
import tensorflow as tf
import seaborn as sns
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.layers.experimental import preprocessing
import matplotlib.pyplot as plt
import numpy as np
from sklearn import linear_model
from sklearn import svm
from sklearn.metrics import mean_squared_error
from sklearn.metrics import explained_variance_score
import pandas as pd
import numpy as np


#del df['HourlyVisibility']
#del df['HourlyWindDirection']
#del df['HourlyWindSpeed']
#del df['DATE']
#del df['alistindex']
#del df['LCLPressure']
dataset = df27.copy()
train_dataset = dataset.sample(frac=0.8, random_state=0)
test_dataset = dataset.drop(train_dataset.index)
train_features = train_dataset.copy().astype("float64")
test_features = test_dataset.copy().astype("float64")

train_labels = train_features.pop('NET').astype("float64")
test_labels = test_features.pop('NET').astype("float64")
train_dataset.describe().transpose()[['mean', 'std']]

def plot_loss(history):
  plt.plot(history.history['loss'], label='loss')
  plt.plot(history.history['val_loss'], label='val_loss')
  plt.ylim([0, 1])
  plt.xlabel('Epoch')
  plt.ylabel('Error')
  plt.legend()
  plt.grid(True)
normalizer = preprocessing.Normalization(axis=-1)
normalizer.adapt(np.array(train_features).astype("float64"))
def build_and_compile_model(norm):
  model = keras.Sequential([
      norm,
      layers.Dense(64, activation='relu'),
      layers.Dense(64, activation='relu'),
      layers.Dense(270, activation='relu'),
      layers.Dense(1)
  ])

  model.compile(loss='mean_absolute_error',
                optimizer=tf.keras.optimizers.Adam(0.001))
  return model
dnn_model = build_and_compile_model(normalizer)
dnn_model.summary()
history = dnn_model.fit(
    train_features, train_labels,
    validation_split=0.2,
    verbose=0, epochs=1000)
plot_loss(history)
test_predictions = dnn_model.predict(test_features).flatten()

a = plt.axes(aspect='equal')
plt.scatter(test_labels, test_predictions)
plt.xlabel('True Values [MPG]')
plt.ylabel('Predictions [MPG]')
lims = [22, 30]
plt.xlim(lims)
plt.ylim(lims)
_ = plt.plot(lims, lims)
accneigh = explained_variance_score(test_labels, test_predictions)
msegpc = mean_squared_error(test_labels, test_predictions, squared=False)
print("ACC: " + str(accneigh))
print("MSE: " + str(msegpc))
