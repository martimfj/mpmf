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

    #Functions

    def console(self, text):
        item = QtGui.QListWidgetItem()
        item.setText(text)
        item.setFlags(QtCore.Qt.NoItemFlags)
        self.console_display.addItem(item)
        
    def cleanConsole(self):
        self.console_display.clear()

    def loadFile(self, type):
        directory = os.getcwd()
        fileLocation = QtGui.QFileDialog.getOpenFileName(self, 'Open file', directory, "WAVE Files (*.wav)")
        path, fileName = os.path.split(fileLocation)
        self.console("Audio {1} File Loaded from: {0}".format(fileLocation, type))

        if type == "1":
            audio1_data, fs = sf.read(fileLocation)
            self.plotDataTime(audio1_data, type)
        else:
            audio2_data, fs = sf.read(fileLocation)
            self.plotDataTime(audio2_data, type)

    def plotDataTime(self, data, type):
        if type == "1":
            self.widget_audio1_time.clear()
            #self.widget_audio1_time.setRange(xRange=(100,600),yRange=(-2,2))
            self.widget_audio1_time.plot(data, pen=self.pen)
            self.plotDataFrequency(data, type)
        else:
            self.widget_audio2_time.clear()
            #self.widget_audio2_time.setRange(xRange=(100,600),yRange=(-2,2))
            self.widget_audio2_time.plot(data, pen=self.pen)
            self.plotDataFrequency(data, type)

    def plotDataFrequency(self, data, type):
        if type == "1":
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

    def recordMic(self, type):
        audio = sd.rec(1*self.fs, channels = 1)
        print ("Mic recording... ")
        sd.wait()
        y = audio[:,0]
        self.plotDataTime(y, type)

        import uuid
        filename = "recorded_{}_".format(type) + str(uuid.uuid4()) + ".wav"
        print(filename)
        self.saveFile(filename, y)


if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    window = Transmitter()
    window.show()
    app.exec_() 
