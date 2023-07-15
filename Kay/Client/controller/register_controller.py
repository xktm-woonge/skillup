from PyQt5.QtCore import QTimer, QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QLineEdit, QMessageBox
from controller import *

class RegisterController(QObject):
    back_button_clicked = pyqtSignal()
    send_email_fail = pyqtSignal()

    def __init__(self, client_thread):
        super().__init__()
        self.client_thread = client_thread
        self.register_window = RegisterWindow()
        self.register_window.backButton.clicked.connect(self.back_button_clicked)
        self.register_window.emailField.getButton().clicked.connect(self.request_verification_code)
        self.register_window.verifyField.getButton().clicked.connect(self.verify_verification_code)
        self.client_thread.send_email_fail.connect(self.handle_email_sent_failure)
        
        self.back_button_clicked.connect(self.handle_back_button_clicked)
        self.back_button_was_clicked = False  # 새로운 멤버 추가

        self.timer = QTimer()  # 타이머 객체 생성
        self.timer.timeout.connect(self.update_button)  # 타이머 타임아웃 시그널에 슬롯 연결

    @pyqtSlot()
    def request_verification_code(self):
        email = self.register_window.emailField.text()
        # 서버와 연결 확인 후 연결 상태에 따라 다른 동작 실행
        if self.client_thread.client.is_connected:
            self.client_thread.request_verification_code(email)
            self.start_countdown()  # 인증요청 버튼 클릭 시 카운트다운 시작
        else:
            QMessageBox.critical(
                self.register_window,
                "서버 연결 실패",
                "서버에 연결할 수 없습니다. 네트워크 상태를 확인해주세요."
            )

    @pyqtSlot()
    def verify_verification_code(self):
        email = self.register_window.emailField.text()
        verification_code = self.register_window.verifyField.text()
        self.client_thread.verify_verification_code(email, verification_code)

    def start_countdown(self):
        self.register_window.emailField.getButton().setEnabled(False)  # 버튼 비활성화
        self.register_window.emailField.getButton().setProperty("remaining_time", 180)  # 버튼에 남은 시간 속성 설정 (초 단위)
        self.timer.start(1000)  # 타이머 시작, 1초마다 타임아웃 이벤트 발생
        self.register_window.emailField.getButton().setText("03:00")

    def update_button(self):
        remaining_time = self.register_window.emailField.getButton().property("remaining_time")
        if remaining_time <= 0:
            self.register_window.emailField.getButton().setText("인증요청")
            self.register_window.emailField.getButton().setEnabled(True)
            self.timer.stop()  # 타이머 정지
        else:
            remaining_time -= 1
            self.register_window.emailField.getButton().setProperty("remaining_time", remaining_time)
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            self.register_window.emailField.getButton().setText(f"{minutes:02d}:{seconds:02d}")
            
    @pyqtSlot()
    def handle_back_button_clicked(self):
        self.back_button_was_clicked = True
    
    @pyqtSlot()
    def handle_email_sent_failure(self):
        if not self.back_button_was_clicked:
            QMessageBox.critical(
                self.register_window,
                "이메일 전송 실패",
                "이메일 전송에 실패했습니다."
            )

    def reset_verifyButton(self):
        self.timer.stop()  # 타이머 정지
        self.register_window.emailField.getButton().setText("인증요청")
        self.register_window.emailField.getButton().setEnabled(True)  # 버튼 활성화