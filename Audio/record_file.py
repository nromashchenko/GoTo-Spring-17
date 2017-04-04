import pyaudio
import wave

FRAMERATE = 44100
BUFFER = 4096


music_file = wave.open("result2.wav", "wb")
music_file.setnchannels(1)
music_file.setframerate(FRAMERATE)
music_file.setsampwidth(2)

audio = pyaudio.PyAudio()
in_stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=FRAMERATE, input=True, frames_per_buffer=BUFFER)
seconds = 5

for i in range(seconds * FRAMERATE // BUFFER):
    data = in_stream.read(BUFFER)
    music_file.writeframes(data)
in_stream.stop_stream()





