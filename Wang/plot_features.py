import librosa # library for audio processing
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import numpy

def show_chroma(path):
    librosa_audio, librosa_sample_rate = librosa.load(path)
    chroma = librosa.feature.chroma_stft(y=librosa_audio, sr=librosa_sample_rate)
    # chroma_stft = np.mean(chromas.T, axis=0)

    plt.figure(figsize=(12, 4))
    librosa.display.specshow(chroma, sr=librosa_sample_rate, x_axis='time')
    plt.title('chromas')
    plt.savefig('feature_plot/chroma.png')
    plt.show()

def show_contrast(path):
    librosa_audio, librosa_sample_rate = librosa.load(path)
    S = np.abs(librosa.stft(librosa_audio))
    contrast = librosa.feature.spectral_contrast(S=S, sr=librosa_sample_rate)
    # contrast = np.mean(contrasts.T, axis=0)

    plt.figure(figsize=(12, 4))
    librosa.display.specshow(contrast, sr=librosa_sample_rate, x_axis='time')
    plt.title('contrast')
    plt.savefig('feature_plot/contrast.png')
    plt.show()

def show_mel(path):
    librosa_audio, librosa_sample_rate = librosa.load(path)
    # D = np.abs(librosa.stft(librosa_audio)) ** 2
    # S = librosa.feature.melspectrogram(S=D, sr=librosa_sample_rate)
    mel = librosa.feature.melspectrogram(y=librosa_audio, sr=librosa_sample_rate, n_mels=128, fmax = 8000)
    S_DB = librosa.power_to_db(mel, ref=np.max)
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(S_DB, sr=librosa_sample_rate, x_axis='time')
    # plt.colorbar(format='%+2.0f dB');
    plt.title('mel')
    plt.savefig('feature_plot/mel.png')
    plt.show()

def show_mfcc(path):
    librosa_audio, librosa_sample_rate = librosa.load(path)
    mfcc = librosa.feature.mfcc(y = librosa_audio, sr = librosa_sample_rate, n_mfcc=40)
    # mfcc = np.mean(mfccs.T, axis = 0)

    plt.figure(figsize=(12, 4))
    librosa.display.specshow(mfcc, sr=librosa_sample_rate, x_axis='time')
    plt.title('mfcc')
    plt.savefig('feature_plot/mfcc.png')
    plt.show()

def show_tonnetz(path):
    librosa_audio, librosa_sample_rate = librosa.load(path)
    tonnetz = librosa.feature.tonnetz(y=librosa.effects.harmonic(librosa_audio), sr=librosa_sample_rate)

    plt.figure(figsize=(12, 4))
    librosa.display.specshow(tonnetz, sr=librosa_sample_rate, x_axis='time')
    plt.title('tonnetz')
    plt.savefig('feature_plot/tonnetz.png')
    plt.show()


def show_tempogram(path):
    librosa_audio, librosa_sample_rate = librosa.load(path, res_type='kaiser_fast')
    hop_length = 512
    oenv = librosa.onset.onset_strength(y=librosa_audio, sr=librosa_sample_rate, hop_length=hop_length)
    tempogram = librosa.feature.tempogram(onset_envelope=oenv, sr=librosa_sample_rate,
                                                           hop_length=hop_length)
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(np.abs(tempogram), sr=librosa_sample_rate, hop_length=hop_length,
                             x_axis = 'time', cmap = 'magma')
    plt.title('tempogram')
    plt.savefig('feature_plot/tempogram.png')
    plt.show()

def show_fourier_tempogram(path):
    librosa_audio, librosa_sample_rate = librosa.load(path, res_type='kaiser_fast')
    hop_length = 512
    oenv = librosa.onset.onset_strength(y=librosa_audio, sr=librosa_sample_rate, hop_length=hop_length)
    fourier_tempogram = librosa.feature.fourier_tempogram(onset_envelope=oenv, sr=librosa_sample_rate,
                                                            hop_length=hop_length)


    # Compute the auto-correlation tempogram, unnormalized to make comparison easier
    ac_tempogram = librosa.feature.tempogram(onset_envelope=oenv, sr=librosa_sample_rate, hop_length = hop_length, norm = None)
    plt.figure(figsize=(12, 4))
    librosa.display.specshow(np.abs(ac_tempogram), sr=librosa_sample_rate, hop_length=hop_length,
                             x_axis = 'time',cmap = 'magma')
    plt.title('fourier_tempogram')
    plt.savefig('feature_plot/fourier_tempogram.png')
    plt.show()

if __name__ == '__main__':
    show_chroma('test_audio_10/acafly/XC51408.ogg')
    show_mel('test_audio_10/yerwar/XC138298.ogg')
    show_mfcc('test_audio_10/acafly/XC51408.ogg')
    show_contrast('test_audio_10/acafly/XC51408.ogg')
    show_tonnetz('test_audio_10/acafly/XC51408.ogg')
    show_tempogram('test_audio_10/acafly/XC51408.ogg')
    show_fourier_tempogram('test_audio_10/acafly/XC51408.ogg')



