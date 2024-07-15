import sys
import time

from PyQt5 import uic
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QApplication, QWidget

class MyThread(QThread):
    def __init__(self):
        super().__init__()

    def run(self):
        for i in range(10):
            print("这是一个线程操作%s" %(i+1))
            time.sleep(1)


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.msg = None
        self.my_thread = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./FunXianCheng.ui",self)

        btn1 = self.ui.pushButton
        btn2 = self.ui.pushButton_2

        btn1.clicked.connect(self.click_1)
        btn2.clicked.connect(self.click_2)

    def click_1(self):
        for i in range(10):
            print("非线程执行中%s" %(i+1))
            time.sleep(1)
        print(self.ui.lineEdit.text())

    def click_2(self):
        self.my_thread = MyThread()
        self.my_thread.start()
        print(self.ui.lineEdit.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()
