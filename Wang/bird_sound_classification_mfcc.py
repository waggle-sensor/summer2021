# # Import Comet and create experiment
# from comet_ml import Experiment
#
# # Comet variables
# API_KEY = "<HIDDEN>"
# PROJECT = "urbansound8k"
# WORKSPACE = "demo"
#
# experiment = Experiment(api_key=API_KEY,
#                         project_name=PROJECT, workspace=WORKSPACE)

#### Dependencies ####
import IPython.display as ipd
import numpy as np
import pandas as pd
import librosa
import librosa.display
import matplotlib

matplotlib.use('agg')
import matplotlib.pyplot as plt
# import struct
from scipy.io import wavfile as wav
import os
from datetime import datetime

from sklearn import metrics
from sklearn.preprocessing import LabelEncoder
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.keras.layers import Convolution2D, Conv2D, MaxPooling2D, GlobalAveragePooling2D
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.callbacks import ModelCheckpoint
import np_utils

#### Dependencies ####

def extract_features(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccsscaled = np.mean(mfccs.T, axis=0)

    except Exception as e:
        print("Error encountered while parsing file: ", file_name)
        return None
    return mfccsscaled

def extract_features_chroma(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        chroma_l = librosa.feature.chroma_stft(y=audio, sr=sample_rate)
        chromascaled = np.mean(chroma_l.T, axis=0)

    except Exception as e:
        print("Error encountered while parsing file: ", file_name)
        return None
    return chromascaled

def extract_features_mel(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        mel_l = librosa.feature.melspectrogram(audio, sr=sample_rate)
        mel = np.mean(mel_l.T, axis=0)


    except Exception as e:
        print("Error encountered while parsing file: ", file_name)
        return None
    return mel

# Set the path to the full UrbanSound dataset
fulldatasetpath = 'test_audio'

metadata = pd.read_csv('data/test.csv')

features = []

for index, row in metadata.iterrows():
    file_name = os.path.join(os.path.abspath(fulldatasetpath), str(row["primary_label"]) + '/',
                             str(row["filename"]))
    # file_name = os.path.join(os.path.abspath(fulldatasetpath), 'fold' + str(row["fold"]) + '/',
    #                          str(row["file_name"]))

    class_label = row["primary_label"]
    data = extract_features(file_name)
    features.append([data, class_label])

# Convert into a Panda dataframe
featuresdf = pd.DataFrame(features, columns=['feature', 'class_label'])

# Convert features and corresponding classification labels into numpy arrays
X = np.asarray(featuresdf.feature.tolist())
y = np.asarray(featuresdf.class_label.tolist())

# Encode the classification labels
le = LabelEncoder()
yy = to_categorical(le.fit_transform(y))

# split the dataset
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(X, yy, test_size=0.2, random_state=42)

num_labels = yy.shape[1]
filter_size = 2

# Construct model
model = Sequential()

model.add(Dense(256, input_shape=(40,)))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(256))
model.add(Activation('relu'))
model.add(Dropout(0.5))

model.add(Dense(num_labels))
model.add(Activation('softmax'))

# Compile the model
model.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')

num_epochs = 100
num_batch_size = 32

start = datetime.now()

model.fit(x_train, y_train, batch_size=num_batch_size, epochs=num_epochs, validation_data=(x_test, y_test), verbose=1)

duration = datetime.now() - start

print("Training completed in time: ", duration)

score = model.evaluate(x_train, y_train, verbose=0)
print('train accuracy: {}'.format(score))
# experiment.log_metric("train_acc", score)

score = model.evaluate(x_test, y_test, verbose=0)
print('test accuracy: {}'.format(score))
# experiment.log_metric("val_acc", score)
