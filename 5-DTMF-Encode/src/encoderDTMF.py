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

class encoder(object):
    def __init__(self):
        self.periodo = 1
        self.fs = 44100
        self.duration = 50

    def getTone(self, tone):
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

    def makeTone(self, tone):
        T1 = self.createToneWave(self.getTone(1))
        T2 = self.createToneWave(self.getTone(2)) 
        T3 = self.createToneWave(self.getTone(3))
        
        T4 = self.createToneWave(self.getTone(4))
        T5 = self.createToneWave(self.getTone(5)) 
        T6 = self.createToneWave(self.getTone(6)) 

        T7 = self.createToneWave(self.getTone(7)) 
        T8 = self.createToneWave(self.getTone(8)) 
        T9 = self.createToneWave(self.getTone(9)) 

        TA = self.createToneWave(self.getTone("A"))
        T0 = self.createToneWave(self.getTone(0))
        TH = self.createToneWave(self.getTone("H"))

        sd.play(tone, self.fs)
        print("Reproduzindo tom criado...")
        sd.wait()
        
        print("Plotanto gráfico do tom criado...")
        self.plotTone(tom)

    def createToneWave(self, tone):
        lower, higher = tone
        x = np.linspace(0, self.periodo, self.fs * self.periodo)
        return np.sin(2 * math.pi * x * lower) + np.sin(2 * math.pi * x * higher)

    def plotTone(self,value):
        plt.title('Sond Wave')
        plt.ylabel('Values')
        plt.plot(value, label='values')
        plt.legend(loc='upper right')
        plt.show