# view/templates/register.py
import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QToolButton
from PyQt5.QtGui import QIcon, QPainter, QPixmap
from PyQt5.QtCore import Qt, QFile, QTimer
from pathlib import Path


class AuthButton(QPushButton):
    def __init__(self, text, parent=None):
        super().__init__(parent)
        self.setText(text)
        self.setCursor(Qt.PointingHandCursor)

    def enterEvent(self, event):
        self.setStyleSheet("background-color: rgb(220, 220, 220);")
        super().enterEvent(event)

    def leaveEvent(self, event):
        self.setStyleSheet("")
        super().leaveEvent(event)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        # Draw button background
        painter.setPen(Qt.NoPen)
        painter.setBrush(self.palette().button().color())
        painter.drawRect(self.rect())

        # Draw button text
        painter.setPen(self.palette().buttonText().color())
        painter.drawText(self.rect(), Qt.AlignCenter, self.text())


class CustomLineEdit(QLineEdit):
    def __init__(self, lineEditObjectName, buttonName, objectName, parent=None):
        super().__init__(parent)
        self.setFixedSize(360, 40)
        self.setObjectName(lineEditObjectName)

        self.button = AuthButton(buttonName, self)
        self.button.setObjectName(objectName)
        self.button.setFixedSize(100, self.height() - 4)
        self.button.move(self.width() - self.button.width() - 2, 2)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.button.setFixedSize(100, self.height() - 4)
        self.button.move(self.width() - self.button.width() - 2, 2)

    def paintEvent(self, event):
        super().paintEvent(event)
        self.button.update()
        
    def getButton(self):
        return self.button


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.length_valid = False
        self.contain_valid = False
        self.pwd = ""
        self.initUI()

    def initUI(self):
        self.setWindowTitle('회원가입')
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setGeometry(0, 0, 400, 650)
        self.setFixedSize(400, 650)

        layout = QVBoxLayout()

        self.backButton = QPushButton(self)
        self.backButton.setFixedSize(17, 17)
        self.backButton.setIcon(QIcon(f'{Path(__file__).parents[1]}/static/back.png'))
        self.backButton.setObjectName('backButton')
        self.backButton.setCursor(Qt.PointingHandCursor)
        self.backButton.move(30, 30)

        titleLabel = QLabel('회원가입', self)
        titleLabel.setObjectName('title')
        titleLabel.move(160, 24)

        self.emailField = CustomLineEdit('emailLineEdit', '인증요청', 'verifyButton')
        self.emailField.setPlaceholderText('Email')

        emailLayout = QHBoxLayout()
        emailLayout.addWidget(self.emailField, alignment=Qt.AlignCenter)

        self.verifyField = CustomLineEdit('verifyField', '확인', 'confirmButton')
        self.verifyField.setPlaceholderText('인증코드 입력')

        authLayout = QHBoxLayout()
        authLayout.addWidget(self.verifyField, alignment=Qt.AlignCenter)

        self.passwordField = QLineEdit()
        self.passwordField.setPlaceholderText('Password')
        self.passwordField.setEchoMode(QLineEdit.Password)
        self.passwordField.setFixedSize(360, 40)
        
        # self.timer = QTimer()
        # self.timer.timeout.connect(self.hideLastCharacter)
        # self.timer.setInterval(1000)  # 设置定时器间隔为 1000 毫秒

        # self.passwordField.textChanged.connect(self.showLastCharacter)
        
        passwordLayout = QHBoxLayout()
        passwordLayout.addWidget(self.passwordField, alignment=Qt.AlignCenter)

        self.passwordConfirmField = QLineEdit()
        self.passwordConfirmField.setPlaceholderText('Password Confirm')
        self.passwordConfirmField.setEchoMode(QLineEdit.Password)
        self.passwordConfirmField.setFixedSize(360, 40)
        # self.passwordConfirmField.textChanged.connect(self.showLastCharacter)

        passwordConfirmLayout = QHBoxLayout()
        passwordConfirmLayout.addWidget(self.passwordConfirmField, alignment=Qt.AlignCenter)
        
        checkPasswordLengthLayout = QHBoxLayout()
        checkPasswordLengthLayout.addSpacing(15)
        checkPasswordLengthLayout.setAlignment(Qt.AlignLeft)
        self.tb_checkPasswordLength = QToolButton()
        self.tb_checkPasswordLength.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tb_checkPasswordLength.setText(' 8~16자 사이의 길이를 가진 비밀번호')
        self.tb_checkPasswordLength.setIcon(QIcon(f'{Path(__file__).parents[1]}/static/false.png'))
        self.tb_checkPasswordLength.setStyleSheet("border: none; color:red")
        checkPasswordLengthLayout.addWidget(self.tb_checkPasswordLength)
        
        checkPasswordContainLayout = QHBoxLayout()
        checkPasswordContainLayout.addSpacing(15)
        checkPasswordContainLayout.setAlignment(Qt.AlignLeft)
        self.tb_checkPasswordContain = QToolButton()
        self.tb_checkPasswordContain.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        self.tb_checkPasswordContain.setText(' 대문자, 소문자, 숫자, 특수기호를 각 1개 이상 포함')
        self.tb_checkPasswordContain.setIcon(QIcon(f'{Path(__file__).parents[1]}/static/false.png'))
        self.tb_checkPasswordContain.setStyleSheet("border: none; color:red")
        checkPasswordContainLayout.addWidget(self.tb_checkPasswordContain)
        
        # checkPasswordMatchLayout = QHBoxLayout()
        # checkPasswordMatchLayout.addSpacing(15)
        # checkPasswordMatchLayout.setAlignment(Qt.AlignLeft)
        # self.tb_checkPasswordMatch = QToolButton()
        # self.tb_checkPasswordMatch.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
        # self.tb_checkPasswordMatch.setText(' 두번 입력한 비밀번호가 다름')
        # self.tb_checkPasswordMatch.setIcon(QIcon(f'{Path(__file__).parents[1]}/static/false.png'))
        # self.tb_checkPasswordMatch.setStyleSheet("border: none; color:gray")
        # checkPasswordMatchLayout.addWidget(self.tb_checkPasswordMatch)

        signupButton = QPushButton('회원가입')
        signupButton.setObjectName('signupButton')
        signupButton.setCursor(Qt.PointingHandCursor)
        signupButton.setFixedSize(360, 40)

        signupButtonLayout = QHBoxLayout()
        signupButtonLayout.addWidget(signupButton, alignment=Qt.AlignCenter)

        findIDPWButton = QPushButton('ID/PW 찾기')
        findIDPWButton.setObjectName('findIDPW')
        adminContactButton = QPushButton('관리자 문의')
        adminContactButton.setObjectName('adminContact')

        bottomLayout = QHBoxLayout()
        bottomLayout.addSpacing(15)
        bottomLayout.addWidget(findIDPWButton, alignment=Qt.AlignLeft)
        bottomLayout.addWidget(adminContactButton, alignment=Qt.AlignRight)
        bottomLayout.addSpacing(15)

        layout.addSpacing(70)
        layout.addLayout(emailLayout)
        layout.addSpacing(10)
        layout.addLayout(authLayout)
        layout.addSpacing(20)
        layout.addLayout(passwordLayout)
        layout.addSpacing(10)
        layout.addLayout(passwordConfirmLayout)
        layout.addSpacing(5)
        layout.addLayout(checkPasswordLengthLayout)
        layout.addLayout(checkPasswordContainLayout)
        # layout.addLayout(checkPasswordMatchLayout)
        layout.addSpacing(180)
        layout.addLayout(signupButtonLayout)
        layout.addSpacing(20)
        layout.addLayout(bottomLayout)
        layout.setAlignment(Qt.AlignTop)

        self.setLayout(layout)
        self._setStyle()

        # Connect the textChanged signal of the passwordField
        self.passwordField.textChanged.connect(self.changeStyleSheet)
        
    def showLastCharacter(self):
        password = self.sender().text() 
        if password:
            last_character = password[-1]
            encrypted_text = '●' * (len(password) - 1) + last_character
            self.sender().setText(encrypted_text)  # 设置加密的文本

            self.timer.start(1000)  # 启动定时器，设定为1秒

    def hideLastCharacter(self):
        password = self.passwordField.text()
        encrypted_text = '●' * len(password)
        self.passwordField.setText(encrypted_text)  # 设置所有字符加密

        password1 = self.passwordField.text()
        password2 = self.passwordConfirmField.text()

        if password1:
            password = self.passwordField.text()
            encrypted_text = '●' * len(password)
            self.passwordField.setText(encrypted_text)  # 设置加密的文本

        if password2:
            password = self.passwordConfirmField.text()
            encrypted_text = '●' * len(password)
            self.passwordConfirmField.setText(encrypted_text)  # 设置加密的文本

        self.timer.stop()  # 停止定时器

    def _setStyle(self):
        qss_file = QFile(f'{Path(__file__).parents[1]}/static/register.qss')
        qss_file.open(QFile.ReadOnly | QFile.Text)
        style_sheet = qss_file.readAll()
        self.setStyleSheet(str(style_sheet, encoding='utf-8'))
        
    def validatePassword(self, password):
        self.length_valid = bool(re.match(r'^.{8,16}$', password))
        self.contain_valid = bool(re.search(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&]+$', password))

    def changeStyleSheet(self):
        password = self.sender().text()  # Get the text from the signal sender
        self.validatePassword(password)
        
        if self.length_valid:
            self.tb_checkPasswordLength.setIcon(QIcon(f'{Path(__file__).parents[1]}/static/true.png'))
            self.tb_checkPasswordLength.setStyleSheet("border: none; color:green")
        else:
            self.tb_checkPasswordLength.setIcon(QIcon(f'{Path(__file__).parents[1]}/static/false.png'))
            self.tb_checkPasswordLength.setStyleSheet("border: none; color:red")
            
        if self.contain_valid:
            self.tb_checkPasswordContain.setIcon(QIcon(f'{Path(__file__).parents[1]}/static/true.png'))
            self.tb_checkPasswordContain.setStyleSheet("border: none; color:green")
        else:
            self.tb_checkPasswordContain.setIcon(QIcon(f'{Path(__file__).parents[1]}/static/false.png'))
            self.tb_checkPasswordContain.setStyleSheet("border: none; color:red")


if __name__ == '__main__':
    app = QApplication(sys.argv)

    registerWindow = RegisterWindow()
    registerWindow.show()

    sys.exit(app.exec_())
