import pyaudio

FRAMERATE = 44100
BUFFER = 4096

result = b""

audio = pyaudio.PyAudio()
in_stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=FRAMERATE, input=True, frames_per_buffer=BUFFER)
seconds = 5

for i in range(seconds * FRAMERATE // BUFFER):
    data = in_stream.read(BUFFER)
    result += data
in_stream.stop_stream()

out_stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=FRAMERATE, output=True)
out_stream.write(result)