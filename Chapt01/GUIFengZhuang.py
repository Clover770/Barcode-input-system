import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget,QVBoxLayout,QPushButton

class MyWindow(QWidget):
    def __init__(self):
        # 切记要调用init方法，里边有很多初始化
        super().__init__()
        self.resize(int(1050), int(700))
        self.setWindowTitle("垂直布局")
        layout = QVBoxLayout()
        layout.addStretch(2)

        # 设置按钮
        btn1 = QPushButton("按钮1")
        layout.addWidget(btn1)
        btn2 = QPushButton("按钮2")
        layout.addWidget(btn2)
        btn3 = QPushButton("按钮3")
        layout.addWidget(btn3)

        layout.addStretch(2)
        self.setLayout(layout)


if __name__== '__main__':
    app = QApplication(sys.argv)

    # 创建一个QWidget类
    w= MyWindow()
    w.show()

    app.exec_()