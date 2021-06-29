import IPython.display as ipd
import numpy as np
import pandas as pd
import librosa
import librosa.display
import matplotlib

matplotlib.use('agg')
import matplotlib.pyplot as plt
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
from sklearn.model_selection import train_test_split

import types
import functools
from feature_extraction import extract_features_mfcc, extract_features_mel, extract_features_fourier_tempogram, extract_features_tempogram, extract_features_chroma


#### Dependencies ####

def copy_func(f):
    """Based on http://stackoverflow.com/a/6528148/190597 (Glenn Maynard)"""
    g = types.FunctionType(f.__code__, f.__globals__, name=f.__name__,
                           argdefs=f.__defaults__,
                           closure=f.__closure__)
    g = functools.update_wrapper(g, f)
    g.__kwdefaults__ = f.__kwdefaults__
    return g


# def extract_features_mfcc(file_name):
#     try:
#         audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
#         mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
#         mfccsscaled = np.mean(mfccs.T, axis=0)
#     except Exception as e:
#         print("Error encountered while parsing file: ", e)
#         return None
#     return mfccsscaled
#
#
# def extract_features_tempogram(file_name):
#     audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
#     hop_length = 512
#     oenv = librosa.onset.onset_strength(y=audio, sr=sample_rate, hop_length=hop_length)
#     tempograms = librosa.feature.tempogram(onset_envelope=oenv, sr=sample_rate, hop_length=hop_length)
#     tempogram = np.mean(tempograms.T, axis=0)
#     return tempogram
#
#
# def extract_features_fourier_tempogram(file_name):
#     audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
#     hop_length = 512
#     oenv = librosa.onset.onset_strength(y=audio, sr=sample_rate, hop_length=hop_length)
#     fourier_tempograms = librosa.feature.fourier_tempogram(onset_envelope=oenv, sr=sample_rate,
#                                                            hop_length=hop_length)
#     fourier_tempogram = np.mean(fourier_tempograms.T, axis=0)
#
#     return fourier_tempogram
#
#
# def extract_features_chroma(file_name):
#     try:
#         audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
#         chroma_l = librosa.feature.chroma_stft(y=audio, sr=sample_rate)
#         chromascaled = np.mean(chroma_l.T, axis=0)
#     except Exception as e:
#         print("Error encountered while parsing file: ", e)
#         return None
#     return chromascaled
#
#
# def extract_features_mel(file_name):
#     try:
#         audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
#         mel_l = librosa.feature.melspectrogram(audio, sr=sample_rate)
#         mel = np.mean(mel_l.T, axis=0)
#     except Exception as e:
#         print("Error encountered while parsing file: ", e)
#         return None
#     return mel


def feature_extraction(extraction_method):
    if not (extraction_method == "extract_features_mfcc" or extraction_method == "extract_features_mel" or extraction_method == "extract_features_fourier_tempogram"):
        raise Exception("Please select a valid method")

    if extraction_method == "extract_features_mfcc":
        extraction = copy_func(extract_features_mfcc)
    if extraction_method == "extract_features_mel":
        extraction = copy_func(extract_features_mel)
    if extraction_method == "extract_features_fourier_tempogram":
        extraction = copy_func(extract_features_fourier_tempogram)

    features = []
    # Set the path to the full BirdSound dataset
    full_dataset_path = 'test_audio1'
    metadata = pd.read_csv('test1.csv')
    for index, row in metadata.iterrows():
        file_name = os.path.join(os.path.abspath(full_dataset_path), str(row['primary_label']) + '/',
                                 str(row['filename']))
        class_label = row["primary_label"]
        data = extraction(file_name)
        features.append([data, class_label])
        print('parsing' + file_name + '.')
    return features


def get_model(config, output_size):
    m = Sequential()
    if config == "extract_features_mfcc":
        # Construct model
        m.add(Dense(256, input_shape=(40,)))
    if config == "extract_features_mel":
        # Construct model
        m.add(Dense(256, input_shape=(128,)))
    if config == "extract_features_fourier_tempogram":
        m.add(Dense(256, input_shape=(193,)))
    m.add(Activation('relu'))
    m.add(Dropout(0.5))
    m.add(Dense(256))
    m.add(Activation('relu'))
    m.add(Dropout(0.5))
    m.add(Dense(output_size))
    m.add(Activation('softmax'))
    m.compile(loss='categorical_crossentropy', metrics=['accuracy'], optimizer='adam')
    return m


if __name__ == '__main__':
    input_features = feature_extraction(extraction_method="extract_features_mfcc")
    # Convert into a Panda dataframe
    features_df = pd.DataFrame(input_features, columns=['feature', 'class_label'])

    # Convert features and corresponding classification labels into numpy arrays
    X = np.asarray(features_df.feature.tolist())
    y = np.asarray(features_df.class_label.tolist())

    # Encode the classification labels
    le = LabelEncoder()
    yy = to_categorical(le.fit_transform(y))

    # split the dataset
    x_train, x_test, y_train, y_test = train_test_split(X, yy, test_size=0.2, random_state=42)

    model = get_model("extract_features_mfcc", output_size=yy.shape[1])

    # Compile the model
    num_epochs = 100
    num_batch_size = 32
    start = datetime.now()
    model.fit(x_train, y_train, batch_size=num_batch_size, epochs=num_epochs, validation_data=(x_test, y_test),
              verbose=1)
    duration = datetime.now() - start
    print("Training completed in time: ", duration)

    score = model.evaluate(x_train, y_train, verbose=0)
    print('train accuracy: {}'.format(score))
    # experiment.log_metric("train_acc", score)

    score = model.evaluate(x_test, y_test, verbose=0)
    print('test accuracy: {}'.format(score))
    # experiment.log_metric("val_acc", score)
