import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QVBoxLayout,QFormLayout,QLineEdit,QPushButton,QApplication,QWidget

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        # 设置固定高度
        self.setFixedSize(300,150)
        self.setWindowTitle("这是一个登录框")

        # 设置外层容器
        container = QVBoxLayout()

        # 表单容器
        form_layout = QFormLayout()

        # 创建输入框
        username_edit = QLineEdit()
        username_edit.setPlaceholderText("请输入用户名：")
        form_layout.addRow("账号：",username_edit)

        password_edit = QLineEdit()
        password_edit.setPlaceholderText("请输入密码：")
        form_layout.addRow("密码：",password_edit)

        # 将form表单添加到container中
        container.addLayout(form_layout)

        login_btn = QPushButton("登录")
        login_btn.setFixedSize(100,30)
        container.addWidget(login_btn,alignment=Qt.AlignRight)

        self.setLayout(container)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    w = MyWindow()
    w.show()

    app.exec_()
