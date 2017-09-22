import numpy as np
import math
import sounddevice as sd
import soundfile as sf
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from path import path

# setup de variaveis
frequency = 44100
duration = 0.01

realtime = False

sd.default.samplerate = frequency
sd.default.channels = 1

# Cria plot realtime temporal
plt.ion()
fig = plt.figure("F(y)", figsize=(10, 10))
ax = fig.add_subplot(111)

# Calculate de FFT from a signal
# https://docs.scipy.org/doc/scipy/reference/tutorial/fftpack.html
def calcFFT(signal, fs):
    from scipy.fftpack import fft
    from scipy import signal as window

    N = len(signal)
    T = 1 / fs
    xf = np.linspace(0.0, 1.0 / (2.0 * T), N // 2)
    yf = fft(signal)
    return(xf, yf[0:N // 2])

while True:
    # Atualiza plot
    y, fs = sf.read('./audio/tom_0.wav')
    
    if (realtime):
        audio = sd.rec(duration * frequency)
        y = audio[:, 0]

    y = 20 * np.log10(np.abs(y))
    X, Y = calcFFT(y, frequency)

    ax.clear()
    ax.plot(X[0:5000], np.abs(Y[0:5000]))
    fig.canvas.draw()
    plt.pause(duration)

