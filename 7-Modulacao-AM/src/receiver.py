# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np
import soundfile as sf
import sounddevice as sd
from scipy import signal as sg
import sys
import os
import receiver_ui
import webbrowser
import matplotlib.pyplot as plt
from pylab import *


'''
    Função responsável por receber as ondas de áudio transmitidas, demodula-las e salvar os sinais de áudio.
    Recebe como parâmetro as duas frequências das ondas portadoras usadas para transmitir os sinais.
'''
class Receiver(QtGui.QMainWindow, receiver_ui. Ui_MainWindow):
    def __init__(self, parent=None ):
        super(Receiver, self).__init__(parent)
        self.setupUi(self)
        self.fs = 44100
        self.pen = pyqtgraph.mkPen(color='g')

        self.input_freq1.setText('4000')
        self.input_freq2.setText('15000')

        self.f1 = int(self.input_freq1.text())
        self.f2 = int(self.input_freq2.text())

        self.input_freq1.textChanged.connect(lambda: self.frequency_change("1"))
        self.input_freq2.textChanged.connect(lambda: self.frequency_change("2"))
        
        self.recordDuration = 3 # in seconds
        self.periodo = 1

        #Audio 1 - Time -> Audio Recuperado
        self.widget_audio_1_time.setLabel("left", "Amplitude")
        self.widget_audio_1_time.setLabel("bottom", "Time", "seconds")
        self.widget_audio_1_time.setMouseEnabled(y = False)
        self.widget_audio_1_time.showGrid(True, True, 0.5)

        #Audio 1 - Freq -> Audio Recuperado
        self.widget_audio_1_freq.setLabel("left", "Amplitude")
        self.widget_audio_1_freq.setLabel("bottom", "Frequency", "Hz")
        self.widget_audio_1_freq.setMouseEnabled(y = False)
        self.widget_audio_1_freq.showGrid(True, True, 0.5)

        #Audio 2 - Time -> Audio Recuperado
        self.widget_audio_2_time.setLabel("left", "Amplitude")
        self.widget_audio_2_time.setLabel("bottom", "Time", "seconds")
        self.widget_audio_2_time.setMouseEnabled(y = False)
        self.widget_audio_2_time.showGrid(True, True, 0.5)

        #Audio 2 - Freq -> Audio Recuperado
        self.widget_audio_2_freq.setLabel("left", "Amplitude")
        self.widget_audio_2_freq.setLabel("bottom", "Frequency", "Hz")
        self.widget_audio_2_freq.setMouseEnabled(y = False)
        self.widget_audio_2_freq.showGrid(True, True, 0.5)

        #Audio Modulated Received - Time -> Audio Ouvido
        self.widget_modulated_received_time.setLabel("left", "Amplitude")
        self.widget_modulated_received_time.setLabel("bottom", "Time", "seconds")
        self.widget_modulated_received_time.setMouseEnabled(y = False)
        self.widget_modulated_received_time.showGrid(True, True, 0.5)

        #Audio Modulated Received - Freq -> Audio Ouvido
        self.widget_modulated_received_freq.setLabel("left", "Amplitude")
        self.widget_modulated_received_freq.setLabel("bottom", "Frequency", "Hz")
        self.widget_modulated_received_freq.setMouseEnabled(y = False)
        self.widget_modulated_received_freq.showGrid(True, True, 0.5)

        #Audio Modulated 1 Received - Time -> Audio Ouvido Separado
        self.widget_modulated_1_time.setLabel("left", "Amplitude")
        self.widget_modulated_1_time.setLabel("bottom", "Time", "seconds")
        self.widget_modulated_1_time.setMouseEnabled(y = False)
        self.widget_modulated_1_time.showGrid(True, True, 0.5)

        #Audio Modulated 1 Received - Freq -> Audio Ouvido Separado
        self.widget_modulated_1_freq.setLabel("left", "Amplitude")
        self.widget_modulated_1_freq.setLabel("bottom", "Frequency", "Hz")
        self.widget_modulated_1_freq.setMouseEnabled(y = False)
        self.widget_modulated_1_freq.showGrid(True, True, 0.5)
        
        #Audio Modulated 2 Received - Time -> Audio Ouvido Separado
        self.widget_modulated_2_time.setLabel("left", "Amplitude")
        self.widget_modulated_2_time.setLabel("bottom", "Time", "seconds")
        self.widget_modulated_2_time.setMouseEnabled(y = False)
        self.widget_modulated_2_time.showGrid(True, True, 0.5)

        #Audio Modulated 2 Received - Freq -> Audio Ouvido Separado
        self.widget_modulated_2_freq.setLabel("left", "Amplitude")
        self.widget_modulated_2_freq.setLabel("bottom", "Frequency", "Hz")
        self.widget_modulated_2_freq.setMouseEnabled(y = False)
        self.widget_modulated_2_freq.showGrid(True, True, 0.5)

        #Botão Salvar
        #self.button_save

        #Botão Save
        self.button_record.clicked.connect(lambda: self.onRecordButtonClick())

        self.carrier_wave_type = self.carrier_type.currentText()
        self.carrier_type.currentIndexChanged.connect(lambda: self.carrier_type_change())

    '''
        Essa função retorna o áudio captado pelo período de tempo especificado
    '''
    def getMicAudio(self):
        # audio, fs = sf.read('../audio/generated_4f978.wav')
        print("Microfone gravando... ")
        audio = sd.rec(self.recordDuration * self.fs)
        # sd.wait()
        print("Pronto... ")
        audio = audio[:, 0]
        # sd.play(audio, fs)
        # sd.wait()
        return audio

    '''
        Chamada toda vez que usuário clicar no botão `GRAVAR` da interface gráfica
        A função escuta o audio transmitido e plota-o em fourier. 
        
        Em seguida, faz a demodulação do sinal, recuperando as duas mensagens transmitidas.
        Essas mensagens são salvas em dois arquivos .wav e tocadas logo em seguida
        
        TODO: criar a interface com o botão e chamar essa função toda vez que ele for clicado
    '''
    def onRecordButtonClick(self):
        if (len(str(self.f1)) == 0 or len(str(self.f2)) == 0):
            self.console("Defina as frequências das portadoras")
            return
        
        recordedAudio = self.getMicAudio()
        # self.saveFile(recordedAudio, "recebido")
        self.plotTimeSignal(recordedAudio, self.widget_modulated_received_time)
        self.plotFourierSignal(recordedAudio, self.widget_modulated_received_freq)
        msg1, msg2 = self.applyDemodulation(recordedAudio)

        self.plotTimeSignal(msg1, self.widget_audio_1_time)
        self.plotFourierSignal(msg1, self.widget_audio_1_freq)

        self.plotTimeSignal(msg2, self.widget_audio_2_time)
        self.plotFourierSignal(msg2, self.widget_audio_2_freq)

        self.saveFile(msg1, 'message_1')
        self.saveFile(msg2, 'message_2')

        self.playMsg(msg1, 'Tocando mensagem 1')
        self.playMsg(msg2, 'Tocando mensagem 2')

    '''
        Plote o sinal em fourier
    '''
    def plotFourierSignal(self, signal, widget):
        fourierData = self.FFT(signal)
        a = abs(fourierData)
        widget.clear()
        widget.plot(a, pen=self.pen)

    '''
        Plote o sinal no tempo
    '''
    def plotTimeSignal(self, signal, widget):
        widget.clear()
        widget.plot(signal, pen=self.pen)

    ''' 
        Retorna a transformada de Fourier de um sinal
    '''
    def FFT(self, data):
        from scipy.fftpack import fft
        N = len(data)
        fourier_data = fft(data)
        return fourier_data[0:N // 2]

    '''
        Retorna as duas mensagens originais, aplicando a demulação do sinal recebido
    '''
    def applyDemodulation(self, modulatedSignal):
        self.console("Aplicando a demodulação...")

        t = np.linspace(0, self.periodo, self.fs * self.recordDuration)
        np_wave = np.cos if self.carrier_wave_type == 'Cosine' else np.sin

        carrier1 = np_wave(2 * np.pi * self.f1 * t)
        carrier2 = np_wave(2 * np.pi * self.f2 * t)

        demodulated1 = np.multiply(modulatedSignal, carrier1)
        demodulated2 = np.multiply(modulatedSignal, carrier2)

        msg1 = self.LPF(demodulated1, 2000, self.fs)
        msg2 = self.LPF(demodulated2, 2000, self.fs)
        return msg1, msg2
    
    '''
        Aplica o filtro passa baixa
    '''
    def LPF(self, signal, cutoff_hz, fs):
        #####################
        # Filtro
        #####################
        # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html
        nyq_rate = fs / 2
        width = 5.0 / nyq_rate
        ripple_db = 60.0  # dB
        N, beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, cutoff_hz / nyq_rate, window=('kaiser', beta))
        return(sg.lfilter(taps, 1.0, signal))

    
    '''
        Salva as mensagens originais em arquivos .wav
    '''
    def saveFile(self, audio, msgId):
        self.console("Salvando mensagem original")
        filePath = "./audio/" + "received_" + msgId + ".wav"
        self.console(filePath)
        sf.write(filePath, audio, self.fs)

    
    def frequency_change(self, version):
        if version == "1":
            self.f1 = int(self.input_freq1.text())
        else:
            self.f2 = int(self.input_freq2.text())

    def carrier_type_change(self):
        self.carrier_wave_type = self.carrier_type.currentText()

    def console(self, text):
        item = QtGui.QListWidgetItem()
        item.setText(text)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.console_display.addItem(item)

    def cleanConsole(self):
        self.console_display.clear()


    def playMsg(self, msg, logOutput):
        self.console(logOutput)
        sd.play(msg, self.fs)
        sd.wait()

if __name__ == "__main__":
    fs = 44100
    # sound device setup
    sd.default.samplerate = fs
    sd.default.channels = 1


    app = QtGui.QApplication(sys.argv)
    window = Receiver()
    window.show()
    app.exec_()
