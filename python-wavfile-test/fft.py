from recorder import record
from printwave import printW

import wave as we
import numpy as np
import matplotlib.pyplot as plt
import sys

def wavread(path):
	wavfile = we.open(path, "rb")
	params = wavfile.getparams()
	nchannels, sampwidth, framesra, frameswav = params[:4]
	print("nchannels:%d" % nchannels)
	print("sampwidth:%d" % wavfile.getsampwidth())
	datawav = wavfile.readframes(frameswav)
	wavfile.close()
	datause = np.fromstring(datawav, dtype=np.short)
	if nchannels == 2:
		datause.shape = -1, 2
	datause = datause.T
	time = np.arange(0, frameswav) * (1.0 / framesra)
	return datause, time, nchannels

def fft(path):
	wavdata, wavtime, nchannels = wavread(path)
	df = 1
	freq = [df * n for n in range(0, len(wavdata))]
	c = np.fft.fft(wavdata) * nchannels
	print(c)
	d = int(len(c) / 2)
	fig, ax = plt.subplots(2, 1)
	ax[0].plot(wavtime, wavdata, color='green')
	ax[0].set_xlabel('Time')
	ax[0].set_ylabel('Amplitude')
	ax[1].plot(freq[70:800], abs(c)[70:800], color='red')
	ax[1].set_xlabel('Freq(HZ)')
	ax[1].set_ylabel('Y(freq)')
	plt.show()


filename = '../wav/shi.wav'
# record(filename, 2)
printW(filename)
# fft(filename)

