#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#-------# Geração dos Tons #-------#
# Geração de tons DTMF para cada um dos símbolos (0,1,2,...9)
# Para cada símbolo, plota-se os sinais gerados no tempo
# Interface gráfica para transmitir os tons
# Exibição da transformada de Fourier dos sinais (transmitido e recuperado)

import numpy as np
import sounddevice as sd
import matplotlib.pyplot as plt
import math

periodo = 1
fs = 44100
duration = 5
x = np.linspace(0, periodo, fs * periodo)

def getTone(tone):
    DTMF = {1: (697, 1209),
            2: (697, 1336),
            3: (697, 1477),
            4: (770, 1209),
            5: (770, 1336),
            6: (770, 1477),
            7: (852, 1209),
            8: (852, 1336),
            9: (852, 1477),
            "A": (941, 1209),
            0: (941, 1336),
            "H": (941, 1477),
            } 
    return(DTMF.get(tone))

def makeTone(tone):
    Tone = createToneWave(getTone(tone))

    sd.play(Tone, fs)
    print("Reproduzindo tom criado...")
    sd.wait()
    
    print("Plotanto gráfico do tom criado...")
    plotTone(Tone)

def createToneWave(tone):
    lower, higher = tone
    return np.sin(2 * math.pi * x * lower) + np.sin(2 * math.pi * x * higher)

def plotTone(tone):
    plt.title('Sound Wave')
    plt.ylabel('Amplitude')
    plt.plot(x[0:500], tone[0:500])
    plt.axis('tight')
    plt.legend(loc='upper right')
    plt.show()