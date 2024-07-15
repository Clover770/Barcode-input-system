import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./login_01.ui", self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()

    app.exec_()
