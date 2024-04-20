# Audio file formats:
# .mp3
# .flac
# .wav


# Audio signal parameters
#     - Number of channels: Mono or stereo
#     - sample width:
#     - framerate/ sample_rate: Sample freq, number of samples of each second. eg 44,100 Hz (or 44.1 KHz sample values each second)
#     - number of frames
#     - values of a frame

#Todo Loading a file
import wave

obj = wave.open("voice.wav", "rb")  # rb --> read in binary

#! Details of the audio
print("Number of channels:", obj.getnchannels())
print("Sample width:", obj.getsampwidth())
print("Frame rate:", obj.getframerate())
print("Number of frames", obj.getnframes())
print("Parameters", obj.getparams())

#! Time duration of the audio
t_audio = obj.getnframes()/ obj.getframerate()
print(t_audio)

#! Frames
frames = obj.readframes(-1)
print(type(frames), type(frames[0]))
print(len(frames)/4)

obj.close()

#! Creatin new file with other features of audio
obj_new = wave.open("voice_new.wav", "wb")
obj_new.setnchannels(1)
obj_new.setsampwidth(2)
obj_new.setframerate(16000.0)
obj_new.writeframes(frames)
obj_new.close()