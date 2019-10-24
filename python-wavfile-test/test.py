import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import soundfile as sf
from scipy.signal import wiener

def readWave(f):
    d, r = sf.read(f)
    d = d.T
    return d, r


filename = r'/home/alvis/desktop/sound-classification/wav/shi.wav'

wave_data, frame_rate = readWave(filename)

time = np.arange(len(wave_data[0])) * (1 / frame_rate)

wave_data = wiener(wave_data)

plt.subplot(2, 2, 1)
plt.plot(time, wave_data[0])
plt.subplot(2, 2, 2)
plt.plot(time, wave_data[1])

cc = np.fft.fft(wave_data) * 2
cc = np.abs(cc)
freq = [1 * n for n in range(0, len(wave_data[0]))]

f_begin = 0
f_end = 1000

plt.subplot(2, 2, 3)
plt.plot(freq[f_begin:f_end], cc[0][f_begin:f_end])
plt.subplot(2, 2, 4)
plt.plot(freq[f_begin:f_end], cc[1][f_begin:f_end])

plt.show()
