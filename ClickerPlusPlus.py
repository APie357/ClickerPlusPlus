import json
import sys
import clickerlib
from PyQt5 import QtGui, uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QLabel, QLineEdit, QPushButton, QStatusBar

def loadConfig():
    configFile = open('config.json', 'r')
    config = json.loads(configFile.read())
    configFile.close()
    return config

class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        uic.loadUi('mainWindow.ui', self)  # load the mainWindow.ui file

        self.setFixedSize(800, 600)  # Set fixed window size to be 800x600
        self.setWindowTitle('Clicker++')  # Set the title of the window to be 'Clicker++'
        self.setWindowIcon(QtGui.QIcon('./logo.png'))  # Set the logo to './logo.png'

        self.letter = self.findChild(QLineEdit, 'letter')  # Get the 'letter' QLineEdit element of GUI

        self.letter.setInputMask('X')  # Sets the input mask to only allow one char

        self.show()  # Makes the window be visible

app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()  # Executes the app
