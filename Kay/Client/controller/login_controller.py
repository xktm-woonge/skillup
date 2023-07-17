# controller/login_controller.py

from PyQt5.QtCore import QObject, pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout, QMessageBox

try:
    from controller import *
    from model.check_re import validate_email
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from controller import *
    from model.check_re import validate_email


class LoginController(QObject):
    def __init__(self, client_thread):
        super().__init__()
        self.client_thread = client_thread

        self.main_widget = QWidget()  # 부모 위젯 생성
        self.stacked_widget = QStackedWidget()  # QStackedWidget 생성

        self.login_window = LoginWindow()
        self.register_controller = RegisterController(self.client_thread)
        
        self.stacked_widget.addWidget(self.login_window)  # 로그인 창 페이지 추가
        self.stacked_widget.addWidget(self.register_controller.register_window)  # 회원가입 창 페이지 추가

        layout = QVBoxLayout(self.main_widget)
        layout.addWidget(self.stacked_widget)
        layout.setContentsMargins(0, 0, 0, 0)

        self.main_widget.setFixedSize(400, 650)  # 창의 크기를 고정
        self.main_widget.setWindowFlags(self.main_widget.windowFlags() & ~Qt.WindowMaximizeButtonHint)  # 최대화 버튼 제거
        self.main_widget.show()
        
        self.connect_slot()
        
    def connect_slot(self):
        self.login_window.registerButton.clicked.connect(self.show_register_window)
        self.login_window.loginButton.clicked.connect(self.handle_login)
        self.register_controller.back_button_clicked.connect(self.show_login_window)
        self.client_thread.login_success.connect(self.handle_login_success)
        self.client_thread.login_fail.connect(self.handle_login_fail)

    @pyqtSlot()
    def show_register_window(self):
        self.register_controller.back_button_was_clicked = False
        self.stacked_widget.setCurrentIndex(1)  # 회원가입 창 페이지로 전환

    @pyqtSlot()
    def show_login_window(self):
        self.stacked_widget.setCurrentIndex(0)  # 로그인 창 페이지로 전환

    @pyqtSlot()
    def handle_login(self):
        if not self.login_window.emailField.text():
            QMessageBox.warning(
                self.login_window,
                "이메일 체크",
                "이메일을 입력해 주세요."
            )
            self.login_window.emailField.setFocus()
            return
        
        if not validate_email(self.login_window.emailField.text()):
            QMessageBox.warning(
                self.login_window,
                "이메일 양식 체크",
                "이메일 양식이 틀렸습니다."
            )
            self.login_window.emailField.setFocus()
            return
            
        if not self.login_window.passwordField.text():
            QMessageBox.warning(
                self.login_window,
                "비밀번호 체크",
                "비밀번호를 입력해 주세요."
            )
            self.login_window.passwordField.setFocus()
            return
            
        self.client_thread.login(self.login_window.emailField.text(),
                                 self.login_window.passwordField.text())
        
    @pyqtSlot()
    def handle_login_success(self):
        QMessageBox.information(
                self.login_window,
                "로그인",
                "로그인에 성공했습니다."
            )
        
    @pyqtSlot()
    def handle_login_fail(self):
        QMessageBox.warning(
                self.login_window,
                "로그인",
                "아이디와 비밀번호가 일치하지 않습니다."
            )