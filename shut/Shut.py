# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

#https://winitpro.ru/index.php/2018/10/15/komanda-shutdown-windows/

#http://it.kgsu.ru/Python_Qt/oglav5.html


from PyQt5 import QtCore, QtGui, QtWidgets
import sys


import os
import time


class Ui_Shut(object):
    def setupUi(self, Shut):
        Shut.setObjectName("Shut")
        Shut.resize(300, 80)
        Shut.setGeometry(200,200,500,80)
        Shut.setFixedSize(300,80)
        

        

        self.ShutDown = QtWidgets.QPushButton(Shut)
        self.ShutDown.setGeometry(QtCore.QRect(10, 10, 75, 23))
        self.ShutDown.setObjectName("ShutDown")

        self.Restarbtn = QtWidgets.QPushButton(Shut)
        self.Restarbtn.setGeometry(QtCore.QRect(190, 10, 75, 23))
        self.Restarbtn.setObjectName("Restarbtn")

        self.Cancel = QtWidgets.QPushButton(Shut)
        self.Cancel.setGeometry(QtCore.QRect(100, 10, 75, 23))
        self.Cancel.setObjectName("Cancel")

        self.lineEdit = QtWidgets.QLineEdit(Shut)
        self.lineEdit.setGeometry(QtCore.QRect(30, 50, 113, 20))
        self.lineEdit.setObjectName("lineEdit")

        #self.label = QLabel(self)
        #self.label.setAlignment(Qt.AlignBottom | Qt.AlignRight)


        #self.lineEdit.setText(str(0))
        #self.lineEdit.textChanged[str].connect(self.onChanged)
        #self.lineEdit.setText(str(20))
        #self.lineEdit.insert("text")
        self.lineEdit.insert(str(10))
        #self.lineEdit.textEdited.connect(self.ShutdownPC)


        #self.lineEdit.textChanged[str].connect(self.ShutdownPC)


        #self.lineEdit.setFont(font_12)
        self.lineEdit.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.lineEdit.setClearButtonEnabled(True)

        #self.lineEdit.setInputMask(a)


        self.retranslateUi(Shut)
        QtCore.QMetaObject.connectSlotsByName(Shut)


        self.Restarbtn.clicked.connect(self.Restarbt)
        self.ShutDown.clicked.connect(self.ShutdownPC)
        self.Cancel.clicked.connect(self.Cancelsh)
     
        


    def ShutdownPC(self,text):

        d = self.lineEdit.text()
        print(d)
        
        os.system("shutdown -f -s -t %s" % d)
        #os.system("shutdown -r -t %s" % d)
        #os.system("shutdown -a")
        #print("Cancelsh")
        #exit() 
         

    def Restarbt(self,text):

        d = self.lineEdit.text()
        os.system("shutdown -f -r -t %s" % d)
        
     
    def Cancelsh(self):
        
        os.system("shutdown -a")
        print("Cancelsh")
        exit()   


    def retranslateUi(self, Shut):
        _translate = QtCore.QCoreApplication.translate
        Shut.setWindowTitle(_translate("Shut", "Shut"))
        self.ShutDown.setText(_translate("Shut", "Shut Down"))
        self.Restarbtn.setText(_translate("Shut", "Restar"))
        self.Cancel.setText(_translate("Shut", "Cancel"))
        #self.label.setText("first line\nsecond line")
   

    

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Shut = QtWidgets.QWidget()
    ui = Ui_Shut()
    ui.setupUi(Shut)
    Shut.show()
    sys.exit(app.exec_())
