from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton, QLabel, QDesktopWidget
from PyQt5.QtGui import QFont

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('Chatting')

        # 메인창 위치
        self.setGeometry(0, 0, 400, 600)
        self.center()

        layout = QVBoxLayout()

        label_login = QLabel("LOGIN")
        layout.addWidget(label_login)

        self.lineedit_id = QLineEdit()
        self.lineedit_id.setPlaceholderText("ID")
        layout.addWidget(self.lineedit_id)
        self.lineedit_pwd = QLineEdit()
        self.lineedit_pwd.setPlaceholderText("PASSWORD")
        layout.addWidget(self.lineedit_pwd)

        button_login = QPushButton("LOGIN")
        layout.addWidget(button_login)
        button_signup = QPushButton("SIGNUP")
        layout.addWidget(button_signup)

        self.setLayout(layout)

        # # 设置字体
        # font = QFont()
        # font.setPointSize(12)

        # # 创建布局
        # layout = QVBoxLayout()

        # # 创建标签和文本框
        # label1 = QLabel('用户名')
        # label1.setFont(font)
        # self.username = QLineEdit()
        # self.username.setFont(font)
        # layout.addWidget(label1)
        # layout.addWidget(self.username)

        # label2 = QLabel('密码')
        # label2.setFont(font)
        # self.password = QLineEdit()
        # self.password.setEchoMode(QLineEdit.Password)
        # self.password.setFont(font)
        # layout.addWidget(label2)
        # layout.addWidget(self.password)

        # # 创建登录按钮
        # self.loginButton = QPushButton('登录')
        # self.loginButton.setFont(font)
        # self.loginButton.clicked.connect(self.login)
        # layout.addWidget(self.loginButton)

        # # 设置布局
        # self.setLayout(layout)

    def center(self):
        # 获取屏幕的矩形
        screenRect = QDesktopWidget().screenGeometry()

        # 获取窗口的矩形
        windowRect = self.frameGeometry()

        # 计算居中位置
        x = (screenRect.width() - windowRect.width()) // 2
        y = (screenRect.height() - windowRect.height()) // 2

        # 移动窗口
        self.move(x, y)


    def login(self):
        username = self.username.text()
        password = self.password.text()

        # 在这里可以添加登录逻辑

if __name__ == '__main__':
    app = QApplication([])
    loginWindow = LoginWindow()
    loginWindow.show()
    app.exec_()
