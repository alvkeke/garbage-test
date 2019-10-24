import numpy as np
import soundfile as sf
import matplotlib.pyplot as plt
import wave

filename = r'/home/alvis/desktop/sound-classification/wav/output.wav'

def readWave(filename, sampleWidth = 2):
	data, rate = sf.read(filename)
	data = data.T
	return data, rate



f = wave.open(filename, 'rb')
nframes = f.getnframes()
rate = f.getframerate()
data_str = f.readframes(nframes)
data = np.fromstring(data_str, np.short)


data , rate = readWave(filename, 3)



times = np.arange(0, len(data)) * (1.0/rate)
nchannels = len(data)

plt.subplot(2, 2, 1)
plt.plot(times, data)
plt.xlabel('Time/s')

df = 1
freq = [df * n for n in range(0, len(data))]
c = np.fft.fft(data) * nchannels
c = np.abs(c)

freq_begin = 0
freq_end = 1000
# freq_end = len(freq)
plt.subplot(2, 2, 3)
plt.plot(freq[freq_begin:freq_end], c[freq_begin:freq_end])

plt.show()
