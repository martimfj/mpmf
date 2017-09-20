#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-------# Geração dos Tons #-------#
# Geração de tons DTMF para cada um dos símbolos (0,1,2,...9)
# Para cada símbolo, plota-se os sinais gerados no tempo
# Interface gráfica para transmitir os tons
# Exibição da transformada de Fourier dos sinais (transmitido e recuperado)

import numpy as np
import math
import sounddevice as sd
import matplotlib.pyplot as plt
# https://python-sounddevice.readthedocs.io/en/0.3.8/

fs = 44100
sd.default.samplerate = fs
sd.default.channels = 1
duration = 5

def getTone(symbol):
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
    return(DTMF.get(symbol))

def makeTone(symbol, x):
    f1, f2 = getTone(symbol)
    return np.sin(2 * np.pi * f1 * x) + np.sin(2 * np.pi * f2 * x)


symbols = ['0','1','2','3','4','5','6','7','8','9','0','*','#']
symbolsPlot = [[0, 0]] # holds our plot of symbols

for (i,symbol) in enumerate(symbols):
    plot = [[0,0]]
    for x in range(1, 100):
        plot.append([x, makeTone(symbol, x)])

    symbols[i] = plot

# value = makeTone(1, 440, 44100)

# audio = sd.rec(duration*fs)
# sd.wait()

# y = audio[:,0]
# print(y)
# print(len(y))
# x = np.linspace(0, duration*fs, duration*fs)
print(symbols[0])
plt.plot(symbols[0])
plt.xlabel('t [s]')
plt.ylabel('Tom')
plt.axis('tight')
plt.show()


# sd.play(y, fs)

# sd.wait()
