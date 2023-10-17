import numpy as np
import numpy.fft
import pylab as plt

# Constructing time signal
Fs = 256  # Sampling freq (Hz).
tStep = 1 / Fs  # Sample time interval
F = 5  # Signal freq

# N = int(Fs/F)                   #No of samples

# t = np.linspace(0,1,N,endpoint=False)
tt = np.linspace(0, 1, 256, endpoint=False)
# print(t)
# print(tt)
y = np.sin(2 * np.pi * F * tt)
plt.plot(tt, y, '*')
plt.title('Sine wave')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.show()

# fourier transform
sp = numpy.fft.fft(y)  # correct
# X_mag = np.abs(X)
signal = y
n = signal.size
freq = np.fft.fftfreq(n, d=1 / 256)
plt.plot(freq, abs(sp))
plt.show()
