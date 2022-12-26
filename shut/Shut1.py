# -*- coding: utf-8 -*-

#pyuic5 -x Shut1.ui -o Shut1.py

# Form implementation generated from reading ui file 'Shut1.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.



from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIntValidator,QRegExpValidator
from PyQt5.QtCore import QRegExp
import os
from threading import Thread
import sys, time 
from PyQt5.QtWidgets import QMessageBox, QApplication, QDialog,QPushButton,QProgressBar,QTextEdit,QVBoxLayout,QMainWindow
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread
#from time import sleep


'''
class ProgressBarThread(QThread,QtWidgets,QMainWindow,QMainWindow):
    def __init__(self, mainwindow):
        super().__init__()
        self.mainwindow = mainwindow

        
    
    def run(self):

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
        
        self.lineEdit.setValidator(pValidator)

        d = self.lineEdit.text()
        for i in range(100):
            
            print(i)
            self.mainwindow.progressbar.setValue(i)
            print(i)
            time.sleep(0.3) 
'''

class Ui_Form(object):
    def setupUi(self, Form):
        
        Form.setObjectName("Form")
        Form.resize(350, 210)
        Form.setFixedSize(350,210)
        #self.title = ("f")

        #Shut_Down////////////////////////////////////////////////////////////////////////////////////////////Shut_Down

        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(10, 20, 100, 25))
        self.pushButton.setObjectName("pushButton")

        self.pushButton.clicked.connect(self.Shut_Down1)
        self.pushButton.clicked.connect(self.launch_progress_bar_filling2)

        #Shut_Down////////////////////////////////////////////////////////////////////////////////////////////Shut_Down

        #self.pushButton.clicked.connect(self.Cancelsh)
        #self.pushButton.clicked.connect(self.t1)

        #self.ProgressbarThread_instance = ProgressBarThread(mainwindow=self)
        

                    #Cancelsh

        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(125, 10, 100, 40))
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.Cancelsh)
        #self.pushButton_2.clicked.start()



#Restarbt////////////////////////////////////////////////////////////////////////////////////////////Restarbt
                    #Restarbt

        self.pushButton_3 = QtWidgets.QPushButton(Form)
        self.pushButton_3.setGeometry(QtCore.QRect(240, 20, 100, 25))
        self.pushButton_3.setObjectName("pushButton_3")

        self.pushButton_3.clicked.connect(self.Restarbt)
        self.pushButton_3.clicked.connect(self.launch_progress_bar_filling2)

