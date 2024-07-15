import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDesktopWidget,QVBoxLayout,QPushButton,QGroupBox,QRadioButton,QHBoxLayout

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        # 最外层的垂直布局包含两部分：爱好和性别
        container = QVBoxLayout()
        # --------创建第1个组，添加多个组件--------
        # hobby主要是保证他们是一个组。
        hobby_box = QGroupBox("爱好")
        # v_layout保证三个爱好是垂直摆放
        v_layout = QVBoxLayout()
        btn1 = QRadioButton("抽烟")
        btn2 = QRadioButton("喝酒")
        btn3 = QRadioButton("玩手机")
        # 添加到v_layout中
        v_layout.addWidget(btn1)
        v_layout.addWidget(btn2)
        v_layout.addWidget(btn3)
        # 把v_layout添加到hobby_box中
        hobby_box.setLayout(v_layout)

        # --------创建第2个组，添加多个组件--------
        gender_box = QGroupBox("性别")
        # 性别容器
        h_layout = QHBoxLayout()
        # 性别选项：男、女
        btn4 = QRadioButton("男")
        btn5 = QRadioButton("女")
        # 向layout容器中添加组件
        h_layout.addWidget(btn4)
        h_layout.addWidget(btn5)
        # 将layout添加到box中
        gender_box.setLayout(h_layout)

        # 将两个box添加到container中
        container.addWidget(hobby_box)
        container.addWidget(gender_box)

        # 将container设置到窗口中
        self.setLayout(container)

if __name__=='__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()

