import sys
import re
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QToolButton
from PyQt5.QtGui import QIcon, QPainter, QPixmap
from PyQt5.QtCore import Qt, QFile, QRect, QPoint
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
    def __init__(self, buttonName, objectName, parent=None):
        super().__init__(parent)
        self.setFixedSize(360, 40)

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


class RegisterWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.length_valid = False
        self.contain_valid = False
        self.initUI()

    def initUI(self):
        self.setWindowTitle('회원가입')
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint)
        self.setGeometry(0, 0, 400, 650)
        self.setFixedSize(400, 650)

        layout = QVBoxLayout()

        backButton = QPushButton(self)
        backButton.setFixedSize(17, 17)
        backButton.setIcon(QIcon(f'{Path(__file__).parents[1]}/static/back.png'))
        backButton.setObjectName('backButton')
        backButton.setCursor(Qt.PointingHandCursor)
        backButton.move(30, 30)

        titleLabel = QLabel('회원가입', self)
        titleLabel.setObjectName('title')
        titleLabel.move(160, 24)

        emailField = CustomLineEdit('인증발송', 'verifyButton')
        emailField.setPlaceholderText('Email')

        emailLayout = QHBoxLayout()
        emailLayout.addWidget(emailField, alignment=Qt.AlignCenter)

        authField = CustomLineEdit('확인', 'confirmButton')
        authField.setPlaceholderText('인증코드 입력')

        authLayout = QHBoxLayout()
        authLayout.addWidget(authField, alignment=Qt.AlignCenter)

        passwordField = QLineEdit()
        passwordField.setPlaceholderText('Password')
        passwordField.setFixedSize(360, 40)

        passwordLayout = QHBoxLayout()
        passwordLayout.addWidget(passwordField, alignment=Qt.AlignCenter)

        passwordConfirmField = QLineEdit()
        passwordConfirmField.setPlaceholderText('Password Confirm')
        passwordConfirmField.setFixedSize(360, 40)

        passwordConfirmLayout = QHBoxLayout()
        passwordConfirmLayout.addWidget(passwordConfirmField, alignment=Qt.AlignCenter)

        # self.checkPasswordLength = QLabel('8~16자 사이의 길이를 가진 비밀번호')
        # self.checkPasswordContain = QLabel('대문자, 소문자, 숫자, 특수기호를 각 1개 이상 포함')
        # self.checkPasswordMatch = QLabel('두번 입력한 비밀번호가 다름')
        # self.checkPasswordLength.setObjectName('checkPasswordLength')
        # self.checkPasswordContain.setObjectName('checkPasswordContain')
        # self.checkPasswordMatch.setObjectName('checkPasswordMatch')
        # self.checkPasswordLength.setContentsMargins(15, 0, 0, 0)
        # self.checkPasswordContain.setContentsMargins(15, 0, 0, 0)
        # self.checkPasswordMatch.setContentsMargins(15, 0, 0, 0)

        # falseLabel = QLabel()
        # falsePixmap = QPixmap((f'{Path(__file__).parents[1]}/static/false.jpg'))
        # smallFalsePixmap = falsePixmap.scaled(10, 10)
        # falseLabel.setPixmap(smallFalsePixmap)

        # checkPasswordLengthLayout = QHBoxLayout()
        # checkPasswordLengthLayout.addSpacing(15)
        # checkPasswordLengthLayout.addWidget(falseLabel)
        # checkPasswordLengthLayout.addWidget(self.checkPasswordLength)
        # checkPasswordLengthLayout.setAlignment(Qt.AlignLeft)

        # falseLabel = QLabel()
        # falsePixmap = QPixmap((f'{Path(__file__).parents[1]}/static/false.jpg'))
        # smallFalsePixmap = falsePixmap.scaled(10, 10)
        # falseLabel.setPixmap(smallFalsePixmap)

        # checkPasswordContainLayout = QHBoxLayout()
        # checkPasswordContainLayout.addSpacing(15)
        # checkPasswordContainLayout.addWidget(falseLabel)
        # checkPasswordContainLayout.addWidget(self.checkPasswordContain)
        # checkPasswordContainLayout.setAlignment(Qt.AlignLeft)

        # falseLabel = QLabel()
        # falsePixmap = QPixmap((f'{Path(__file__).parents[1]}/static/false.jpg'))
        # smallFalsePixmap = falsePixmap.scaled(10, 10)
        # falseLabel.setPixmap(smallFalsePixmap)

        # checkPasswordMatchLayout = QHBoxLayout()
        # checkPasswordMatchLayout.addSpacing(15)
        # checkPasswordMatchLayout.addWidget(falseLabel)
        # checkPasswordMatchLayout.addWidget(self.checkPasswordMatch)
        # checkPasswordMatchLayout.setAlignment(Qt.AlignLeft)
        
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
        passwordField.textChanged.connect(self.changeStyleSheet)

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
