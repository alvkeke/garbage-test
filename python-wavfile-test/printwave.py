import wave
import pylab as pl 
import numpy as np 
import pyaudio
import soundfile as sf

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

def readWave(filename):
	data, rate = sf.read(filename)
	return data, rate

def printW(filename):
	# 打开WAV文档 
	f = wave.open(filename, "rb") 

	# 读取格式信息 
	# (nchannels, sampwidth, framerate, nframes, comptype, compname) 
	params = f.getparams() 
	nchannels, sampwidth, framerate, nframes = params[:4] 

	# 读取波形数据 
	str_data = f.readframes(nframes) 
	nframes_r = f.getnframes()
	sw =  f.getsampwidth()
	f.close() 

	#将波形数据转换为数组 
	wave_data = np.fromstring(str_data, dtype=np.short) 

	if nchannels == 2:
		wave_data.shape = -1, 2 
		wave_data = wave_data.T 
		times = np.arange(0, nframes_r) * (1.0 / framerate) 

		# 绘制波形 
		pl.subplot(211)
		pl.plot(times, wave_data[0]) 
		pl.subplot(212)
		pl.plot(times, wave_data[1], c="g") 
		pl.xlabel("time (seconds)") 
		pl.show()

	elif nchannels == 1:
		wave_data.shape = -1, 1 
		wave_data = wave_data.T 
		times = np.arange(0, nframes) * (1.0 / framerate) 
		# 绘制波形 
		pl.subplot(211) 
		pl.plot(times, wave_data[0]) 
		pl.xlabel("time (seconds)") 
		pl.show()

def printW_2(filename):
	# 打开WAV文档 
	# f = wave.open(filename, "rb") 

	# 读取格式信息 
	# (nchannels, sampwidth, framerate, nframes, comptype, compname) 
	# params = f.getparams() 
	# nchannels, sampwidth, framerate, nframes = params[:4] 

	# 读取波形数据 
	# str_data = f.readframes(nframes) 
	# nframes_r = f.getnframes()
	# sw =  f.getsampwidth()
	# f.close() 

	str_data, framerate = readWave(filename)

	nframes = len(str_data)
	nchannels = len(str_data[0])

	#将波形数据转换为数组 
	wave_data = np.fromstring(str_data, dtype=np.long) 

	if nchannels == 2:
		wave_data.shape = -1, 2 
		wave_data = wave_data.T 
		times = np.arange(0, nframes) * (1.0 / framerate) 

		# 绘制波形 
		pl.subplot(211)
		pl.plot(times, wave_data[0]) 
		pl.subplot(212)
		pl.plot(times, wave_data[1], c="g") 
		pl.xlabel("time (seconds)") 
		pl.show()

	elif nchannels == 1:
		wave_data.shape = -1, 1 
		wave_data = wave_data.T 
		times = np.arange(0, nframes) * (1.0 / framerate) 
		# 绘制波形 
		pl.subplot(211) 
		pl.plot(times, wave_data[0]) 
		pl.xlabel("time (seconds)") 
		pl.show()
		

filename = r'/home/alvis/desktop/wav-file-test/wav/shi.wav'
printW_2(filename)
