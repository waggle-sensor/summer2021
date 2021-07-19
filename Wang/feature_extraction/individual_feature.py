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

def extract_features_mfcc(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        mfccs = librosa.feature.mfcc(y=audio, sr=sample_rate, n_mfcc=40)
        mfccsscaled = np.mean(mfccs.T, axis=0)
    except Exception as e:
        print("Error encountered while parsing file: ", e)
        return None
    return mfccsscaled


def extract_features_tempogram(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        hop_length = 512
        oenv = librosa.onset.onset_strength(y=audio, sr=sample_rate, hop_length=hop_length)
        tempograms = librosa.feature.tempogram(onset_envelope=oenv, sr=sample_rate, hop_length=hop_length)
        tempogram = np.mean(tempograms.T, axis=0)
    except Exception as e:
        print("Error encountered while parsing file: ", e)
        return None
    return tempogram


def extract_features_fourier_tempogram(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        hop_length = 512
        oenv = librosa.onset.onset_strength(y=audio, sr=sample_rate, hop_length=hop_length)
        fourier_tempogram = librosa.feature.fourier_tempogram(onset_envelope=oenv, sr=sample_rate,
                                                               hop_length=hop_length)
        fourier_tempogram=fourier_tempogram.real
        fourier_tempograms = np.mean(fourier_tempogram.T, axis=0)

    except Exception as e:
        print("Error encountered while parsing file: ", e)
        return None
    return fourier_tempograms


def extract_features_chroma(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        chroma_l = librosa.feature.chroma_stft(y=audio, sr=sample_rate)
        chromascaled = np.mean(chroma_l.T, axis=0)
    except Exception as e:
        print("Error encountered while parsing file: ", e)
        return None
    return chromascaled


def extract_features_mel(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        mel_l = librosa.feature.melspectrogram(audio, sr=sample_rate)
        mel = np.mean(mel_l.T, axis=0)
    except Exception as e:
        print("Error encountered while parsing file: ", e)
        return None
    return mel


def extract_features_contrast(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        contrasts = librosa.feature.spectral_contrast(audio, sr=sample_rate)
        contrast = np.mean(contrasts.T, axis=0)
    except Exception as e:
        print("Error encountered while parsing file: ", e)
        return None
    return contrast


def extract_features_tonnetzs(file_name):
    try:
        audio, sample_rate = librosa.load(file_name, res_type='kaiser_fast')
        tonnetzs = librosa.feature.tonnetz(y=librosa.effects.harmonic(audio), sr=sample_rate)
        tonnetz = np.mean(tonnetzs.T, axis=0)
    except Exception as e:
        print("Error encountered while parsing file: ", e)
        return None
    return tonnetz
