# main.py
import os
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSizePolicy,\
                            QLabel, QLineEdit, QPushButton, QDesktopWidget, QHBoxLayout
from PyQt5.QtGui import QPixmap

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
        self.setGeometry(0, 0, 400, 600)
        self.setFixedSize(400, 600)
        self._moveToCenter()

        # 레이아웃 설정
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)  # 모든 마진을 0으로 설정
        layout.setSpacing(0)  # 모든 공백을 0으로 설정
        self.setLayout(layout)

        # 이미지 레이블
        pixmap = QPixmap(r'D:\g_Project\2023_skillup_chatting\Kay\Client\view\static\background.png')
        imageLabel = QLabel()
        imageLabel.setPixmap(pixmap)
        imageLabel.setScaledContents(True)  # 추가된 줄
        layout.addWidget(imageLabel)

        # 제목 레이블
        titleLabel = QLabel('로그인')
        titleLabel.setObjectName('title')
        titleLabel.setAlignment(Qt.AlignCenter)  # 가운데 정렬
        layout.addWidget(titleLabel)
        
        # 이메일, 비밀번호 입력 필드
        emailField = QLineEdit()
        emailField.setStyleSheet("QLineEdit { padding-left: 10px; }")  # 여백 추가
        emailField.setPlaceholderText('Email')
        layout.addWidget(emailField)

        passwordField = QLineEdit()
        passwordField.setStyleSheet("QLineEdit { padding-left: 10px; }")  # 여백 추가
        passwordField.setPlaceholderText('비밀번호')
        layout.addWidget(passwordField)
        
        # 로그인, 회원가입 버튼
        loginButton = QPushButton('로그인')
        loginButton.setObjectName('loginButton')
        loginButton.setCursor(Qt.PointingHandCursor)  # 마우스 오버 시 커서 변경
        layout.addWidget(loginButton)  # layout에 추가

        signupButton = QPushButton('회원가입')
        signupButton.setObjectName('signupButton')
        signupButton.setCursor(Qt.PointingHandCursor)  # 마우스 오버 시 커서 변경
        layout.addWidget(signupButton)  # layout에 추가
        
        # ID/PW 찾기, 관리자 문의 레이블
        bottomLayout = QHBoxLayout()  # 새로운 레이아웃 생성
        bottomLayout.setContentsMargins(20, 0, 20, 0)  # 좌, 상, 우, 하 마진 설정

        findIDPWLabel = QLabel('ID/PW 찾기')
        findIDPWLabel.setObjectName('findIDPW')
        findIDPWLabel.setCursor(Qt.PointingHandCursor)  # 마우스 오버 시 커서 변경
        bottomLayout.addWidget(findIDPWLabel, alignment=Qt.AlignLeft)  # 새로운 레이아웃에 추가

        adminContactLabel = QLabel('관리자 문의')
        adminContactLabel.setObjectName('adminContact')
        adminContactLabel.setCursor(Qt.PointingHandCursor)  # 마우스 오버 시 커서 변경
        bottomLayout.addWidget(adminContactLabel, alignment=Qt.AlignRight)  # 새로운 레이아웃에 추가

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
        

def main():
    app = QApplication(sys.argv)

    # 스타일 시트 적용
    with open(r'D:\g_Project\2023_skillup_chatting\Kay\Client\view\static\login.qss', 'r', encoding='utf-8') as f:
        app.setStyleSheet(f.read())

    loginWindow = LoginWindow()
    loginWindow.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
