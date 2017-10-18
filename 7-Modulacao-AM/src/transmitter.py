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
        self.periodo = 1
        self.duration = 5
        self.batch_name = None
        self.fc_1 = self.spin_freq_1.value()
        self.fc_2 = self.spin_freq_2.value()
        self.carrier_1 = self.carrier_type_1.currentText()
        self.carrier_2 = self.carrier_type_2.currentText()
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

        self.plotCarrierTime(self.createCarrierWave("1"), "1")
        self.plotCarrierTime(self.createCarrierWave("2"), "2")


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
        self.console("Audio {1} File Loaded from: {0}".format(fileLocation, version))

        if version == "1":
            audio1_data, fs = sf.read(fileLocation)
            self.plotDataTime(audio1_data, version)
        else:
            audio2_data, fs = sf.read(fileLocation)
            self.plotDataTime(audio2_data, version)

    def plotDataTime(self, data, version):
        if version == "1":
            self.widget_audio1_time.clear()
            #self.widget_audio1_time.setRange(xRange=(100,600),yRange=(-2,2))
            self.widget_audio1_time.plot(data, pen=self.pen)
            self.plotDataFrequency(data, version)
        else:
            self.widget_audio2_time.clear()
            #self.widget_audio2_time.setRange(xRange=(100,600),yRange=(-2,2))
            self.widget_audio2_time.plot(data, pen=self.pen)
            self.plotDataFrequency(data, version)

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
        self.console("Mic recording for 5 seconds")
        audio = sd.rec(self.duration * self.fs, channels = 1)
        sd.wait()
        self.console("Recording is over.")
        y = audio[:,0]

        self.plotDataTime(y, version)

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
        x = np.linspace(0, self.periodo, self.fs * self.periodo)
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
        else:
            self.widget_carrier2_time.clear()
            self.widget_carrier2_time.setRange(xRange=(0,80),yRange=(-1,1))
            self.widget_carrier2_time.plot(data, pen=self.pen)
            self.plotCarrierFrequency(data, version)

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
            
            


if __name__=="__main__":
    app = QtGui.QApplication(sys.argv)
    window = Transmitter()
    window.show()
    app.exec_() 
