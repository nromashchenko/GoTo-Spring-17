import wave, struct

music_file = wave.open("task1.wav", "rb")
params = music_file.getparams()
nframes = music_file.getnframes()

music_data = music_file.readframes(nframes)

frames = struct.unpack("<{0}h".format(nframes), music_data)
new_frames = []

for frame in frames:
    new_frames.append(frame*10)

new_music_data = struct.pack("<{0}h".format(nframes), *new_frames)

new_music_file = wave.open("result1.wav", "wb")
new_music_file.setparams(params)
new_music_file.writeframes(new_music_data)
