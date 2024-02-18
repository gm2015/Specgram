import torchaudio
import matplotlib.pyplot as plt

from common.constants import *

mp3_file = '.\data\cardinal.mp3'

y, sr = torchaudio.load(mp3_file)
print(type(y), y.shape, y.dtype, y.device)
print(sr)

#torchaudio.save('out.wav', y, sr)

yn = y.to('cpu')
Y = yn.numpy()
print(Y)
Time = Y[0][0]
Data = Y[0][1]

#print(Data[1:20])
plt.figure(mp3_file)
plt.plot(Time, Data) 

plt.show()


