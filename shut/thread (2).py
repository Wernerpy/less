import sys, time 
from PyQt5.QtWidgets import QApplication, QDialog,QPushButton,QProgressBar,QTextEdit,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QThread


class ProgressBarThread(QThread):
    def __init__(self, mainwindow, parent=None):
        super().__init__()
        self.mainwindow = mainwindow


    def run(self):
        for i in range(101):
            c=1+i
            c = c // 1
            self.mainwindow.progressbar.setValue(c)
            time.sleep(0.2)   

class MyProgressbarWindow(QDialog):
    def __init__(self, parent=None):
        super(). __init__()
        self.progressbar = QProgressBar()
        self.progressbar.setAlignment(Qt.AlignCenter)
        self.PushButtonLaunchLoading = QPushButton("Launch Loading")
        self.TextEditer = QTextEdit()
        self.setGeometry(300, 300, 300, 150)
        vbox = QVBoxLayout()
        vbox.addWidget(self.PushButtonLaunchLoading)
        vbox.addWidget(self.TextEditer)
        vbox.addWidget(self.progressbar)
        self.setLayout(vbox)
    
        self.PushButtonLaunchLoading.clicked.connect(self.launch_progress_bar_filling)
        self.ProgressbarThread_instance = ProgressBarThread(mainwindow=self)

    def launch_progress_bar_filling(self):
        self.ProgressbarThread_instance.start()


app = QApplication(sys.argv)
main = MyProgressbarWindow()
main.show()
sys.exit(app.exec_())


