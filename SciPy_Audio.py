import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy import fftpack



if __name__ == '__main__':
    samplerate, data = wavfile.read("resources/sample.wav")
    print(samplerate)
    print(data)
    type(data)
    data.shapedata.ndim
    data.dtypedata.size
    data.nbytes
    plt.plot(data)
    plt.show()
    samples = data.shape[0]
    print(samples)

    samples = data.shape[0]
    print(samples)

    freqs = fftpack.fftfreq(samples, 1/samplerate)
    datafft = fftpack.fft(data)
    fftabs = abs(datafft)
    print(fftabs)
    plt.plot(freqs, fftabs)
    plt.show()
    plt.plot(data[:10*samplerate])
    plt.show()

    channel1 = data[:, 0]
    channel2 = data[:, 1]
    print(channel1, channel2)

    plt.subplot(2, 1, 1)
    plt.plot(channel1[:10*samplerate])
    plt.subplot(2, 1, 2)
    plt.plot(channel2[:10*samplerate])
    plt.show()
