from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QVBoxLayout
from PyQt5.QtCore import QTimer
import sys

class PasswordInputWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.passwordLineEdit1 = QLineEdit()
        layout.addWidget(self.passwordLineEdit1)

        self.passwordLineEdit2 = QLineEdit()
        layout.addWidget(self.passwordLineEdit2)

        self.timer = QTimer()
        self.timer.timeout.connect(self.updatePasswordInput)

        self.passwordLineEdit1.textChanged.connect(self.startTimer)  # 监听文本变化信号
        self.passwordLineEdit2.textChanged.connect(self.startTimer)  # 监听文本变化信号

        self.setLayout(layout)

    def startTimer(self):
        self.timer.start(1000)  # 启动定时器，设定为1秒

    def updatePasswordInput(self):
        password1 = self.passwordLineEdit1.text()
        password2 = self.passwordLineEdit2.text()

        if password1:
            last_character = password1[-1]
            encrypted_text = '*' * (len(password1) - 1) + last_character
            self.passwordLineEdit1.setText(encrypted_text)  # 设置加密的文本

        if password2:
            last_character = password2[-1]
            encrypted_text = '*' * (len(password2) - 1) + last_character
            self.passwordLineEdit2.setText(encrypted_text)  # 设置加密的文本

        self.timer.stop()  # 停止定时器

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = PasswordInputWidget()
    window.show()

    sys.exit(app.exec_())
