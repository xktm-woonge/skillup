import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QSpacerItem, QSizePolicy, QHBoxLayout, QVBoxLayout, QCheckBox, QPushButton
from PyQt5.QtGui import QIcon, QPainter
from PyQt5.QtCore import Qt, QFile, QRect, QPoint
from pathlib import Path


class AuthButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setCursor(Qt.PointingHandCursor)  # 设置鼠标光标形状为手型

    def enterEvent(self, event):
        self.setStyleSheet("background-color: rgb(220, 220, 220);")  # 设置鼠标悬停时的背景颜色
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet("")  # 清除背景颜色样式
        super().leaveEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # 绘制按钮背景
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.palette().button().color())
        painter.drawEllipse(self.rect())

        # 绘制按钮文本
        painter.setPen(self.palette().buttonText().color())
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())


class CustomLineEdit(QLineEdit):
    def __init__(self, buttonName, objectName, parent=None):
        super().__init__(parent)
        self.buttonRect = QRect()
        self.buttonVisible = True

        self.button = AuthButton(buttonName, self)  # 将按钮的父级小部件设置为CustomLineEdit
        self.button.setObjectName(objectName)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.updateButtonRect()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.buttonVisible:
            painter = QPainter(self)
            painter.setRenderHint(QPainter.Antialiasing)

            self.button.setGeometry(self.buttonRect)

            self.button.render(painter)

    def updateButtonRect(self):
        buttonWidth = 100  # 设置按钮的宽度
        buttonHeight = self.height() - 4
        buttonX = self.width() - buttonWidth - 2
        buttonY = 2
        self.buttonRect = QRect(buttonX, buttonY, buttonWidth, buttonHeight)


class RegisterWindow(QWidget):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('회원가입')

        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint) # 최대화 버튼 제거

        # 메인창 위치
        self.setGeometry(0, 0, 400, 650)
        self.setFixedSize(400, 650)

        layout = QVBoxLayout()

        backButton = QPushButton(self)
        backButton.setIcon(QIcon(f'{Path(__file__).parents[1]}/static/back.png'))
        backButton.setObjectName('backButton')
        # backButton.move(-10, 44)
        backButton.setCursor(Qt.PointingHandCursor)

        titleLabel = QLabel('회원가입')
        titleLabel.setObjectName('title')
        titleLabel.setAlignment(Qt.AlignCenter)

        # Move backButton and titleLabel to the same layout
        titleLayout = QHBoxLayout()
        # titleLayout.addWidget(backButton)
        # titleLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding))
        titleLayout.addWidget(titleLabel)
        # titleLayout.addItem(QSpacerItem(0, 0, QSizePolicy.Expanding))


        emailField = CustomLineEdit('인증요청', 'verifyButton')
        emailField.setPlaceholderText('Email')

        authField = CustomLineEdit('확인', 'confirmButton')
        authField.setPlaceholderText('인증코드 입력')

        passwordField = QLineEdit()
        passwordField.setPlaceholderText('Password')

        passwordConfirmField = QLineEdit()
        passwordConfirmField.setPlaceholderText('Password Confirm')

        checkPasswordLength = QLabel('8~16자 사이의 길이를 가진 비밀번호')
        checkPasswordContain = QLabel('대문자, 소문자, 숫자, 특수기호를 각 1개 이상 포함')
        checkPasswordMatch = QLabel('두번 입력한 비밀번호가 다름')

        signupButton = QPushButton('회원가입')
        signupButton.setObjectName('signupButton')
        signupButton.setCursor(Qt.PointingHandCursor)

        findIDPWButton = QPushButton('ID/PW 찾기')
        findIDPWButton.setObjectName('findIDPW')
        adminContactButton = QPushButton('관리자 문의')
        adminContactButton.setObjectName('adminContact')

        bottomLayout = QHBoxLayout()  # 새로운 레이아웃 생성
        bottomLayout.addWidget(findIDPWButton, alignment=Qt.AlignLeft)
        bottomLayout.addWidget(adminContactButton, alignment=Qt.AlignRight)

        layout.addLayout(titleLayout)
        layout.addWidget(emailField)
        layout.addWidget(authField)
        layout.addWidget(passwordField)
        layout.addWidget(passwordConfirmField)
        layout.addWidget(checkPasswordLength)
        layout.addWidget(checkPasswordContain)
        layout.addWidget(checkPasswordMatch)
        layout.addWidget(signupButton)
        layout.addLayout(bottomLayout)

        self.setLayout(layout)
        self._setStyle()

    def _setStyle(self):
        qss_file = QFile(f'{Path(__file__).parents[1]}/static/register.qss')
        qss_file.open(QFile.ReadOnly | QFile.Text)
        style_sheet = qss_file.readAll()
        self.setStyleSheet(str(style_sheet, encoding='utf-8'))


if __name__ == '__main__':
    app = QApplication(sys.argv)

    registerWindow = RegisterWindow()
    registerWindow.show()

    sys.exit(app.exec_())
