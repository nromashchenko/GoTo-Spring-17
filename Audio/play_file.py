import pyaudio
import wave

music_file = wave.open("result1.wav", "rb")
params = music_file.getparams()
nframes = music_file.getnframes()
music_data = music_file.readframes(nframes)


audio = pyaudio.PyAudio()
out_stream = audio.open(format=pyaudio.paInt16, channels=params[0],
                        rate=params[2], output=True)
out_stream.write(music_data)





