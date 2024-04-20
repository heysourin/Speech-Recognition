import wave
import numpy as np
import matplotlib.pyplot as plt

wav_obj = wave.open('voice.wav', 'r')

sample_freq = wav_obj.getframerate()
print(sample_freq)

n_samples = wav_obj.getnframes()
print(n_samples)

t_audio = n_samples/sample_freq
print(t_audio, "seconds")

signal_wave = wav_obj.readframes(n_samples)

# Check if the audio is stereo
n_channels = wav_obj.getnchannels()

# Adjust the dtype and shape based on the number of channels
if n_channels == 2: # Stereo
    signal_array = np.frombuffer(signal_wave, dtype=np.int16).reshape(-1, 2)
    # If you want to plot the left channel, for example
    signal_array = signal_array[:, 0]
else: # Mono
    signal_array = np.frombuffer(signal_wave, dtype=np.int16)

print(signal_array.shape)

times = np.linspace(0, t_audio, num=n_samples)
print(times.shape)
plt.figure(figsize=(15, 5))
plt.plot(times, signal_array)
plt.title('Audio')
plt.ylabel('Signal Value')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.show()


plt.figure(figsize=(15, 5))
plt.specgram(signal_array, Fs=sample_freq, vmin=-20, vmax=50)
plt.title('Left Channel')
plt.ylabel('Frequency (Hz)')
plt.xlabel('Time (s)')
plt.xlim(0, t_audio)
plt.colorbar()
plt.show()

