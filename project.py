from pyAudioAnalysis import audioTrainTest as aT
#from collections import defaultdict
import pickle
import pyaudio
import wave
import speech_recognition as sr

curse_words= ['bad','dumb','stupid']

count=0

def getResults(file = 'pyAudioAnalysis/data/speechEmotion/00.wav'):
	global count,curse_words
	emo = aT.fileClassification(file,'pyAudioAnalysis/svmemopikl','svm')
	r = sr.Recognizer()
	with sr.AudioFile(file) as source:
		audio = r.record(source)
	stt = r.recognize_sphinx(audio)
	for i in stt.split():
		if i in curse_words:
			count+=1
	return emo[2][int(emo[0])], stt, count


CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "file_temp.wav"

while True:
	try:

		p = pyaudio.PyAudio()
		stream = p.open(format=FORMAT,
						channels=CHANNELS,
						rate=RATE,
						input=True,
						frames_per_buffer=CHUNK)

		print("* recording")

		frames = []

		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data)

		print("* done recording")

		stream.stop_stream()
		stream.close()
		p.terminate()

		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()
	except Exception as e:
		print("Error in recording: ", e)

	print (getResults(WAVE_OUTPUT_FILENAME))
