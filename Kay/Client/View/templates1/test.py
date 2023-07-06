import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton

class LoginView(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口属性
        self.setWindowTitle('登录')
        self.resize(300, 150)

        # 垂直布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 用户名布局
        username_layout = QHBoxLayout()
        layout.addLayout(username_layout)
        username_label = QLabel('用户名')
        username_layout.addWidget(username_label)
        self.username_input = QLineEdit()
        username_layout.addWidget(self.username_input)

        # 密码布局
        password_layout = QHBoxLayout()
        layout.addLayout(password_layout)
        password_label = QLabel('密码')
        password_layout.addWidget(password_label)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(self.password_input)

        # 按钮布局
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)
        login_button = QPushButton('登录')
        button_layout.addWidget(login_button)
        register_button = QPushButton('注册')
        button_layout.addWidget(register_button)

class RegisterView(QWidget):
    def __init__(self):
        super().__init__()

        # 设置窗口属性
        self.setWindowTitle('注册')
        self.resize(300, 150)

        # 垂直布局
        layout = QVBoxLayout()
        self.setLayout(layout)

        # 用户名布局
        username_layout = QHBoxLayout()
        layout.addLayout(username_layout)
        username_label = QLabel('用户名')
        username_layout.addWidget(username_label)
        self.username_input = QLineEdit()
        username_layout.addWidget(self.username_input)

        # 密码布局
        password_layout = QHBoxLayout()
        layout.addLayout(password_layout)
        password_label = QLabel('密码')
        password_layout.addWidget(password_label)
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)
        password_layout.addWidget(self.password_input)

        # 按钮布局
        button_layout = QHBoxLayout()
        layout.addLayout(button_layout)
        register_button = QPushButton('注册')
        button_layout.addWidget(register_button)
        back_button = QPushButton('返回登录')
        button_layout.addWidget(back_button)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    # login_view = LoginView()
    register_view = RegisterView()
    register_view.show()
    sys.exit(app.exec_())