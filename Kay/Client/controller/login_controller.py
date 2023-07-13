# controller/login_controller.py

from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal, Qt
from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout
from controller import *


class LoginController(QObject):
    def __init__(self, client_thread):
        super().__init__()
        self.client_thread = client_thread

        self.main_widget = QWidget()  # 부모 위젯 생성
        self.stacked_widget = QStackedWidget()  # QStackedWidget 생성

        self.login_window = LoginWindow()
        self.register_controller = RegisterController(self.client_thread)
        self.login_window.registerButton.clicked.connect(self.show_register_window)
        self.register_controller.back_button_clicked.connect(self.show_login_window)

        self.stacked_widget.addWidget(self.login_window)  # 로그인 창 페이지 추가
        self.stacked_widget.addWidget(self.register_controller.register_window)  # 회원가입 창 페이지 추가

        layout = QVBoxLayout(self.main_widget)
        layout.addWidget(self.stacked_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.main_widget.setFixedSize(400, 650)  # 창의 크기를 고정
        self.main_widget.setWindowFlags(self.main_widget.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # 최대화 버튼 제거
        self.main_widget.show()

    @pyqtSlot()
    def show_register_window(self):
        self.stacked_widget.setCurrentIndex(1)  # 회원가입 창 페이지로 전환

    @pyqtSlot()
    def show_login_window(self):
        self.stacked_widget.setCurrentIndex(0)  # 로그인 창 페이지로 전환
