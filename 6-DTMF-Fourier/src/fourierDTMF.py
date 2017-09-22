import numpy as np
import math
import sounddevice as sd
import soundfile as sf
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from path import path

fs = 44100
duration = 0.5

recordingSteps = 12
sd.default.samplerate = fs
sd.default.channels = 1

# Cria plot
plt.ion()
fig = plt.figure("F(y)", figsize=(10, 10))
ax = fig.add_subplot(111)

while True:
    # Atualiza plot
    audio = sd.rec(duration * fs)
    x = np.linspace(0, duration, fs * duration)
    y = audio[:, 0]
    ax.clear()
    ax.plot(x[0:2200], y[0:2200])
    fig.canvas.draw()
    plt.pause(duration)
