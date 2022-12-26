#!/usr/bin/python

import sys
from PyQt5.QtWidgets import QWidget, QLabel, QCheckBox, QApplication, QHBoxLayout

class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        hbox = QHBoxLayout()

        cb = QCheckBox('Show title', self)
        cb.move(150, 200)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        hbox.addWidget(QLabel("falcon"))
        hbox.addWidget(QLabel("owl"))
        hbox.addWidget(QLabel("eagle"))
        hbox.addWidget(QLabel("skylark"))

        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)

        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)
        
        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)



        self.setLayout(hbox)

        self.setGeometry(100, 100, 350, 250)
        self.setWindowTitle('QCheckBox')
        
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle('')

def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()


'''
    #!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
from PyQt5.QtWidgets import QWidget, QLabel, QApplication
 
class Example(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        lbl1 = QLabel('Zetcode', self)
        lbl1.move(15, 10)
        lbl2 = QLabel('tutorials', self)
        lbl2.move(35, 40)
        
        lbl3 = QLabel('for programmers', self)
        lbl3.move(55, 70)        
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Absolute')    
        self.show()
         
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())

'''