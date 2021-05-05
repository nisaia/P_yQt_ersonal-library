import sys

from PyQt5.QtWidgets import QWidget
from ui.settings_window import *
from utils.constants import STYLES_PATH
from os import listdir
from os.path import isfile, join

class SettingsView(QWidget):

    def __init__(self, parent):
        super().__init__(parent)

        self.ui = Ui_settings_window()
        self.ui.setupUi(self)

        self.ui.changeStyle_button.clicked.connect(self.changeStyle)

        for button in self.findChildren(QtWidgets.QPushButton):
            button.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))

        self.show()
    
    def updateStyles(self):
        self.ui.style_comboBox.clear()
        
        for file in listdir(STYLES_PATH):
            if isfile(join(STYLES_PATH, file)):
                self.ui.style_comboBox.addItem(file)

    def changeStyle(self):
        app = QtWidgets.QApplication.instance()
        currentStyle = self.ui.style_comboBox.currentText()
        with open(join(STYLES_PATH, currentStyle), 'r') as f:
            qss = f.read()
            app.setStyleSheet(qss)

        
                