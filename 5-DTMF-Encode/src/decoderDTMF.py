#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-------# Recepção de áudio #-------#
# Deve receber um áudio pelo microfone
# A cada segundo plota um gráfico do sinal recebido pelo microfone

#-------# Tons #-------#
#Recebe cada um dos tons (a cada 1 segundo) e salva os sinais para uso futuro. 

import numpy as np
import math
import sounddevice as sd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
# https://python-sounddevice.readthedocs.io/en/0.3.8/

fs = 44100
sd.default.samplerate = fs
sd.default.channels = 1
duration = 5

arquivo_audio = "./audio/recebido.wav"

audio = sd.rec(duration*fs)
print ("Microfone gravando... ")
sd.wait()

y = audio[:,0]
sd.play(y, fs)
print ("Reproduzindo audio gravado...")
sd.wait()

print("-------------------------")
print ("Salvando dados no arquivo :")
print (" - {}".format(arquivo_audio))
file = open(arquivo_audio, 'wb')
file.write(y)
print("Arquivo Salvo")


x = np.linspace(0, duration*fs, duration*fs)
plt.plot(x, y)
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()

