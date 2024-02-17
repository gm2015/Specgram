# Importing libraries using import keyword.
import numpy as np
import matplotlib.pyplot as plt
import scipy.fftpack
import os

from common.constants import *

# Number of samplepoints
N = 600
# sample spacing
T = 1.0 / 1000.0
x = np.linspace(0.0, N*T, N)
Data = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x) + 1.5*np.sin(180.0 * 2.0*np.pi*x)
plt.figure('Original data')
plt.plot(x, Data) 
plt.title('Original data')
plt.ylabel("Value")
plt.xlabel("Time")
plt.savefig(os.path.join(OUTPUT_DIR,'time-domain.png'))

# 'FFT spectrum'
yf = scipy.fftpack.fft(Data)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
plt.figure('FFT spectrum')
plt.plot(xf, 2.0/N * np.abs(yf[:N//2]))
plt.title('FFT spectrum of the data')
plt.ylabel("Spectrum")
plt.xlabel("Frequency")
plt.savefig(os.path.join(OUTPUT_DIR,'fft.png'))

# Matplotlib.pyplot.specgram() function to
# generate spectrogram
plt.figure()
plt.specgram(Data, Fs=6, cmap="rainbow")
plt.savefig(os.path.join(OUTPUT_DIR,'Spectrogram.png'))
# Set the title of the plot, xlabel and ylabel
# and display using show() function
plt.title('Spectrogram Using matplotlib.pyplot.specgram() Method')
plt.ylabel("Data")
plt.xlabel("Data point")
plt.show()



