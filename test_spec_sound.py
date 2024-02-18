import torchaudio
import matplotlib.pyplot as plt
import scipy.fftpack
import numpy as np
import os
from utils.constants import *

mp3_file = '.\data\cardinal.mp3'

y, sr = torchaudio.load(mp3_file)
print(type(y), y.shape, y.dtype, y.device)
#print(sr)

#torchaudio.save('out.wav', y, sr)

yn = y.to('cpu')
Data = yn.numpy()[0]

plt.figure('data')
plt.plot(Data) 

N = len(Data)
# sample spacing
T = 1.0 / 2000.0
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
plt.figure('Specgram')
plt.specgram(Data, Fs=6, cmap="rainbow")
plt.savefig(os.path.join(OUTPUT_DIR,'Spectrogram.png'))
# Set the title of the plot, xlabel and ylabel
# and display using show() function
plt.title('Spectrogram Using matplotlib.pyplot.specgram() Method')
plt.ylabel("Data")
plt.xlabel("Data point")
plt.show()