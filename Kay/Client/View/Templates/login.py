# view/templates/login.py

import sys
from pathlib import Path
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, \
                            QLabel, QLineEdit, QPushButton, QDesktopWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap

try:
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))
    from utils import *


class LoginWindow(QWidget):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
    def initUI(self):
        # 윈도우 설정
        self.setWindowTitle('로그인')
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowMaximizeButtonHint) # 최대화 버튼 제거
        
        # 메인창 위치
        self.setGeometry(0, 0, 400, 650)
        self.setFixedSize(400, 650)
        self._moveToCenter()

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # 모든 마진을 0으로 설정
        layout.setSpacing(0)  # 모든 공백을 0으로 설정
        self.setLayout(layout)

        # 이미지 레이블
        pixmap = QPixmap(f'{Path(__file__).parents[1]}/static/img/background.png')
        imageLabel = QLabel()
        imageLabel.setPixmap(pixmap)
        imageLabel.setScaledContents(True)  # 추가된 줄
        layout.addWidget(imageLabel)

        # 제목 레이블
        titleLabel = QLabel('로그인')
        titleLabel.setObjectName('title')
        titleLabel.setFont(font.NOTOSAN_FONT_BOLD)
        titleLabel.setAlignment(Qt.AlignCenter)  # 가운데 정렬
        layout.addWidget(titleLabel)
        
        # 이메일, 비밀번호 입력 필드
        self.emailField = QLineEdit()
        self.emailField.setPlaceholderText('Email')
        self.emailField.setFixedSize(350, 50)
        
        # QHBoxLayout를 생성하고 가운데 정렬을 적용한 후 메인 레이아웃에 추가
        emailLayout = QHBoxLayout()
        emailLayout.addWidget(self.emailField, alignment=Qt.AlignCenter)
        layout.addLayout(emailLayout)

        self.passwordField = QLineEdit()
        self.passwordField.setPlaceholderText('Password')
        self.passwordField.setEchoMode(QLineEdit.Password)
        self.passwordField.setFixedSize(350, 50)
        
        # QHBoxLayout를 생성하고 가운데 정렬을 적용한 후 메인 레이아웃에 추가
        passwordLayout = QHBoxLayout()
        passwordLayout.addWidget(self.passwordField, alignment=Qt.AlignCenter)
        layout.addLayout(passwordLayout)
        
        # 로그인, 회원가입 버튼
        self.loginButton = QPushButton('로그인')
        self.loginButton.setObjectName('loginButton')
        self.loginButton.setCursor(Qt.PointingHandCursor)  # 마우스 오버 시 커서 변경
        self.loginButton.setFixedSize(350, 50)
        
        # QHBoxLayout를 생성하고 가운데 정렬을 적용한 후 메인 레이아웃에 추가
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.loginButton, alignment=Qt.AlignCenter)
        layout.addLayout(buttonLayout)

        self.registerButton = QPushButton('회원가입')
        self.registerButton.setObjectName('registerButton')
        self.registerButton.setCursor(Qt.PointingHandCursor)  # 마우스 오버 시 커서 변경
        self.registerButton.setFixedSize(350, 50)
        
        # QHBoxLayout를 생성하고 가운데 정렬을 적용한 후 메인 레이아웃에 추가
        buttonLayout = QHBoxLayout()
        buttonLayout.addWidget(self.registerButton, alignment=Qt.AlignCenter)
        layout.addLayout(buttonLayout)
        
        # ID/PW 찾기, 관리자 문의 레이블
        bottomLayout = QHBoxLayout()  # 새로운 레이아웃 생성
        bottomLayout.setContentsMargins(20, 0, 20, 0)  # 좌, 상, 우, 하 마진 설정
        
        layout.addSpacing(20)

        findIDPWButton = QPushButton('ID/PW 찾기')
        findIDPWButton.setObjectName('findIDPW')
        findIDPWButton.setCursor(Qt.PointingHandCursor)  # 마우스 오버 시 커서 변경
        bottomLayout.addWidget(findIDPWButton, alignment=Qt.AlignLeft)  # 새로운 레이아웃에 추가

        adminContactButton = QPushButton('관리자 문의')
        adminContactButton.setObjectName('adminContact')
        adminContactButton.setCursor(Qt.PointingHandCursor)  # 마우스 오버 시 커서 변경
        bottomLayout.addWidget(adminContactButton, alignment=Qt.AlignRight)  # 새로운 레이아웃에 추가

        layout.setContentsMargins(0, 0, 0, 50)
        
        self._setStyle()
        layout.addLayout(bottomLayout)  # 메인 레이아웃에 추가

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
        qss_file = QFile(f'{Path(__file__).parents[1]}/static/login.qss')
        qss_file.open(QFile.ReadOnly | QFile.Text)
        style_sheet = qss_file.readAll()
        self.setStyleSheet(str(style_sheet, encoding='utf-8'))
        
        
if __name__ == '__main__':
    app = QApplication(sys.argv)

    # 스타일 시트 적용
    # with open(f'{Path(__file__).parents[1]}/static/login.qss', 'r', encoding='utf-8') as f:
    #     app.setStyleSheet(f.read())

    loginWindow = LoginWindow()
    loginWindow.show()

    sys.exit(app.exec_())