import matplotlib.pyplot as plt
import numpy as np
from scipy.io import wavfile  # scipy library to read wav files


def extract(input, output):
    fs, audiodata = wavfile.read(input)

    # Plot the audio signal in time
    plt.plot(audiodata)
    plt.figure()
    # plt.show()

    # Spectrogram
    from scipy import signal
    my_dpi = 96
    N = 512  # Number of point in the fft
    f, t, sxx = signal.spectrogram(audiodata, fs, window=signal.blackman(N), nfft=N)
    fig = plt.figure(frameon=False, figsize=(160/my_dpi, 120/my_dpi), dpi=my_dpi)
    plt.axis('off')
    ax = plt.Axes(fig, [0., 0., 1., 1.])
    ax.set_axis_off()
    fig.add_axes(ax)
    plt.pcolormesh(t, f, 10 * np.log10(sxx))  # dB spectrogram

    plt.savefig(output, bbox_inches=0, transparent=True, pad_inches=0, dpi=my_dpi)
    plt.close(fig)
    plt.close("all")