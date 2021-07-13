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
from sklearn.svm import SVC
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
import types
import functools
from individual_feature import extract_features_mfcc, extract_features_mel, extract_features_fourier_tempogram, extract_features_tempogram, extract_features_chroma, extract_features_contrast, extract_features_tonnetzs


#### Dependencies ####

def copy_func(f):
    """Based on http://stackoverflow.com/a/6528148/190597 (Glenn Maynard)"""
    g = types.FunctionType(f.__code__, f.__globals__, name=f.__name__,
                           argdefs=f.__defaults__,
                           closure=f.__closure__)
    g = functools.update_wrapper(g, f)
    g.__kwdefaults__ = f.__kwdefaults__
    return g


def feature_extraction(extraction_method):
    if not (extraction_method == "extract_features_mfcc" or extraction_method == "extract_features_mel" or extraction_method == "extract_features_fourier_tempogram"
            or extraction_method == "extract_features_chroma" or extraction_method == "extract_features_tempogram" or extraction_method == "extract_features_contrast"
            or extraction_method == "extract_features_tonnetzs" or extraction_method == "extract_features_tempogram"):
        raise Exception("Please select a valid method")

    if extraction_method == "extract_features_mfcc":
        extraction = copy_func(extract_features_mfcc)
    if extraction_method == "extract_features_mel":
        extraction = copy_func(extract_features_mel)
    if extraction_method == "extract_features_fourier_tempogram":
        extraction = copy_func(extract_features_fourier_tempogram)
    if extraction_method == "extract_features_chroma":
        extraction = copy_func(extract_features_chroma)
    if extraction_method == "extract_features_contrast":
            extraction = copy_func(extract_features_contrast)
    if extraction_method == "extract_features_tonnetzs":
            extraction = copy_func(extract_features_tonnetzs)
    if extraction_method == "extract_features_tempogram":
        extraction = copy_func(extract_features_tempogram)

    features = []
    # Set the path to the full BirdSound dataset
    full_dataset_path = 'test_audio_3'
    metadata = pd.read_csv('test_3.csv')
    for index, row in metadata.iterrows():
        file_name = os.path.join(os.path.abspath(full_dataset_path), str(row['primary_label']) + '/',
                                 str(row['filename']))
        class_label = row["primary_label"]
        data = extraction(file_name)
        features.append([data, class_label])
        print('parsing' + file_name + '.')
    return features


if __name__ == '__main__':
    input_features = feature_extraction(extraction_method="extract_features_fourier_tempogram")
    # Convert into a Panda dataframe
    features_df = pd.DataFrame(input_features, columns=['feature', 'class_label'])
    # features_df.head

    # Convert features and corresponding classification labels into numpy arrays
    X = np.asarray(features_df.feature.tolist())
    y = np.asarray(features_df.class_label.tolist())

    # Encode the classification labels
    le = LabelEncoder()
    yy = to_categorical(le.fit_transform(y))

    # split the dataset
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.4, random_state=0)
    print('fitting...')

    # training with SVM
    clf = SVC(C=10.0, gamma=0.00001, kernel='rbf')
    # clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
    clf.fit(X_train, y_train)

    # evaluate
    acc = clf.score(X_test, y_test)
    print("acc=%0.3f" % acc)

