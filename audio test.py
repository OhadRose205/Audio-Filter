import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import butter, lfilter

signal, fs = sf.read('example.wav')
t = np.arange(len(signal)) / fs

# show original wave
plt.figure(figsize=(10, 4))
plt.plot(t, signal)
plt.title("Raw audio signal")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()

def butter_lowpass(cutoff, fs, order=5):
    nyq = fs * 0.5
    normal_cutoff = cutoff / nyq
    b, a = butter(order, normal_cutoff, btype='low', analog=False)
    return b, a

def apply_filter(data, cutoff, fs):
    b, a = butter_lowpass(cutoff, fs)
    return lfilter(b, a, data)


filtered_signal = apply_filter(signal, cutoff=3000, fs=fs)

# show filtered wave
plt.plot(t, filtered_signal)
plt.title("Filtered Audio")
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.grid()
plt.show()