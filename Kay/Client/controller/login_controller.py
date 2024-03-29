# controller/login_controller.py

from PyQt5.QtCore import QObject, pyqtSlot, Qt
from PyQt5.QtWidgets import QWidget, QStackedWidget, QVBoxLayout

try:
    from controller.register_controller import RegisterController
    from controller.chatting_controller import ChattingController
    from view.templates import *
    from model.check_re import validate_email
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from controller.register_controller import RegisterController
    from controller.chatting_controller import ChattingController
    from view.templates import *
    from model.check_re import validate_email


class LoginController(QObject):
    def __init__(self, api_thread):
        super().__init__()
        self.api_thread = api_thread

        self.main_widget = QWidget()  # 부모 위젯 생성
        self.stacked_widget = QStackedWidget()  # QStackedWidget 생성

        self.login_window = LoginWindow()
        self.register_controller = RegisterController(self.api_thread)
        
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
        self.api_thread.login_success.connect(self.handle_login_success)
        self.api_thread.login_fail.connect(self.handle_login_fail)
        self.api_thread.non_existent_email.connect(self.handle_non_existent_email)
        
        # Enter key press event on emailField and passwordField
        self.login_window.emailField.returnPressed.connect(self.login_window.loginButton.click)
        self.login_window.passwordField.returnPressed.connect(self.login_window.loginButton.click)

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
            msg = "이메일을 입력해 주세요."
            warningBox(self.login_window, msg)
            self.login_window.emailField.setFocus()
            return
        
        if not validate_email(self.login_window.emailField.text()):
            msg = "이메일 양식이 틀렸습니다."
            warningBox(self.login_window, msg)
            self.login_window.emailField.setFocus()
            return
            
        if not self.login_window.passwordField.text():
            msg = "비밀번호를 입력해 주세요."
            warningBox(self.login_window, msg)
            self.login_window.passwordField.setFocus()
            return
            
        self.api_thread.execute('login', 
                                self.login_window.emailField.text(),
                                self.login_window.passwordField.text())
        
    def handle_login_success(self, token):
        result = self.api_thread.get_userInfo(self.login_window.emailField.text(), 
                                        token)
                                        
        if result.get('status') == 'SUCCESS':
            # Create an instance of the chatting window and display it
            self.chatting_controller = ChattingController(
                self.login_window.emailField.text(), result.get('data'), token, self.api_thread)
            self.main_widget.close()
        else:
            warningBox(self.login_window, result.get('message'))
        
    def handle_login_fail(self, msg):
        warningBox(self.login_window, msg)
        
    def handle_non_existent_email(self, msg):
        warningBox(self.login_window, msg)