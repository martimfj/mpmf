#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import math
import sounddevice as sd
import soundfile as sf

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from path import path
# https://python-sounddevice.readthedocs.io/en/0.3.8/

fs = 44100
duration = 3
x = np.linspace(0, duration, fs*duration)

recordingSteps = 12

sd.default.samplerate = fs
sd.default.channels = 1
arquivo_audio = "./audio/recebido"

def generateFilePath(fileName, counter):
    return "./audio/tom_ask.wav"#fileName + str(counter) + ".wav"

def record_to_file(file, data, fs):
    sf.write(file, data, fs)


def play_sound(data, fs):
    print("Reproduzindo audio gravado...")
    sd.play(data, fs)
    sd.wait()


counter = 0
# while(counter < recordingSteps):
    # counter += 1
audio = sd.rec(duration*fs)
print ("Microfone gravando... ")
sd.wait()

y = audio[:,0]
# play_sound(y, fs)

print("-------------------------")
print ("Salvando dados no arquivo :")
print (" - {}".format(arquivo_audio))
record_to_file(generateFilePath(arquivo_audio, counter), y, fs)
print("Arquivo Salvo")

plt.plot(x[500:1000], y[500:1000])
plt.title('Sound Wave')
plt.ylabel('Amplitude')
plt.xlabel('Tempo')
plt.axis('tight')
plt.show()
