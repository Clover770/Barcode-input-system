import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QTableWidget, QTableWidgetItem, \
    QPushButton, QVBoxLayout, QHBoxLayout, QGridLayout, QSizePolicy, QMessageBox, QHeaderView, QScrollArea
from datetime import datetime
from PyQt5.QtGui import QPixmap
import database  # 导入数据库模块

# 定义条码记录系统类，继承自QMainWindow
class BarcodeRecordSystem(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()  # 调用初始化用户界面的方法

    # 初始化用户界面的方法
    def init_ui(self):
        self.setWindowTitle("条码记录系统")  # 设置窗口标题
        self.setGeometry(100, 100, 1200, 800)  # 设置窗口大小和位置

        # 主布局
        main_layout = QVBoxLayout()

        # 顶部部分：Logo和标题
        top_layout = QHBoxLayout()
        logo_label = QLabel()
        pixmap = QPixmap("pictures/b.jpg")  # 替换为你的图片路径
        pixmap = pixmap.scaledToWidth(100)  # 调整图片宽度为100像素，高度按比例缩放
        logo_label.setPixmap(pixmap)
        top_layout.addWidget(logo_label)
        top_layout.addStretch()  # 添加弹性空间
        title = QLabel("条码记录系统")
        title.setStyleSheet("font-size: 36px; color: yellow;")  # 设置标题的样式
        top_layout.addWidget(title)
        top_layout.addStretch()
        top_layout.setContentsMargins(10, 10, 10, 10)  # 设置边距
        main_layout.addLayout(top_layout)
        main_layout.setStretchFactor(top_layout, 2)  # 增加顶部部分的比例

        # 中间部分：表单和表格
        middle_layout = QVBoxLayout()

        form_layout = QGridLayout()
        form_layout.addWidget(QLabel("任务单:"), 0, 0)
        self.task_input = QLineEdit()
        form_layout.addWidget(self.task_input, 0, 1)

        form_layout.addWidget(QLabel("自动装袋数:"), 0, 2)
        self.count_input = QLineEdit()
        form_layout.addWidget(self.count_input, 0, 3)

        form_layout.addWidget(QLabel("扫码人:"), 0, 4)
        self.user_input = QLineEdit()
        form_layout.addWidget(self.user_input, 0, 5)

        middle_layout.addLayout(form_layout)

        # 创建一个表格，包含10行4列
        self.table = QTableWidget(10, 4)
        self.table.setHorizontalHeaderLabels(["任务单", "条码", "时间", "扫码人员"])  # 设置表格头标签
        self.table.verticalHeader().setVisible(True)  # 保留默认行号
        self.table.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)  # 设置表格大小策略，填充满整个布局
        self.table.horizontalHeader().setStretchLastSection(True)  # 让最后一列自动填充
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # 让所有列自动填充

        # 创建滚动区域并添加表格
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.table)

        middle_layout.addWidget(scroll_area)
        middle_layout.setStretch(1, 1)  # 让表格占据中间部分的最大空间
        main_layout.addLayout(middle_layout)
        main_layout.setStretchFactor(middle_layout, 8)  # 设置中间部分比例

        # 底部部分：条码输入和按钮
        bottom_layout = QHBoxLayout()
        self.barcode_input = QLineEdit()
        self.barcode_input.setPlaceholderText("条码录入")  # 设置条码输入框的占位符
        self.barcode_input.returnPressed.connect(self.add_scan_record)  # 将回车键与扫码按钮等效
        bottom_layout.addWidget(self.barcode_input)

        # 创建按钮并添加到布局中
        scan_button = QPushButton("扫码")
        scan_button.clicked.connect(self.add_scan_record)  # 绑定扫码按钮的点击事件
        cancel_button = QPushButton("取消")
        cancel_button.clicked.connect(self.clear_barcode_input)  # 绑定取消按钮的点击事件
        clear_button = QPushButton("一键清空")
        clear_button.clicked.connect(self.clear_all_inputs)  # 绑定一键清空按钮的点击事件
        data_button = QPushButton("基础数据")
        data_button.clicked.connect(self.show_basic_data)  # 绑定基础数据按钮的点击事件
        help_button = QPushButton("使用说明")
        help_button.clicked.connect(self.show_help)  # 绑定使用说明按钮的点击事件
        exit_button = QPushButton("退出/Exit")
        exit_button.clicked.connect(self.close)  # 绑定退出按钮的点击事件

        bottom_layout.addWidget(scan_button)
        bottom_layout.addWidget(cancel_button)
        bottom_layout.addWidget(clear_button)
        bottom_layout.addWidget(data_button)
        bottom_layout.addWidget(help_button)
        bottom_layout.addWidget(exit_button)
        bottom_layout.setContentsMargins(10, 10, 10, 10)  # 设置边距

        main_layout.addLayout(bottom_layout)
        main_layout.setStretchFactor(bottom_layout, 2)  # 增加底部部分的比例

        # 设置主布局
        widget = QWidget()
        widget.setLayout(main_layout)
        self.setCentralWidget(widget)

    # 清除条码录入框的内容
    def clear_barcode_input(self):
        self.barcode_input.clear()

    # 清空所有输入框的内容
    def clear_all_inputs(self):
        self.task_input.clear()
        self.count_input.clear()
        self.user_input.clear()
        self.barcode_input.clear()

    # 添加扫码记录的方法
    def add_scan_record(self):
        # 获取当前表格中的行数
        row_position = self.table.rowCount()
        self.table.insertRow(row_position)  # 在表格中插入新行

        # 获取用户输入的值
        task = self.task_input.text()
        barcode = self.barcode_input.text()
        user = self.user_input.text()

        # 获取当前时间并格式化
        current_time = datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")

        # 查找任务单非空的最后一行
        last_nonempty_row = -1
        for row in range(self.table.rowCount()):
            if self.table.item(row, 0) is not None and self.table.item(row, 0).text() != "":
                last_nonempty_row = row

        new_row = last_nonempty_row + 1

        # 添加到表格中
        self.table.setItem(new_row, 0, QTableWidgetItem(task))
        self.table.setItem(new_row, 1, QTableWidgetItem(barcode))
        self.table.setItem(new_row, 2, QTableWidgetItem(current_time))
        self.table.setItem(new_row, 3, QTableWidgetItem(user))

    # 点击基础数据按钮后执行的方法
    def show_basic_data(self):
        # 获取扫码人员输入框中的内容
        user = self.user_input.text()

        # 获取数据库查询结果
        data = database.get_records_by_user(user)

        # 清空表格
        self.table.setRowCount(0)

        # 将查询结果填充到表格中
        for row_num, row_data in enumerate(data):
            self.table.insertRow(row_num)
            for col_num, col_data in enumerate(row_data):
                self.table.setItem(row_num, col_num, QTableWidgetItem(str(col_data)))

    # 显示使用说明
    def show_help(self):
        QMessageBox.information(self, "使用说明", "这是条码记录系统的使用说明。")

# 程序入口
if __name__ == '__main__':
    app = QApplication(sys.argv)  # 创建QApplication对象
    window = BarcodeRecordSystem()  # 创建主窗口对象
    window.show()  # 显示主窗口
    sys.exit(app.exec_())  # 进入应用程序的主循环