#Restarbt////////////////////////////////////////////////////////////////////////////////////////////Restarbt

                    #exit1

        self.pushButton_4 = QtWidgets.QPushButton(Form)
        self.pushButton_4.setGeometry(QtCore.QRect(125, 180, 100, 25))
        self.pushButton_4.setObjectName("pushButton_4")

        self.pushButton_4.clicked.connect(self.SMMMS)
        



        
        self.checkBox = QtWidgets.QCheckBox(Form)
        self.checkBox.setGeometry(QtCore.QRect(100, 60, 70, 17))
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(Form)
        self.checkBox_2.setGeometry(QtCore.QRect(100, 90, 70, 17))
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(Form)
        self.checkBox_3.setGeometry(QtCore.QRect(100, 120, 70, 17))
        self.checkBox_3.setObjectName("checkBox_3")

        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(10, 60, 82, 17))
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(Form)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 90, 82, 17))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(Form)
        self.radioButton_3.setGeometry(QtCore.QRect(10, 120, 82, 17))
        self.radioButton_3.setObjectName("radioButton_3")
        

                    #lineEdit

        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(190, 60, 113, 20))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.insert(str(int(5)))
        #self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus) #фокус есть или нету при нажатии на таб
        self.lineEdit.setClearButtonEnabled(True)
        #self.lineEdit.setMaxLength(3)
        #self.lineEdit.setInputMask("x" * 3)
        self.lineEdit.setPlaceholderText("от 0 до 99 ")
        #reg = QRegExp("[a-яА-Я0-9]{3}")
        reg = QRegExp("[0-9]{2}")
        pValidator = QRegExpValidator()
        pValidator.setRegExp(reg)        
        #pIntValidator = QIntValidator()
        #pIntValidator.setRange(0,60)
        #self.lineEdit.setValidator(pIntValidator)
        self.lineEdit.setValidator(pValidator)


                    #label

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(190, 130, 150, 25))
        self.label.setObjectName("label")
        self.label.setText("0")
        self.label.setFont(QtGui.QFont("Capsuula", 10))
        self.label.setStyleSheet("color: red;")



        self.comboBox = QtWidgets.QComboBox(Form)
        self.comboBox.setGeometry(QtCore.QRect(190, 90, 111, 20))
        self.comboBox.setObjectName("comboBox")
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

                    #progressbar

        self.progressbar = QProgressBar(Form)
        self.progressbar.setAlignment(Qt.AlignCenter)
        self.progressbar.setGeometry(QtCore.QRect(5, 155, 340, 15))

        

    

    def retranslateUi(self, Form):

        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Shut"))

        self.pushButton.setText(_translate("Form", "Shut Down"))
        self.pushButton_2.setText(_translate("Form", "Cancel"))
        self.pushButton_3.setText(_translate("Form", "Restar"))
        self.pushButton_4.setText(_translate("Form", "Exit"))
        self.checkBox.setText(_translate("Form", "CheckBox"))
        self.checkBox_2.setText(_translate("Form", "CheckBox"))
        self.checkBox_3.setText(_translate("Form", "CheckBox"))
        self.radioButton.setText(_translate("Form", "RadioButton"))
        self.radioButton_2.setText(_translate("Form", "RadioButton"))
        self.radioButton_3.setText(_translate("Form", "RadioButton"))


    def Cancelsh(self):
        #os.system("shutdown -a")
        print("Stop")
        self.label.setText("Stop")
        print("Cancel")

          
#Shut_Down1////////////////////////////////////////////////////////////////////////////////////////////Shut_Down1
    def Shut_Down1(self):
        d = self.lineEdit.text()
        
        if d == str():
            msg = QMessageBox()
            msg.setWindowTitle("Info")
            msg.setText("Поле ввода пустое приравнивается к нулю")
            msg.setIcon(QMessageBox.Question)
            msg.setStandardButtons(QMessageBox.Ok )
            x = msg.exec_()

            if x == QMessageBox.Ok:
                self.lineEdit.insert(str(int(0)))

        d = str(int(0))

        self.label.setText("Shutdown %s sec" % d)
        #os.system("shutdown -f -s -t %s" % d)
        


    def launch_progress_bar_filling2(self):
       
        d = self.lineEdit.text()
        self.label.setText("%s sec" % d)
        
        if d == str():
            d = str(0)
            self.label.setText("%s sec" % d)
            
        d=int(d)
        
        print(type(d))
        
        for i in range(101):
            t = 1
            t=d/100
            self.progressbar.setValue(i)
            time.sleep(t) 

#Shut_Down1////////////////////////////////////////////////////////////////////////////////////////////Shut_Down1




#Restarbt////////////////////////////////////////////////////////////////////////////////////////////Restarbt
    def Restarbt(self):
        d = self.lineEdit.text()
        if d == str():
            d = str(int(0))
            self.label.setText("Restar %s sec" % d)
            #os.system("shutdown -f -r -t %s" % d)
            
#Restarbt////////////////////////////////////////////////////////////////////////////////////////////Restarbt    

    


    def SMMMS(self):
        print('Exit')

        self.label.setText("Exit")

        Form.update()
        msg = QMessageBox()
        msg.setWindowTitle("Close")
        msg.setText("Do you really want to close the application")
        msg.setIcon(QMessageBox.Question)
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        #msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Retry | QMessageBox.Cancel)
        msg.setInformativeText("Press Ok to close the program or Cancel to quit")
        x = msg.exec_()

        if x == QMessageBox.Ok:
            exit()
        else:
            self.label.setText("Welcome")

       

        #msg = QMessageBox()
        #msg.exec_()

        #print("gf")
        #self.pushButton.setText("123")



    
            
            

    #self.thead = QThread()
    #self.thead.started.connect(self.Shut_Down())
    #self.thead.start()
       

   
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
    