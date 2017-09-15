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
# https://python-sounddevice.readthedocs.io/en/0.3.8/

fs = 44100
sd.default.samplerate = fs
sd.default.channels = 1
duration = 5

def getTone(tone):
    DTMF = {
        '1': (697, 1209),
        '2': (697, 1336),
        '3': (697, 1477),
        '4': (770, 1209),
        '5': (770, 1336),
        '6': (770, 1477),
        '7': (852, 1209),
        '8': (852, 1336),
        '9': (852, 1477),
        '*': (941, 1209),
        '0': (941, 1336),
        '#': (941, 1477),
    } 
    return(DTMF.get(tone))

audio = sd.rec(duration*fs)
sd.wait()

y = audio[:,0]

x = np.linspace(0, duration*fs, duration*fs)
plt.plot(x, y)
plt.xlabel('Angle [rad]')
plt.ylabel('sin(x)')
plt.axis('tight')
plt.show()

