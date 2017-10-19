# -*- coding: utf-8 -*-
from PyQt4 import QtGui,QtCore
import pyqtgraph as pg
import pyqtgraph.exporters
import numpy as np
import soundfile as sf
import sounddevice as sd
import sys
import os
import transmitter_ui
import webbrowser

class Transmitter(QtGui.QMainWindow, transmitter_ui. Ui_MainWindow):
    def __init__(self, parent=None):
        super(Transmitter, self).__init__(parent)
        self.setupUi(self)
        self.pen = pyqtgraph.mkPen(color='g')
        self.fs = 44100
        self.fl = None
        self.periodo = 1
        self.duration = 3
        self.batch_name = None
        self.fc_1 = self.spin_freq_1.value()
        self.fc_2 = self.spin_freq_2.value()
        self.carrier_1 = self.carrier_type_1.currentText()
        self.carrier_2 = self.carrier_type_2.currentText()
        self.message_1 = None
        self.message_2 = None
        self.cut_freq = 4000
        self.modulatedTime1 = None
        self.modulatedTime2 = None
        self.ultimateaudio = None
        # Variables

        #Audio 1 - Time
        self.widget_audio1_time.setLabel("left", "Amplitude")
        self.widget_audio1_time.setLabel("bottom", "Time", "seconds")
        self.widget_audio1_time.setMouseEnabled(y = False)
        self.widget_audio1_time.showGrid(True, True, 0.5)

        #Audio 1 - Frequency
        self.widget_audio1_freq.setLabel("left", "Amplitude")
        self.widget_audio1_freq.setLabel("bottom", "Frequency", "hertz")
        self.widget_audio1_freq.setMouseEnabled(y = False)
        self.widget_audio1_freq.setRange(xRange=(0,10000),yRange=(0,10000))
        self.widget_audio1_freq.showGrid(True, True, 0.5)

        #Audio 2 - Time
        self.widget_audio2_time.setLabel("left", "Amplitude")
        self.widget_audio2_time.setLabel("bottom", "Time", "seconds")
        self.widget_audio2_time.setMouseEnabled(y = False)
        self.widget_audio2_time.showGrid(True, True, 0.5)

        #Audio 2 - Frequency
        self.widget_audio2_freq.setLabel("left", "Amplitude")
        self.widget_audio2_freq.setLabel("bottom", "Frequency", "hertz")
        self.widget_audio2_freq.setMouseEnabled(y = False)
        self.widget_audio2_freq.showGrid(True, True, 0.5)

        #Carrier 1 - Time
        self.widget_carrier1_time.setLabel("left", "Amplitude")
        self.widget_carrier1_time.setLabel("bottom", "Time", "seconds")
        self.widget_carrier1_time.setMouseEnabled(y = False)
        self.widget_carrier1_time.showGrid(True, True, 0.5)

        #Carrier 1 - Frequency
        self.widget_carrier1_freq.setLabel("left", "Amplitude")
        self.widget_carrier1_freq.setLabel("bottom", "Frequency", "hertz")
        self.widget_carrier1_freq.setMouseEnabled(y = False)
        self.widget_carrier1_freq.showGrid(True, True, 0.5)

        #Carrier 2 - Time
        self.widget_carrier2_time.setLabel("left", "Amplitude")
        self.widget_carrier2_time.setLabel("bottom", "Time", "seconds")
        self.widget_carrier2_time.setMouseEnabled(y = False)
        self.widget_carrier2_time.showGrid(True, True, 0.5)

        #Carrier 2 - Frequency
        self.widget_carrier2_freq.setLabel("left", "Amplitude")
        self.widget_carrier2_freq.setLabel("bottom", "Frequency", "hertz")
        self.widget_carrier2_freq.setMouseEnabled(y = False)
        self.widget_carrier2_freq.showGrid(True, True, 0.5)

        #Modulated Signal 1 - Time
        self.widget_modsig1_time.setLabel("left", "Amplitude")
        self.widget_modsig1_time.setLabel("bottom", "Time", "seconds")
        self.widget_modsig1_time.setMouseEnabled(y = False)
        self.widget_modsig1_time.showGrid(True, True, 0.5)

        #Modulated Signal 1 - Frequency
        self.widget_modsig1_freq.setLabel("left", "Amplitude")
        self.widget_modsig1_freq.setLabel("bottom", "Frequency", "hertz")
        self.widget_modsig1_freq.setMouseEnabled(y = False)
        self.widget_modsig1_freq.showGrid(True, True, 0.5)

        #Modulated Signal 2 - Time
        self.widget_modsig2_time.setLabel("left", "Amplitude")
        self.widget_modsig2_time.setLabel("bottom", "Time", "seconds")
        self.widget_modsig2_time.setMouseEnabled(y = False)
        self.widget_modsig2_time.showGrid(True, True, 0.5)

        #Modulated Signal 2 - Frequency
        self.widget_modsig2_freq.setLabel("left", "Amplitude")
        self.widget_modsig2_freq.setLabel("bottom", "Frequency", "hertz")
        self.widget_modsig2_freq.setMouseEnabled(y = False)
        self.widget_modsig2_freq.showGrid(True, True, 0.5) 

        #Resulting Modulated Signal - Time
        self.widget_modsigf_time.setLabel("left", "Amplitude")
        self.widget_modsigf_time.setLabel("bottom", "Time", "seconds")
        self.widget_modsigf_time.setMouseEnabled(y = False)
        self.widget_modsigf_time.showGrid(True, True, 0.5)

        #Resulting Modulated Signal - Frequency
        self.widget_modsigf_freq.setLabel("left", "Amplitude")
        self.widget_modsigf_freq.setLabel("bottom", "Frequency", "hertz")
        self.widget_modsigf_freq.setMouseEnabled(y = False)
        self.widget_modsigf_freq.showGrid(True, True, 0.5) 

        #Documentation Link
        self.link_to_docs.clicked.connect(lambda: webbrowser.open('https://github.com/martimfj/mpmf/tree/master/7-Modulacao-AM'))

        #Load File Button
        self.button_load_1.clicked.connect(lambda: self.loadFile("1"))
        self.button_load_2.clicked.connect(lambda: self.loadFile("2"))

        self.button_record_1.clicked.connect(lambda: self.recordMic("1"))
        self.button_record_2.clicked.connect(lambda: self.recordMic("2"))

        self.spin_freq_1.valueChanged.connect(lambda: self.spin_change("1"))
        self.spin_freq_2.valueChanged.connect(lambda: self.spin_change("2"))

        self.carrier_type_1.currentIndexChanged.connect(lambda: self.carrier_type_change("1"))
        self.carrier_type_2.currentIndexChanged.connect(lambda: self.carrier_type_change("2"))

        # Starts disabled until some audio is loaded
        self.spin_freq_1.setEnabled(False)
        self.carrier_type_1.setEnabled(False)

        self.spin_freq_2.setEnabled(False)
        self.carrier_type_2.setEnabled(False)

        self.button_play.clicked.connect(lambda: self.playSound(self.ultimateaudio))

    #Functions
    def console(self, text):
        item = QtGui.QListWidgetItem()
        item.setText(text)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.console_display.addItem(item)
        
    def cleanConsole(self):
        self.console_display.clear()

    def loadFile(self, version):
        directory = os.getcwd()
        fileLocation = QtGui.QFileDialog.getOpenFileName(self, 'Open file', directory, "WAVE Files (*.wav)")
        path, fileName = os.path.split(fileLocation)

        if version == "1":
            self.message_1, self.fl = sf.read(fileLocation)
            self.message_1 = self.LPF(self.message_1, self.cut_freq, self.fl)
            self.plotDataTime(self.message_1, version)
            self.plotCarrierTime(self.createCarrierWave("1"), "1")
            self.console("Audio {1} File Loaded from: {0}".format(fileLocation, version))
        else:
            self.message_2, self.fl = sf.read(fileLocation)
            self.message_2 = self.LPF(self.message_2, self.cut_freq, self.fl)
            self.plotDataTime(self.message_2, version)
            self.plotCarrierTime(self.createCarrierWave("2"), "2")
            self.console("Audio {1} File Loaded from: {0}".format(fileLocation, version))
            
    def plotDataTime(self, data, version):
        if version == "1":
            self.widget_audio1_time.clear()
            #self.widget_audio1_time.setRange(xRange=(100,600),yRange=(-2,2))
            self.widget_audio1_time.plot(data, pen=self.pen)
            self.plotDataFrequency(data, version)
            self.spin_freq_1.setEnabled(True)
            self.carrier_type_1.setEnabled(True)
        else:
            self.widget_audio2_time.clear()
            #self.widget_audio2_time.setRange(xRange=(100,600),yRange=(-2,2))
            self.widget_audio2_time.plot(data, pen=self.pen)
            self.plotDataFrequency(data, version)
            self.spin_freq_2.setEnabled(True)
            self.carrier_type_2.setEnabled(True)

    def plotDataFrequency(self, data, version):
        if version == "1":
            self.widget_audio1_freq.clear()
            #self.widget_audio1_time.setRange(xRange=(100,600),yRange=(-2,2))
            audio_fft = abs(self.FFT(data))
            self.widget_audio1_freq.plot(audio_fft, pen=self.pen)
        else:
            self.widget_audio2_freq.clear()
            #self.widget_audio1_time.setRange(xRange=(100,600),yRange=(-2,2))
            audio_fft = abs(self.FFT(data))
            self.widget_audio2_freq.plot(audio_fft, pen=self.pen)

    def FFT(self, data):
        from scipy.fftpack import fft
        N = len(data)
        fourier_data = fft(data)
        return fourier_data[0:N // 2]

    def recordMic(self, version):
        self.console("Mic recording for 3 seconds")
        audio = sd.rec(self.duration * self.fs, channels = 1)
        sd.wait()
        self.console("Recording is over.")
        y = audio[:,0]

        if version == "1":
            self.message_1 = self.LPF(y, self.cut_freq, self.fs)
            self.plotCarrierTime(self.createCarrierWave(version), version)
            self.plotDataTime(self.message_1, version)
        else:
            self.message_2 = self.LPF(y, self.cut_freq, self.fs)
            self.plotCarrierTime(self.createCarrierWave(version), version)
            self.plotDataTime(self.message_2, version)

        # import uuid
        # unique = uuid.uuid4()
        # filename = "recorded_" + str(unique)[:5] + "_{}.wav".format(type)
        # print(filename)
        # self.saveFile(filename, y)

    # def saveFile(self, fileName, audio):
    #     filePath = "./audio/" + "tone_" + str(fileName) + ".wav"
    #     sf.write(filePath, audio, self.fs)
    #     self.console("Tone {0} was saved as: {1}".format(fileName, filePath))

    def createCarrierWave(self, version):
        x = np.linspace(0, self.periodo, self.fs * self.duration)
        if self.carrier_1 == "Cosine":
            if version == "1":
                return np.cos(2 * np.pi *  self.fc_1 * x)
            else:
                return np.cos(2 * np.pi *  self.fc_2 * x)
        else:
            if version == "2":
                return np.sin(2 * np.pi *  self.fc_2 * x)
            else:
                return np.sin(2 * np.pi *  self.fc_1 * x)

    def plotCarrierTime(self, data, version):
        if version == "1":
            self.widget_carrier1_time.clear()
            self.widget_carrier1_time.setRange(xRange=(0,80),yRange=(-1,1))
            self.widget_carrier1_time.plot(data, pen=self.pen)
            self.plotCarrierFrequency(data, version)
            self.plotModulatedTime(self.message_1, data, version)
        else:
            self.widget_carrier2_time.clear()
            self.widget_carrier2_time.setRange(xRange=(0,80),yRange=(-1,1))
            self.widget_carrier2_time.plot(data, pen=self.pen)
            self.plotCarrierFrequency(data, version)
            self.plotModulatedTime(self.message_2, data, version)

    def plotCarrierFrequency(self, data, version):
        if version == "1":
            self.widget_carrier1_freq.clear()
            self.widget_carrier1_freq.setRange(xRange=(0,10000))
            audio_fft = abs(self.FFT(data))
            self.widget_carrier1_freq.plot(audio_fft, pen=self.pen)
        else:
            self.widget_carrier2_freq.clear()
            self.widget_carrier2_freq.setRange(xRange=(0,10000))
            audio_fft = abs(self.FFT(data))
            self.widget_carrier2_freq.plot(audio_fft, pen=self.pen)
    
    def spin_change(self, version):
        if version == "1":
            self.fc_1 = self.spin_freq_1.value()
            self.plotCarrierTime(self.createCarrierWave("1"), "1")
        else:
            self.fc_2 = self.spin_freq_2.value()
            self.plotCarrierTime(self.createCarrierWave("2"), "2")

    def carrier_type_change(self, version):
        if version == "1":
            self.carrier_1 = self.carrier_type_1.currentText()
            self.plotCarrierTime(self.createCarrierWave("1"), "1")

            index = self.carrier_type_2.findText(self.carrier_1)
            self.carrier_type_2.setCurrentIndex(index)

            self.carrier_2 = self.carrier_type_1.currentText()
            self.plotCarrierTime(self.createCarrierWave("2"), "2")

        if version == "2":
            self.carrier_2 = self.carrier_type_2.currentText()
            self.plotCarrierTime(self.createCarrierWave("2"), "2")

            index = self.carrier_type_1.findText(self.carrier_2)
            self.carrier_type_1.setCurrentIndex(index)

            self.carrier_1 = self.carrier_type_2.currentText()
            self.plotCarrierTime(self.createCarrierWave("1"), "1")

    def plotModulatedTime(self, data, carrier, version):
        if version == "1":
            self.modulatedTime1 = data * carrier
            self.widget_modsig1_time.clear()
            self.widget_modsig1_time.setRange(xRange=(0,80),yRange=(-1,1))
            self.widget_modsig1_time.plot(self.modulatedTime1, pen=self.pen)
            self.plotModulatedFrequency(self.modulatedTime1, version)
            
        else:
            self.modulatedTime2 = data * carrier
            self.widget_modsig2_time.clear()
            self.widget_modsig2_time.setRange(xRange=(0,80),yRange=(-1,1))
            self.widget_modsig2_time.plot(self.modulatedTime2, pen=self.pen)
            self.plotModulatedFrequency(self.modulatedTime2, version)

    def plotModulatedFrequency(self, data, version):
        if version == "1":
            self.widget_modsig1_freq.clear()
            self.widget_modsig1_freq.setRange(xRange=(0,10000))
            audio_fft = abs(self.FFT(data))
            self.widget_modsig1_freq.plot(audio_fft, pen=self.pen)
            self.ResultingModulated()
        else:
            self.widget_modsig2_freq.clear()
            self.widget_modsig2_freq.setRange(xRange=(0,10000))
            audio_fft = abs(self.FFT(data))
            self.widget_modsig2_freq.plot(audio_fft, pen=self.pen)
            self.ResultingModulated()

    def LPF(self, signal, cutoff_hz, fs):
        from scipy import signal as sg
        # https://scipy.github.io/old-wiki/pages/Cookbook/FIRFilter.html

        nyq_rate = fs/2
        width = 5.0/nyq_rate
        ripple_db = 60.0 #dB
        N , beta = sg.kaiserord(ripple_db, width)
        taps = sg.firwin(N, cutoff_hz/nyq_rate, window=('kaiser', beta))
        return( sg.lfilter(taps, 1.0, signal))

    def ResultingModulated(self):
        if  self.modulatedTime1 != None and self.modulatedTime2 != None:
            data = self.modulatedTime1 + self.modulatedTime2
            self.plotResultingModulatedTime(data)
        else:
            print("Ainda não tem dois audios")

    def plotResultingModulatedTime(self, data):
        self.widget_modsigf_time.clear()
        self.widget_modsigf_time.plot(data, pen=self.pen)
        self.plotResultingModulatedFrequency(data)
        self.ultimateaudio = data

    def plotResultingModulatedFrequency(self, data):
        self.widget_modsigf_freq.clear()
        audio_fft = abs(self.FFT(data))
        self.widget_modsigf_freq.plot(audio_fft, pen=self.pen)
        
    def playSound(self, data):
        if self.ultimateaudio != None:
            sd.play(data, self.fs)
            sd.wait()
        else:
            self.console("Segura ae campeão, você não gerou tudo ainda")


if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    window = Transmitter()
    window.show()
    app.exec_() 
