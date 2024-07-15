import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QPushButton,QStackedLayout,QLabel

class Window1(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("抽屉一",self)
        self.setStyleSheet("background-color:green;")

class Window2(QWidget):
    def __init__(self):
        super().__init__()
        QLabel("抽屉二",self)
        self.setStyleSheet("background-color:red;")

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.create_staked_layout()
        self.init_ui()

    def create_staked_layout(self):
        # 创建抽屉布局
        self.stacked_layout = QStackedLayout()
        win1 = Window1()
        win2 = Window2()
        self.stacked_layout.addWidget(win1)
        self.stacked_layout.addWidget(win2)


    def init_ui(self):
        # 设置宽高
        self.setFixedSize(300,270)
        self.setWindowTitle("这是一个抽屉布局")

        # 创建整体布局器
        container = QVBoxLayout()

        # 创建要显示的一个子widget
        widget = QWidget()
        widget.setLayout(self.stacked_layout)
        widget.setStyleSheet("background-color:grey;")

        # 创建两个按钮
        btn_press1 = QPushButton("抽屉1")
        btn_press2 = QPushButton("抽屉2")
        btn_press1.clicked.connect(self.btn_press1_clicked)
        btn_press2.clicked.connect(self.btn_press2_clicked)

        # 在布局器中添加组件
        container.addWidget(widget)
        container.addWidget(btn_press1)
        container.addWidget(btn_press2)

        # 布局器和上级关联
        self.setLayout(container)

    def btn_press1_clicked(self):
        # 设置当前布局器索引值，即切换显示那个widget
        self.stacked_layout.setCurrentIndex(0)

    def btn_press2_clicked(self):
        # 设置当前布局器索引值，即切换显示那个widget
        self.stacked_layout.setCurrentIndex(1)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    win = MyWindow()
    win.show()

    app.exec_()
