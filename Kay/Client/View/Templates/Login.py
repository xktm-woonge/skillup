import os
from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QDesktopWidget

try:
    from Templates import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))

    from Templates import *

class LoginWindow(QWidget):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        super().__init__()

        BUTTON_HEIGHT = 80

        self.setWindowTitle('Chatting')

        # 메인창 위치
        self.setGeometry(0, 0, 400, 600)
        self.setFixedSize(400, 600)
        self._moveToCenter()
        
        layout = QVBoxLayout()

        label_login = QLabel("LOGIN")
        label_login.setObjectName("label_login")
        layout.addWidget(label_login)

        self.lineEdit_id = QLineEdit()
        self.lineEdit_id.setObjectName("lineEdit")
        self.lineEdit_id.setPlaceholderText("ID")
        layout.addWidget(self.lineEdit_id)

        self.lineEdit_pwd = QLineEdit()
        self.lineEdit_pwd.setObjectName("lineEdit")
        self.lineEdit_pwd.setPlaceholderText("PASSWORD")
        layout.addWidget(self.lineEdit_pwd)

        self.btn_login = HoverButton("LOGIN")
        self.btn_login.setFixedHeight(BUTTON_HEIGHT)
        layout.addWidget(self.btn_login)
        self.btn_register = HoverButton("REGISTER")
        self.btn_register.setFixedHeight(BUTTON_HEIGHT)
        layout.addWidget(self.btn_register)

        self._setStyle()
        self.setLayout(layout)

    def _moveToCenter(self):
        # 获取屏幕的矩形
        screenRect = QDesktopWidget().screenGeometry()

        # 获取窗口的矩形
        windowRect = self.frameGeometry()

        # 计算居中位置
        x = (screenRect.width() - windowRect.width()) // 2
        y = (screenRect.height() - windowRect.height()) // 2

        # 移动窗口
        self.move(x, y)

    def _setStyle(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(current_path)

        qss_file = QFile('../Static/login.qss')
        qss_file.open(QFile.ReadOnly | QFile.Text)
        style_sheet = qss_file.readAll()
        self.setStyleSheet(str(style_sheet, encoding='utf-8'))


if __name__ == '__main__':
    app = QApplication([])
    loginWindow = LoginWindow()
    loginWindow.show()
    app.exec_()