# ./controller/register_controller.py

from PyQt5.QtCore import QTimer, QObject, pyqtSignal, pyqtSlot, Qt
from PyQt5.QtWidgets import QMessageBox, QLineEdit
import os
import hashlib

try:
    from controller import *
    from model.check_re import validate_email
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from controller import *
    from model.check_re import validate_email
    

class RegisterController(QObject):
    back_button_clicked = pyqtSignal()

    def __init__(self, client_thread):
        super().__init__()
        self.client_thread = client_thread
        self.register_window = RegisterWindow()
        self.back_button_was_clicked = False  # 새로운 멤버 추가
        self.verify_email_success = False
        self.timer = QTimer()  # 타이머 객체 생성
        
        self.connect_slot()
        
    def connect_slot(self):
        self.timer.timeout.connect(self.update_button)  # 타이머 타임아웃 시그널에 슬롯 연결
        self.register_window.backButton.clicked.connect(self.handle_back_button_clicked)
        self.register_window.emailField.getButton().clicked.connect(self.request_verification_code)
        self.register_window.verifyField.getButton().clicked.connect(self.verify_verification_code)
        self.register_window.registerButton.clicked.connect(self.send_register)
        self.client_thread.send_email_fail.connect(self.handle_email_sent_failure)
        self.client_thread.verify_success.connect(self.handle_verify_success)
        self.client_thread.verify_fail.connect(self.handle_verify_fail)
        self.client_thread.register_success.connect(self.handle_register_success)
        self.client_thread.duplicate_registration.connect(self.handle_duplicate_registration)
        
    @pyqtSlot()
    def request_verification_code(self):
        email = self.register_window.emailField.text()
        
        if not validate_email(self.register_window.emailField.text()):
            QMessageBox.warning(
                self.register_window,
                "이메일 양식 체크",
                "이메일 양식이 틀렸습니다."
            )
            self.register_window.emailField.setFocus()
            return
        
        # 서버와 연결 확인 후 연결 상태에 따라 다른 동작 실행
        if self.client_thread.client.is_connected:
            self.client_thread.request_verification_code(email)
            self.start_countdown()  # 인증요청 버튼 클릭 시 카운트다운 시작
            self.register_window.verifyField.setEnabled(True)
            self.register_window.verifyField.setFocus()
        else:
            QMessageBox.warning(
                self.register_window,
                "서버 연결 실패",
                "서버에 연결할 수 없습니다. 네트워크 상태를 확인해주세요."
            )

    @pyqtSlot()
    def verify_verification_code(self):
        email = self.register_window.emailField.text()
        verification_code = self.register_window.verifyField.text()
        if not verification_code:
            QMessageBox.warning(
                self.register_window,
                "인증 번호 체크",
                "인증 번호를 입력해 주세요."
            )
            return
        
        self.register_window.verifyField.setEnabled(True)        
        self.client_thread.verify_verification_code(email, verification_code)
        
    @pyqtSlot()
    def handle_verify_success(self):
        self.timer.stop()
        self.register_window.emailField.getButton().setText("인증요청")
        self.register_window.emailField.setEnabled(False)
        self.register_window.verifyField.setEnabled(False)
        QMessageBox.information(
                self.register_window,
                "인증 결과",
                "인증에 성공했습니다."
            )
        self.verify_email_success = True
        
    @pyqtSlot()
    def handle_register_success(self):
        QMessageBox.information(
                self.register_window,
                "회원가입 결과",
                "축하합니다.\n회원가입에 성공했습니다."
            )
        self.handle_back_button_clicked()
        
    @pyqtSlot()
    def handle_duplicate_registration(self):
        self.reset_verifyButton()
        QMessageBox.warning(
                self.register_window,
                "회원가입 결과",
                "이미 가입된 계정입니다."
            )
        self.register_window.verifyField.setEnabled(False)
        self.register_window.emailField.setFocus()
        
    @pyqtSlot()
    def handle_verify_fail(self):
        QMessageBox.warning(
                self.register_window,
                "인증 결과",
                "인증에 실패했습니다. 다시 확인해 주세요."
            )
            
    @pyqtSlot()
    def handle_back_button_clicked(self):
        self.back_button_was_clicked = True
        self.verify_email_success = False
        self.reset_lineEdit()
        self.reset_verifyButton()
        self.reset_toolButton()
        self.back_button_clicked.emit()
    
    @pyqtSlot()
    def handle_email_sent_failure(self, msg):
        self.verify_email_success = False
        self.reset_verifyButton()
        self.register_window.verifyField.setEnabled(False)
        if not self.back_button_was_clicked:
            QMessageBox.warning(
                self.register_window,
                "이메일 전송 실패",
                "이메일 전송에 실패했습니다."
            )
            
    @pyqtSlot()
    def send_register(self):        
        if not self.verify_email_success:
            self.register_window.emailField.setFocus()
            QMessageBox.warning(
                self.register_window,
                "이메일 인증 체크",
                "이메일 인증부터 진행해 주세요."
            )
            self.register_window.passwordField.setFocus()
            return
        
        if not self.register_window.validatePassword():
            QMessageBox.warning(
                self.register_window,
                "password 양식 체크",
                "password 양식이 틀렸습니다."
            )
            self.register_window.passwordField.setFocus()
            return
            
        if not self.register_window.checkpasswordConfirmField():
            QMessageBox.warning(
                self.register_window,
                "password 확인 양식 체크",
                "두번 입력한 password가 상이합니다."
            )
            self.register_window.passwordConfirmField.setFocus()
            return
        
        hashed_password, salt = self.encrypt_password()
        
        self.client_thread.register_user(self.register_window.emailField.text(),
                                         hashed_password, salt)

    def hash_password(self, salt: str) -> str:
        password_bytes = self.register_window.passwordField.text().encode('utf-8')
        salt_bytes = salt.encode('utf-8')
        return hashlib.pbkdf2_hmac('sha256', password_bytes, salt_bytes, 100000).hex()
        
    def encrypt_password(self):
        # Generate a salt
        salt = os.urandom(16).hex()

        # Hash the password with the salt
        hashed_password = self.hash_password(salt)
        return hashed_password, salt
        
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
            self.register_window.verifyField.setEnabled(False)
            self.timer.stop()  # 타이머 정지
        else:
            remaining_time -= 1
            self.register_window.emailField.getButton().setProperty("remaining_time", remaining_time)
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            self.register_window.emailField.getButton().setText(f"{minutes:02d}:{seconds:02d}")
            
    def reset_verifyButton(self):
        self.timer.stop()  # 타이머 정지
        self.register_window.emailField.getButton().setText("인증요청")
        self.register_window.emailField.getButton().setEnabled(True)  # 버튼 활성화
        
    def reset_toolButton(self):
        self.register_window.tb_checkPasswordLength.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.register_window.tb_checkPasswordContain.setToolButtonStyle(Qt.ToolButtonTextOnly)
        self.register_window.tb_checkPasswordLength.setStyleSheet("border: none; color:gray")
        self.register_window.tb_checkPasswordContain.setStyleSheet("border: none; color:gray")
        
    def reset_lineEdit(self):
        lineEdits = self.register_window.findChildren(QLineEdit)
        for lineEdit in lineEdits:
            lineEdit.clear()
        self.register_window.emailField.setEnabled(True)
        self.register_window.verifyField.setEnabled(False)
        self.register_window.passwordField.setStyleSheet("")
        self.register_window.passwordConfirmField.setStyleSheet("")