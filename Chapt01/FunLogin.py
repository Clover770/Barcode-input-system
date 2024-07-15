import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget


class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = None
        self.user_name = None
        self.password = None
        self.text_browser = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./login_01.ui",self)
        self.user_name = self.ui.lineEdit
        self.password = self.ui.lineEdit_3
        btn_login = self.ui.pushButton
        btn_register = self.ui.pushButton_2
        self.text_browser = self.ui.textBrowser
        btn_login.clicked.connect(self.login)
        btn_register.clicked.connect(self.register)

    def login(self):
        user_name = self.user_name.text()
        password = self.password.text()
        print(self.user_name.text())
        print(self.password.text())
        print("正在登录")
        if user_name == "admin" and password == "123":
            self.text_browser.setText("欢迎%s" % user_name)
            self.text_browser.repaint()
        else:
            self.text_browser.setText("用户名或密码错误。。。")
            self.text_browser.repaint()

    def register(self):
        print(self.password.text())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()

    app.exec_()
