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

        self.timer = QTimer()  # 타이머 객체 생성
        self.timer.timeout.connect(self.update_button)  # 타이머 타임아웃 시그널에 슬롯 연결

    def show_register(self):
        self.register_window.show()

    def close(self):
        lineEdits = self.register_window.findChildren(QLineEdit, "lineEdit")
        for lineEdit in lineEdits:
            lineEdit.clear()
        self.register_window.close()

    @pyqtSlot()
    def request_verification_code(self):
        email = self.register_window.emailField.text()
        self.client_thread.request_verification_code(email)
        self.start_countdown()  # 인증요청 버튼 클릭 시 카운트다운 시작

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

    def handle_email_sent_failure(self):
        QMessageBox.critical(
            self.register_window,
            "이메일 전송 실패",
            "이메일 전송에 실패했습니다."
        )