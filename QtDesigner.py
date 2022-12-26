from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()

        self.setWindowTitle( "Простая программа")
        self.setGeometry( 200, 200, 300, 300)

        self.new_text = QtWidgets.QLabel(self)

        self.btn = QtWidgets.QPushButton(self)
        self.btn.setText("Это некий текст у кнопки")
        self.btn.move(100, 10)
        #btn.setFixedWidth(200)
        #btn.setFixedHeight(25)
        #btn.setFixedSize(150, 30)
        self.btn.adjustSize()
        self.btn.clicked.connect(self.add_label)

        self.main_text = QtWidgets.QLabel(self)
        self.main_text.setText("Это базовая надпись ")
        self.main_text.move(100, 50)
        self.main_text.adjustSize()


    def add_label(self):
        print("add_label")
        self.new_text.setText("New text for my ))))")
        self.new_text.move(80, 80)
        self.new_text.adjustSize()




def application():
    app = QApplication(sys.argv)
    window = Window()

   




    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    application()

