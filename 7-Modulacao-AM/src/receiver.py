from PyQt4 import QtGui, QtCore
import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np
import soundfile as sf
import sounddevice as sd
from scipy import signal as sg
import sys
import os
import transmitter_ui
import webbrowser


'''
    Função responsável por receber as ondas de áudio transmitidas, demodula-las e salvar os sinais de áudio.
    Recebe como parâmetro as duas frequências das ondas portadoras usadas para transmitir os sinais.
'''
class Transmitter(QtGui.QMainWindow, transmitter_ui. Ui_MainWindow):
    def __init__(self, carrierFrequency1, carrierFrequency2, parent=None ):
        super(Transmitter, self).__init__(parent)
        
        self.fs = 44100
        self.f1 = carrierFrequency1
        self.f2 = carrierFrequency2
        self.periodo = 1
        self.recordDuration = 1 # in seconds

        self.onRecordButtonClick()

    '''
        Essa função retorna o áudio captado pelo período de tempo especificado
    '''
    def getMicAudio(self):
        audio = sd.rec(self.recordDuration * self.fs)
        print("Microfone gravando... ")
        sd.wait()
        print("Pronto... ")
        audio = audio[:, 0]
        sd.play(audio, 44100)
        sd.wait()
        return audio

    '''
        Chamada toda vez que usuário clicar no botão `GRAVAR` da interface gráfica
        A função escuta o audio transmitido e plota-o em fourier. 
        
        Em seguida, faz a demodulação do sinal, recuperando as duas mensagens transmitidas.
        Essas mensagens são salvas em dois arquivos .wav e tocadas logo em seguida
        
        TODO: criar a interface com o botão e chamar essa função toda vez que ele for clicado
    '''
    def onRecordButtonClick(self):
        recordedAudio = self.getMicAudio()
        self.plotFourierSignal(recordedAudio)
        msg1, msg2 = self.applyDemodulation(recordedAudio)

        print(msg1)

    def plotFourierSignal(self, signal):
        fourierData = self.FFT(signal)
        print("PLOT FOURIER HERE!")

    
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
        t = np.linspace(0, self.periodo, self.fs * self.periodo)
        carrier1 = modulatedSignal * np.sin(2 * np.pi * self.f1 * t)
        carrier2 = modulatedSignal * np.sin(2 * np.pi * self.f2 * t)

        demodulated1 = modulatedSignal * carrier1
        demodulated2 = modulatedSignal * carrier2

        msg1 = self.LPF(demodulated1, 4000, self.fs)
        msg2 = self.LPF(demodulated2, 4000, self.fs)

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



if __name__ == "__main__":
    fs = 44100
    # sound device setup
    sd.default.samplerate = fs
    sd.default.channels = 1


    app = QtGui.QApplication(sys.argv)
    window = Transmitter(44000, 50000)
    window.show()
    app.exec_()
