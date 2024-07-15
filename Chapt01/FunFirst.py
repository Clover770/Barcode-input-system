import sys

from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setWindowTitle("点击按钮触发响应函数")
        self.setWindowIcon(QIcon("d.jpg"))
        self.setFixedSize(400,300)
        btn = QPushButton("我是你爹",self)
        btn.clicked.connect(self.btn_click)
    def btn_click(self):
        print("我是你爹")


if __name__=='__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()