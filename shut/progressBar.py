from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import os
from threading import Thread
import sys, time 
from PyQt5.QtWidgets import QApplication, QDialog,QPushButton,QProgressBar,QTextEdit,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread

#from time import sleep



class ProgressBarThread(QThread):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow
        
    def run(self):

        for i in range(101): 
            self.mainwindow.progressbar.setValue(i)
            print(i)
            time.sleep(0.3)
        



class Ui_Form(object):
    def setupUi(self, Form):

        Form.setObjectName("Form")
        Form.resize(350, 210)
        Form.setFixedSize(350,210)
        Form.setWindowTitle("Shut")

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.insert(str(10))
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setClearButtonEnabled(True)
        self.lineEdit.setPlaceholderText("от 0 до 99 ")
        reg = QRegExp("[0-9]{2}")
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)  
            
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 100, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.launch_progress_bar_filling)
        self.pushButton.setText("Thread")

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(200, 20, 100, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.ProgressBarf)
        self.pushButton.setText("ProgressBar")
               
        self.ProgressbarThread_instance = ProgressBarThread(mainwindow=self)

        self.progressbar = QProgressBar(Form)
        self.progressbar.setAlignment(Qt.AlignCenter)
        self.progressbar.setGeometry(QtCore.QRect(5, 155, 340, 15))

        self.progressbar1 = QProgressBar(Form)
        self.progressbar1.setAlignment(Qt.AlignCenter)
        self.progressbar1.setGeometry(QtCore.QRect(5, 120, 340, 15))



    def ProgressBarf(self):
        for i in range(101): 
            self.progressbar1.setValue(i)
            print(i)
            time.sleep(0.2)
         

             

    def launch_progress_bar_filling(self):
        self.ProgressbarThread_instance.start()




    



   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    
