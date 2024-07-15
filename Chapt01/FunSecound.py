import sys

from PyQt5.QtCore import pyqtSignal
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication


class Mywindow(QWidget):
    # 声明一个信号只能放在函数外边
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.resize(300,200)
        btn = QPushButton("开始检测",self)

        # 绑定点击事件
        btn.clicked.connect(self.check)

        # 绑定信号和槽
        self.my_signal.connect(self.my_slot)

    def check(self):
        for i, ip in enumerate(["192.168.1.%d"%x for x in range(1,255)]):
            msg = "模拟，正在检测%s上的漏洞....." %ip
            if i % 5 == 0:
                self.my_signal.emit(msg+"【发现漏洞】")
            else:
                self.my_signal.emit(msg)

    def my_slot(self,msg):
        print(">>>>>",msg)

if __name__=='__main__':
    app=QApplication(sys.argv)

    w = Mywindow()
    w.show()

    app.exec_()