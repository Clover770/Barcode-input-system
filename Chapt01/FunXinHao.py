import sys

from PyQt5.QtCore import pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication, QVBoxLayout, QLabel, QScrollArea, QHBoxLayout


class Mywindow(QWidget):
    # 声明一个信号只能放在函数外边
    my_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.init_ui()
        self.msg_history = list()

    def init_ui(self):
        self.resize(500,200)

        # 创建一个整体布局器
        container = QVBoxLayout()

        # 滚动框
        self.msg = QLabel()
        self.msg.resize(440,15)
        self.msg.setWordWrap(True)
        self.msg.setAlignment(Qt.AlignTop)

        # 滚动条关联滚动框
        scroll = QScrollArea()
        scroll.setWidget(self.msg)

        # 将滚动框放入垂直布局器中
        v_layout = QVBoxLayout()
        v_layout.addWidget(scroll)

        # 创建水平布局器,将按钮放入其中
        h_layout = QHBoxLayout()
        btn = QPushButton("开始检测",self)
        # 绑定点击事件
        btn.clicked.connect(self.check)
        h_layout.addStretch(1)
        h_layout.addWidget(btn)
        h_layout.addStretch(1)

        # 将两个布局器添加到总容器中
        container.addLayout(v_layout)
        container.addLayout(h_layout)

        # 总容器关联父容器
        self.setLayout(container)

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
        self.msg_history.append(msg)
        self.msg.setText("<br/>".join(self.msg_history))
        self.msg.resize(440,self.msg.frameSize().height() + 15)
        self.msg.repaint()

if __name__=='__main__':
    app=QApplication(sys.argv)

    w = Mywindow()
    w.show()

    app.exec_()