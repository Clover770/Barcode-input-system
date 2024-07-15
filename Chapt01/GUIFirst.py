import sys

from PyQt5.QtWidgets import QApplication, QWidget, QPushButton,QDesktopWidget
from PyQt5.QtGui import QIcon

if __name__== '__main__':
    app = QApplication(sys.argv)

    w = QWidget()

    # 设置窗口大小
    w.resize(1050, 700)
    # 将窗口设置到左上角
    w.move(0, 0)
    # 调整窗口在屏幕中央显示
    center_pointer = QDesktopWidget().availableGeometry().center()
    x = center_pointer.x()
    y = center_pointer.y()
    old_x, old_y, width, height = w.frameGeometry().getRect()
    w.move(int(x - width/2), int(y - height/2))
    # 设置窗口标题
    w.setWindowTitle("第一个PyQt")
    # 设置图标
    w.setWindowIcon(QIcon('d.jpg'))

    # 创建按钮组件，设置父子关系
    btn = QPushButton("按钮", w)

    # 展示窗口
    w.show()

    # 程序循环等待
    app.exec_()