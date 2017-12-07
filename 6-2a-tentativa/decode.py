#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import time as time
import math
import numpy as np
import sounddevice as sd
import soundfile as sf
from scipy.fftpack import fft, ifft
from scipy.signal import find_peaks_cwt

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from path import path

fs = 44100
duration = 1
x = np.linspace(0, duration, fs * duration)

recordingSteps = 12

sd.default.samplerate = fs
sd.default.channels = 1
arquivo_audio = "./audio/recebido"


def generateFilePath(fileName, counter):
    return "./audio/tom_ask.wav"  # fileName + str(counter) + ".wav"


def record_to_file(file, data, fs):
    sf.write(file, data, fs)


def play_sound(data, fs):
    print("Reproduzindo audio gravado...")
    sd.play(data, fs)
    sd.wait()

def calcFFT(signal):
    N  = len(signal)
    T  = 1/fs
    xf = np.linspace(0.0, 1.0/(2.0*T), N//2)
    yf = fft(signal)
    return(xf, yf[0:N//2])


def return_two_main_freqs(lista):
    cleared_indexes = []
    indexes = find_peaks_cwt(lista, np.arange(1, 300))
    #get only interesting values
    for value in list(indexes):
        if 650 <= value <= 1700:
            cleared_indexes.append(value)
    high = max(cleared_indexes)
    low = min(cleared_indexes)
    return (high, low)

def cast_to_symbol(high, low):
    error = 5
    msg = '\n ---------------- \n Símbolo DTMF: {0} \n ---------------- \n '
    if 1209-error <= high <= 1209+error:
        if 697-error <= low <= 697+error:
            print(msg.format(1))
        elif 770-error <= low <= 770+error:
            print(msg.format(4))
        elif 852-error <= low <= 852+error:
            print(msg.format(7))
    elif 1336-error <= high <= 1336+error:
        if 697-error <= low <= 697+error:
            print(msg.format(2))
        elif 770-error <= low <= 770+error:
            print(msg.format(5))
        elif 852-error <= low <= 852+error:
            print(msg.format(8))
        elif 941-error <= low <= 941+error:
            print(msg.format(0))
    elif 1477-error <= high <= 1477+error:
        if 697-error <= low <= 697+error:
            print(msg.format(3))
        elif 770-error <= low <= 770+error:
            print(msg.format(6))
        elif 852-error <= low <= 852+error:
            print(msg.format(9))
    else:
        print("\n ---------------- \n Símbolo DTMF: NÃO IDENTIFICADO \n ---------------- \n ")


    print("Freq. Alta: {0}".format(high))
    print("Freq. Baixa: {0}".format(low))


print("Microfone gravando em: ")
print("3...")
time.sleep(0.5)
print("2...")
time.sleep(0.5)
print("1...")
time.sleep(0.5)
print("Gravando por {0} segundos".format(duration))
audio = sd.rec(duration * fs)
sd.wait()

print("Pronto, audio gravado:")

y = audio[:, 0]

print("Plotando sinal no tempo")
plt.plot(x, y)
plt.title('Sinal no Tempo')
plt.ylabel('Amplitude')
plt.xlabel('Tempo')
plt.axis('tight')
plt.show()

time.sleep(2)

print("Plotando no domínio da frequência")

X, Y = calcFFT(y)
y_graph = list(np.abs(Y))
high, low = return_two_main_freqs(y_graph)
cast_to_symbol(high, low)

plt.plot(y_graph)
plt.title('Sinal no Tempo')
plt.ylabel('Amplitude')
plt.xlabel('Frequencia')
plt.axis('tight')
plt.show()