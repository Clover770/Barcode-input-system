import json
import sys
import time

import requests
from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QWidget

class LoginThread(QThread):
    start_login_signal = pyqtSignal(str)

    def __init__(self,signal):
        super().__init__()
        self.login_complete_signal = signal

    def login_by_requests(self,user_passsword_json):
         # 将json字符串转为自定
        user_password_dict = json.loads(user_passsword_json)
        print(user_password_dict.get("user_name"))
        print(user_password_dict.get("password"))

        r = requests.post(url="https://service-j421zn62-1311682057.gz.tencentapigw.com.cn/release/pyqt_login",json=user_password_dict)

        ret = r.json()

        self.login_complete_signal.emit(json.dumps(ret))

    def run(self):
        while True:
            print("子线程正在执行。。。。")
            time.sleep(1)

class MyWindow(QWidget):
    # 创建登录状态信息
    login_status_signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.ui = None
        self.user_name = None
        self.password = None
        self.text_browser = None
        self.login_thread = None
        self.init_ui()

    def init_ui(self):
        self.ui = uic.loadUi("./login_01.ui",self)
        # 绑定控件
        self.user_name = self.ui.lineEdit
        self.password = self.ui.lineEdit_3
        btn_login = self.ui.pushButton
        btn_register = self.ui.pushButton_2
        self.text_browser = self.ui.textBrowser

        # 绑定信号与槽函数
        btn_login.clicked.connect(self.login)

        self.login_status_signal.connect(self.login_status)

        # 创建一个子线程（将login_threat变量变为对象的属性，
        # 如果不是对象属性而是普通的局部变量会随则init_ui函数执行结束而被释放，此时子线程还没执行完，所以会产生的问题）
        self.login_thread = LoginThread(self.login_status_signal)
        self.login_thread.start_login_signal.connect(self.login_thread.login_by_requests)
        self.login_thread.start()

    def login(self):
        user_name = self.user_name.text()
        password = self.password.text()
        self.login_thread.start_login_signal.emit(json.dumps({"user_name":user_name,"password":password}))

    def login_status(self,status):
        status_dict = json.loads(status)
        print("status........",status_dict.get("errmsg"))
        self.text_browser.setText(status_dict.get("errmsg"))
        self.text_browser.repaint()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MyWindow()
    w.show()
    app.exec_()