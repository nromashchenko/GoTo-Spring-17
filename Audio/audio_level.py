import pyaudio, struct

FRAMERATE = 44100
BUFFER = 4096

result = b""

audio = pyaudio.PyAudio()
in_stream = audio.open(format=pyaudio.paInt16, channels=1,
                       rate=FRAMERATE, input=True, frames_per_buffer=BUFFER)
seconds = 5

while True:
    s = 0
    k = 0
    for i in range(int(0.1 * FRAMERATE / BUFFER)):
        data = in_stream.read(BUFFER)
        frames = struct.unpack("<{0}h".format(len(data) // 2), data)
        for frame in frames:
            s += abs(frame)
        k += len(frames)
    print(s // k)