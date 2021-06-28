# importing dependencies#
import pandas as pd
import numpy as np # matrix math
from scipy.io import wavfile # reading the wavfile
import os # interation with the OS
from sklearn.utils import shuffle # shuffling of data
from random import sample # random selection
from tqdm import tqdm # progress bar

import matplotlib.pyplot as plt

# audio processing
from scipy import signal # audio processing
from scipy.fftpack import dct
import librosa # library for audio processing
import librosa.display

PATH = 'data/train_short_audio/acafly/XC6671.ogg'
librosa_audio, librosa_sample_rate = librosa.load(PATH)
#print("Librosa sample rate: {}".format(librosa_sample_rate))

plt.figure(figsize=(12, 4))
plt.plot(librosa_audio)
plt.show()
#plt.savefig('librosa_audio.png')

#chroma_stft
chromas = librosa.feature.chroma_stft(y = librosa_audio, sr = librosa_sample_rate)
chroma_stft = np.mean(chromas.T, axis = 0)
print('chroma_stft shape: ', chromas.shape, chroma_stft.shape)

#chroma_cqt, Constant-Q chromagram
chromac = librosa.feature.chroma_cqt(y = librosa_audio, sr = librosa_sample_rate)
chroma_cqt = np.mean(chromas.T, axis = 0)
print('chroma_cqt shape: ', chromas.shape, chroma_cqt.shape)

#chroma_cen, Chroma Energy Normalized
chromacn = librosa.feature.chroma_cens(y = librosa_audio, sr = librosa_sample_rate)
chroma_cen= np.mean(chromas.T, axis = 0)
print('chroma_cen shape: ', chromacn.shape, chroma_cen.shape)

#mel
mels = librosa.feature.melspectrogram(y = librosa_audio, sr = librosa_sample_rate)
mel = np.mean(mels.T, axis = 0)
print('mel shape: ', mels.shape, mel.shape)

#mfcc
mfccs = librosa.feature.mfcc(y = librosa_audio, sr = librosa_sample_rate, n_mfcc=40)
mfcc = np.mean(mfccs.T, axis = 0)
print('mfcc shape: ', mfccs.shape, mfcc.shape)
#Librosa calculated 40 MFCCs over a 1358 frame audio sample.

#rms
rmss = librosa.feature.rms(y = librosa_audio)
rms = np.mean(rmss.T, axis = 0)
print('rms shape: ', rmss.shape, rms.shape)

#spectral_centroid
centroids = librosa.feature.spectral_centroid(y = librosa_audio, sr = librosa_sample_rate)
centroid = np.mean(centroids.T, axis = 0)
print('centroid shape: ', centroids.shape, centroid.shape)

#spectral_bandwidth
bandwidths = librosa.feature.spectral_bandwidth(y = librosa_audio, sr = librosa_sample_rate)
bandwidth = np.mean(bandwidths.T, axis = 0)
print('bandwidth shape: ', bandwidths.shape, bandwidth.shape)

#spectral_contrast
S = np.abs(librosa.stft(librosa_audio))
contrasts = librosa.feature.spectral_contrast(S = S, sr = librosa_sample_rate)
contrast = np.mean(contrasts.T, axis = 0)
print('contrast shape:', contrasts.shape, contrast.shape)

#spectral_flatness
flatnesss = librosa.feature.spectral_flatness(y = librosa_audio)
flatness = np.mean(flatnesss.T, axis = 0)
print('flatness shape:', flatnesss.shape, flatness.shape)

#spectral_rolloff
rolloffs = librosa.feature.spectral_rolloff(y = librosa_audio)
rolloff = np.mean(rolloffs.T, axis = 0)
print('rolloff shape:', rolloffs.shape, rolloff.shape)

#poly_features
polys = librosa.feature.poly_features(y = librosa_audio, sr = librosa_sample_rate)
poly = np.mean(polys.T, axis = 0)
print('poly shape:', polys.shape, poly.shape)

#tonnetz
tonnetzs = librosa.feature.tonnetz(y = librosa.effects.harmonic(librosa_audio), sr = librosa_sample_rate)
tonnetz = np.mean(tonnetzs.T, axis = 0)
print('tonnetz shape: ', tonnetzs.shape, tonnetz.shape)

#zero_crossing rate
zero_crossings = librosa.feature.zero_crossing_rate(y = librosa_audio)
zero_crossing = np.mean(zero_crossings.T, axis = 0)
print('zero_crossing shape:', zero_crossings.shape, zero_crossing.shape)

#tempogram
hop_length = 512
oenv = librosa.onset.onset_strength(y = librosa_audio, sr = librosa_sample_rate, hop_length=hop_length)
tempograms = librosa.feature.tempogram(onset_envelope = oenv, sr = librosa_sample_rate, hop_length = hop_length)
tempogram = np.mean(tempograms.T, axis = 0)
print('tempogram shape:', tempograms.shape, tempogram.shape)
# Compute global onset autocorrelation
ac_global = librosa.autocorrelate(oenv, max_size=tempogram.shape[0])
ac_global = librosa.util.normalize(ac_global)
# Estimate the global tempo for display purposes
tempo = librosa.beat.tempo(onset_envelope = oenv, sr = librosa_sample_rate, hop_length = hop_length)[0]

#fourier_tempogram
hop_length = 512
oenv = librosa.onset.onset_strength(y = librosa_audio, sr = librosa_sample_rate, hop_length=hop_length)
fourier_tempograms = librosa.feature.fourier_tempogram(onset_envelope = oenv, sr = librosa_sample_rate, hop_length = hop_length)
fourier_tempogram = np.mean(fourier_tempograms.T, axis = 0)
print('fourier_tempogram shape:', fourier_tempograms.shape, fourier_tempogram.shape)
# Compute global onset autocorrelation
ac_tempogram = librosa.feature.tempogram(onset_envelope = oenv, sr = librosa_sample_rate, hop_length = hop_length)
fig, ax = plt.subplots(nrows=3, sharex=True)
ax[0].plot(librosa.times_like(oenv), oenv, label='Onset strength')
ax[0].legend(frameon=True)
ax[0].label_outer()
librosa.display.specshow(np.abs(fourier_tempograms), sr=librosa_sample_rate, hop_length=hop_length, x_axis='time', y_axis='fourier_tempo', cmap='magma', ax=ax[1])
ax[1].set(title='Fourier tempogram')
ax[1].label_outer()
librosa.display.specshow(ac_tempogram, sr=librosa_sample_rate, hop_length=hop_length, x_axis='time', y_axis='tempo', cmap='magma', ax=ax[2])
ax[2].set(title='Autocorrelation tempogram')
plt.show()
plt.savefig('tempo_features.png')

def plot_features(features_extraction):
    plt.figure(figsize=(8, 8))
    librosa.display.specshow(features_extraction, sr = librosa_sample_rate, x_axis='time')
    plt.show()


