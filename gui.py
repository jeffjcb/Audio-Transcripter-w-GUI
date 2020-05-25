from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
import speech_recognition as sr
import os
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 473)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.transcript = QtWidgets.QPushButton(self.centralwidget)
        self.transcript.setGeometry(QtCore.QRect(50, 100, 131, 41))
        self.transcript.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.transcript.setObjectName("transcript")
        self.transcript.clicked.connect(self.speech)

        self.choose_a_file = QtWidgets.QPushButton(self.centralwidget)
        self.choose_a_file.setGeometry(QtCore.QRect(50, 40, 131, 41))
        self.choose_a_file.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.choose_a_file.setObjectName("choose_a_file")
        self.choose_a_file.clicked.connect(self.open_dialog_box)

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(230, 40, 521, 351))
        font = QtGui.QFont()
        font.setFamily("Yu Gothic UI Semilight")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setCursor(QtGui.QCursor(QtCore.Qt.IBeamCursor))
        self.label.setAutoFillBackground(False)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setLineWidth(6)
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label.setObjectName("label")

        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setGeometry(QtCore.QRect(50, 160, 131, 41))
        self.save.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.save.setObjectName("save")
        self.save.clicked.connect(self.saves)

        self.mic = QtWidgets.QPushButton(self.centralwidget)
        self.mic.setGeometry(QtCore.QRect(50, 220, 131, 41))
        self.mic.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.mic.setObjectName("Microphone")
        self.mic.clicked.connect(self.speak)

        self.exit_button = QtWidgets.QPushButton(self.centralwidget)
        self.exit_button.setGeometry(QtCore.QRect(50, 280, 131, 31))
        self.exit_button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.exit_button.setObjectName("exit_button")
        self.exit_button.clicked.connect(self.escape)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.r = sr.Recognizer()

    def open_dialog_box(self):
        filename = QFileDialog.getOpenFileName()
        self.path = str(filename[0])
        self.name = os.path.basename(self.path)
        self.choose_a_file.setText("Choose a file: " + self.name)

    def speech(self):
        try:
            with sr.AudioFile(self.path) as self.source:
                self.audio = self.r.record(self.source)
            print("System Output:"+self.r.recognize_google(self.audio))
            self.label.setText(self.r.recognize_google(self.audio))
        except Exception:
            print("Something went wrong.")

    def escape(self):
        sys.exit()

    def saves(self):
        outF = open("myOutFile.txt", "w")
        outF.writelines(self.r.recognize_google(self.audio))
        outF.close()

    def speak(self):
        with sr.Microphone() as src:
            self.r.adjust_for_ambient_noise(src)
            print("Listening...")
            audio = self.r.listen(src)
            print("Recognizing...")
        try:
            self.label.setText(self.r.recognize_google(audio))
        except Exception:
            self.label.setText("Something went wrong.")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Audio Transcripter"))
        self.transcript.setText(_translate("MainWindow", "Transcript"))
        self.choose_a_file.setText(_translate("MainWindow", "Choose a file"))
        self.label.setText(_translate("MainWindow", " "))
        self.save.setText(_translate("MainWindow", "Save"))
        self.mic.setText(_translate("MainWindow", "Microphone"))
        self.exit_button.setText(_translate("MainWindow", "Exit"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
