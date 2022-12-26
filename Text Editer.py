

from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenuBar, QMenu, QFileDialog

import sys

class Window(QMainWindow):
    def __init__(self):
        super(Window,self).__init__()

        self.setWindowTitle("Text Editor")
        self.setGeometry(300,300,300,300)
        self.text_edit = QtWidgets.QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        self.createMenuBar()

    def createMenuBar(self):
        self.menuBar = QMenuBar(self)
        self.setMenuBar(self.menuBar)

        failMenu = QMenu("&Fail",self)
        self.menuBar.addMenu(failMenu)

        #open_file = failMenu.addMenu("&Open")
        #save_file = failMenu.addMenu("&Save")

        failMenu.addAction("Open",self.action_clicked)
        failMenu.addAction("Save",self.action_clicked)


    @QtCore.pyqtSlot()

    def action_clicked(self):
        action = self.sender()
        if action.text() == "Open":
            fname = QFileDialog.getOpenFileName(self)[0]
            try:
                f = open(fname, "r")
                with f:
                    data = f.read()
                    self.text_edit.setText(data)
                f.close()    
            except FileNotFoundError:
               print("FileNotFoundError_Open")


        elif action.text() == "Save":
            fname = QFileDialog.getSaveFileName(self)[0]
            try:
                f = open(fname, "w")
                text = self.text_edit.toPlainText()
                f.write(text)
                f.close()

            except FileNotFoundError:
               print("FileNotFoundError_Save")


    
def application():

    app = QApplication(sys.argv)
    window = Window()

    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    application()