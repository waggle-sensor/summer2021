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
    y, sr = librosa.load(path)
    onset_env = librosa.onset.onset_strength(y, sr=sr)
    tempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr)

    import scipy.stats
    prior = scipy.stats.uniform(30, 300)  # uniform over 30-300 BPM
    utempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, prior=prior)

    dtempo = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, aggregate = None)
    # Dynamic tempo with a proper log-normal prior
    prior_lognorm = scipy.stats.lognorm(loc=np.log(120), scale=120, s=1)
    dtempo_lognorm = librosa.beat.tempo(onset_envelope=onset_env, sr=sr, aggregate = None,prior = prior_lognorm)

    # Convert to scalar
    tempo = tempo.item()
    utempo = utempo.item()
    # Compute 2-second windowed autocorrelation
    hop_length = 512
    ac = librosa.autocorrelate(onset_env, 2 * sr // hop_length)
    freqs = librosa.tempo_frequencies(len(ac), sr=sr, hop_length = hop_length)
    # Plot on a BPM axis.  We skip the first (0-lag) bin.
    fig, ax = plt.subplots()
    ax.semilogx(freqs[1:], librosa.util.normalize(ac)[1:], label = 'Onset autocorrelation', basex = 2)
    ax.axvline(tempo, 0, 1, alpha=0.75, linestyle='--', color='r', label = 'Tempo (default prior): {:.2f} BPM'.format(tempo))
    ax.axvline(utempo, 0, 1, alpha=0.75, linestyle=':', color='g', label = 'Tempo (uniform prior): {:.2f} BPM'.format(utempo))
    ax.set(xlabel='Tempo (BPM)', title='Static tempo estimation')
    ax.grid(True)
    ax.legend()
    fig.savefig('tempogram.png')
    fig.show()
    # Plot dynamic tempo estimates over a tempogram
    fig, ax = plt.subplots()
    tg = librosa.feature.tempogram(onset_envelope=onset_env, sr=sr, hop_length = hop_length)
    librosa.display.specshow(tg, x_axis='time', y_axis='tempo', cmap='magma', ax=ax)
    ax.plot(librosa.times_like(dtempo), dtempo,color = 'c', linewidth = 1.5, label = 'Tempo estimate (default prior)')
    ax.plot(librosa.times_like(dtempo_lognorm), dtempo_lognorm, color = 'c', linewidth = 1.5, linestyle = '--',
            label = 'Tempo estimate (lognorm prior)')
    ax.set(title='Dynamic tempo estimation')
    ax.legend()
    fig.savefig('dynamic_tempogram.png')
    fig.show()


def show_fourier_tempogram(path):
    librosa_audio, librosa_sample_rate = librosa.load(path, res_type='kaiser_fast')
    hop_length = 512
    oenv = librosa.onset.onset_strength(y=librosa_audio, sr=librosa_sample_rate, hop_length=hop_length)
    fourier_tempogram = librosa.feature.fourier_tempogram(onset_envelope=oenv, sr=librosa_sample_rate,
                                                            hop_length=hop_length)


    # Compute the auto-correlation tempogram, unnormalized to make comparison easier
    ac_tempogram = librosa.feature.tempogram(onset_envelope=oenv, sr=librosa_sample_rate, hop_length = hop_length, norm = None)
    fig, ax = plt.subplots(nrows=3, sharex=True)
    ax[0].plot(librosa.times_like(oenv), oenv, label='Onset strength')
    ax[0].legend(frameon=True)
    ax[0].label_outer()
    librosa.display.specshow(np.abs(fourier_tempogram), sr=librosa_sample_rate, hop_length=hop_length, x_axis = 'time', y_axis = 'fourier_tempo', cmap = 'magma',ax = ax[1])
    ax[1].set(title='Fourier tempogram')
    ax[1].label_outer()
    librosa.display.specshow(ac_tempogram, sr=librosa_sample_rate, hop_length=hop_length,x_axis = 'time', y_axis = 'tempo', cmap = 'magma',ax = ax[2])
    ax[2].set(title='Autocorrelation tempogram')

    plt.figure(figsize=(12, 4))
    librosa.display.specshow(np.abs(ac_tempogram), sr=librosa_sample_rate, hop_length=hop_length,
                             x_axis = 'time',cmap = 'magma')
    fig.savefig('fourier_tempogram.png')
    fig.show()

if __name__ == '__main__':
    # show_chroma('test_audio_10/acafly/XC51408.ogg')
    # show_mel('test_audio_10/yerwar/XC138298.ogg')
    # show_mfcc('test_audio_10/acafly/XC51408.ogg')
    # show_contrast('test_audio_10/acafly/XC51408.ogg')
    # show_tonnetz('test_audio_10/acafly/XC51408.ogg')
    show_tempogram('test_audio_10/acafly/XC51408.ogg')
    # show_fourier_tempogram('test_audio_10/acafly/XC51408.ogg')



