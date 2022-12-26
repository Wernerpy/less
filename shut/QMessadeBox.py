from PyQt5 import QtWidgets 
from PyQt5.QtWidgets import QApplication, QMessageBox






msg = QMessageBox()
msg.exec_()


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    Form.show()
    sys.exit(app.exec_())

