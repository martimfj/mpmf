# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'receiver_ui.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1020, 740)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(1020, 740))
        MainWindow.setMaximumSize(QtCore.QSize(1020, 740))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(1020, 740))
        self.centralwidget.setMaximumSize(QtCore.QSize(1020, 740))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.bg_window = QtGui.QLabel(self.centralwidget)
        self.bg_window.setEnabled(True)
        self.bg_window.setGeometry(QtCore.QRect(0, 0, 1020, 740))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bg_window.sizePolicy().hasHeightForWidth())
        self.bg_window.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Open Sans"))
        self.bg_window.setFont(font)
        self.bg_window.setText(_fromUtf8(""))
        self.bg_window.setPixmap(QtGui.QPixmap(_fromUtf8("img/mainwindow_receiver_bg.PNG")))
        self.bg_window.setObjectName(_fromUtf8("bg_window"))
        self.carrier_type = QtGui.QComboBox(self.centralwidget)
        self.carrier_type.setGeometry(QtCore.QRect(186, 400, 115, 25))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.carrier_type.sizePolicy().hasHeightForWidth())
        self.carrier_type.setSizePolicy(sizePolicy)
        self.carrier_type.setObjectName(_fromUtf8("carrier_type"))
        self.carrier_type.addItem(_fromUtf8(""))
        self.carrier_type.addItem(_fromUtf8(""))
        self.button_save = QtGui.QPushButton(self.centralwidget)
        self.button_save.setEnabled(True)
        self.button_save.setGeometry(QtCore.QRect(326, 400, 75, 25))
        self.button_save.setObjectName(_fromUtf8("button_save"))
        self.button_play = QtGui.QPushButton(self.centralwidget)
        self.button_play.setEnabled(True)
        self.button_play.setGeometry(QtCore.QRect(326, 435, 75, 25))
        self.button_play.setObjectName(_fromUtf8("button_play"))
        self.input_freq1 = QtGui.QLineEdit(self.centralwidget)
        self.input_freq1.setGeometry(QtCore.QRect(80, 400, 80, 25))
        self.input_freq1.setObjectName(_fromUtf8("input_freq1"))
        self.input_freq2 = QtGui.QLineEdit(self.centralwidget)
        self.input_freq2.setGeometry(QtCore.QRect(80, 435, 80, 25))
        self.input_freq2.setObjectName(_fromUtf8("input_freq2"))
        self.widget_modulated_received_time = PlotWidget(self.centralwidget)
        self.widget_modulated_received_time.setGeometry(QtCore.QRect(25, 25, 400, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_modulated_received_time.sizePolicy().hasHeightForWidth())
        self.widget_modulated_received_time.setSizePolicy(sizePolicy)
        self.widget_modulated_received_time.setObjectName(_fromUtf8("widget_modulated_received_time"))
        self.widget_modulated_received_freq = PlotWidget(self.centralwidget)
        self.widget_modulated_received_freq.setGeometry(QtCore.QRect(25, 200, 400, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_modulated_received_freq.sizePolicy().hasHeightForWidth())
        self.widget_modulated_received_freq.setSizePolicy(sizePolicy)
        self.widget_modulated_received_freq.setObjectName(_fromUtf8("widget_modulated_received_freq"))
        self.widget_modulated_1_time = PlotWidget(self.centralwidget)
        self.widget_modulated_1_time.setGeometry(QtCore.QRect(450, 25, 260, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_modulated_1_time.sizePolicy().hasHeightForWidth())
        self.widget_modulated_1_time.setSizePolicy(sizePolicy)
        self.widget_modulated_1_time.setObjectName(_fromUtf8("widget_modulated_1_time"))
        self.widget_modulated_1_freq = PlotWidget(self.centralwidget)
        self.widget_modulated_1_freq.setGeometry(QtCore.QRect(450, 200, 260, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_modulated_1_freq.sizePolicy().hasHeightForWidth())
        self.widget_modulated_1_freq.setSizePolicy(sizePolicy)
        self.widget_modulated_1_freq.setObjectName(_fromUtf8("widget_modulated_1_freq"))
        self.widget_modulated_2_time = PlotWidget(self.centralwidget)
        self.widget_modulated_2_time.setGeometry(QtCore.QRect(735, 25, 260, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_modulated_2_time.sizePolicy().hasHeightForWidth())
        self.widget_modulated_2_time.setSizePolicy(sizePolicy)
        self.widget_modulated_2_time.setObjectName(_fromUtf8("widget_modulated_2_time"))
        self.widget_modulated_2_freq = PlotWidget(self.centralwidget)
        self.widget_modulated_2_freq.setGeometry(QtCore.QRect(735, 200, 260, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_modulated_2_freq.sizePolicy().hasHeightForWidth())
        self.widget_modulated_2_freq.setSizePolicy(sizePolicy)
        self.widget_modulated_2_freq.setObjectName(_fromUtf8("widget_modulated_2_freq"))
        self.widget_audio_1_time = PlotWidget(self.centralwidget)
        self.widget_audio_1_time.setGeometry(QtCore.QRect(450, 390, 260, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_audio_1_time.sizePolicy().hasHeightForWidth())
        self.widget_audio_1_time.setSizePolicy(sizePolicy)
        self.widget_audio_1_time.setObjectName(_fromUtf8("widget_audio_1_time"))
        self.widget_audio_2_freq = PlotWidget(self.centralwidget)
        self.widget_audio_2_freq.setGeometry(QtCore.QRect(735, 565, 260, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_audio_2_freq.sizePolicy().hasHeightForWidth())
        self.widget_audio_2_freq.setSizePolicy(sizePolicy)
        self.widget_audio_2_freq.setObjectName(_fromUtf8("widget_audio_2_freq"))
        self.widget_audio_2_time = PlotWidget(self.centralwidget)
        self.widget_audio_2_time.setGeometry(QtCore.QRect(735, 390, 260, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_audio_2_time.sizePolicy().hasHeightForWidth())
        self.widget_audio_2_time.setSizePolicy(sizePolicy)
        self.widget_audio_2_time.setObjectName(_fromUtf8("widget_audio_2_time"))
        self.widget_audio_1_freq = PlotWidget(self.centralwidget)
        self.widget_audio_1_freq.setGeometry(QtCore.QRect(450, 565, 260, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_audio_1_freq.sizePolicy().hasHeightForWidth())
        self.widget_audio_1_freq.setSizePolicy(sizePolicy)
        self.widget_audio_1_freq.setObjectName(_fromUtf8("widget_audio_1_freq"))
        self.console_display = QtGui.QListWidget(self.centralwidget)
        self.console_display.setGeometry(QtCore.QRect(25, 470, 375, 245))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.console_display.sizePolicy().hasHeightForWidth())
        self.console_display.setSizePolicy(sizePolicy)
        self.console_display.setStyleSheet(_fromUtf8("background-color: rgb(0, 0, 0);\n"
"selection-background-color: rgb(0, 0, 0);\n"
"selection-color: rgb(0, 0, 0);\n"
"font: 8pt \"Consolas\";\n"
"color: rgb(0, 255, 0);"))
        self.console_display.setFrameShape(QtGui.QFrame.NoFrame)
        self.console_display.setFrameShadow(QtGui.QFrame.Plain)
        self.console_display.setLineWidth(0)
        self.console_display.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.console_display.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.console_display.setAutoScrollMargin(50)
        self.console_display.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.console_display.setProperty("showDropIndicator", False)
        self.console_display.setAlternatingRowColors(False)
        self.console_display.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.console_display.setSelectionBehavior(QtGui.QAbstractItemView.SelectItems)
        self.console_display.setTextElideMode(QtCore.Qt.ElideNone)
        self.console_display.setVerticalScrollMode(QtGui.QAbstractItemView.ScrollPerItem)
        self.console_display.setFlow(QtGui.QListView.TopToBottom)
        self.console_display.setProperty("isWrapping", False)
        self.console_display.setResizeMode(QtGui.QListView.Adjust)
        self.console_display.setLayoutMode(QtGui.QListView.Batched)
        self.console_display.setViewMode(QtGui.QListView.ListMode)
        self.console_display.setModelColumn(0)
        self.console_display.setUniformItemSizes(True)
        self.console_display.setObjectName(_fromUtf8("console_display"))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.carrier_type.setToolTip(_translate("MainWindow", "Choose the type of wave of the carrier", None))
        self.carrier_type.setItemText(0, _translate("MainWindow", "Cosine", None))
        self.carrier_type.setItemText(1, _translate("MainWindow", "Sine", None))
        self.button_save.setToolTip(_translate("MainWindow", "Save files", None))
        self.button_save.setText(_translate("MainWindow", "Save", None))
        self.button_play.setToolTip(_translate("MainWindow", "Reproduce resulting modulated signal", None))
        self.button_play.setText(_translate("MainWindow", "Play", None))

from pyqtgraph import PlotWidget
