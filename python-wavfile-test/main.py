import soundfile as sf
import numpy as np
import tensorflow as tf
import pyaudio
import wave
import matplotlib.pyplot as plt


pa = pyaudio.PyAudio()

def record(filename, time_second, channels=1, rate=44100):
	CHUNK = 1024
	FORMAT = pyaudio.paInt16
	# CHANNELS = 1
	# RATE = 44100
	# RECORD_SECONDS = 5
	# WAVE_OUTPUT_FILENAME = "output.wav"

	p = pyaudio.PyAudio()

	stream = p.open(format=FORMAT,
					# channels=CHANNELS,
					# rate=RATE,
					channels = channels,
					rate = rate,
					input=True,
					frames_per_buffer=CHUNK)

	print("* recording")

	frames = []

	for i in range(0, int(rate / CHUNK * time_second)):
		data = stream.read(CHUNK)
		frames.append(data)

	print("* done recording")

	stream.stop_stream()
	stream.close()
	p.terminate()

	wf = wave.open(filename, 'wb')
	wf.setnchannels(channels)
	wf.setsampwidth(p.get_sample_size(FORMAT))
	wf.setframerate(rate)
	wf.writeframes(b''.join(frames))
	wf.close()


filename = r'test.wav'
record(filename, 3, 2, 44100)

data, rate = sf.read(filename,dtype='int16')
data = data.T

time = np.arange(len(data[0])) * (1.0/rate)

f_data = np.fft.fft(data)
freq = np.arange(len(f_data[0]))

plt.subplot(2, 2, 1)
plt.plot(time, data[0])
plt.subplot(2, 2, 2)
plt.plot(time, data[1])

f_begin = 0
f_end = 2000

plt.subplot(2, 2, 3)
plt.plot(freq[f_begin:f_end], f_data[0][f_begin:f_end])
plt.subplot(2, 2, 4)
plt.plot(freq[f_begin:f_end], f_data[1][f_begin:f_end])

plt.show()




