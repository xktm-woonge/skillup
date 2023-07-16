# controller/connector.py

from PyQt5.QtCore import QThread, pyqtSignal
from model.client_model import Client

class ClientThread(QThread):
    message_received = pyqtSignal(str)
    send_email_success = pyqtSignal()
    send_email_fail = pyqtSignal()
    verify_success = pyqtSignal()
    verify_fail = pyqtSignal()
    register_success = pyqtSignal()
    duplicate_registration = pyqtSignal()
    login_success = pyqtSignal()
    login_fail = pyqtSignal()
    

    def __init__(self):
        super().__init__()
        self.client = Client('192.168.35.2', 8000, self.handle_message_received)

    def run(self):
        self.client.connect()
        # self.client.receive_messages()

    def send_message(self, message):
        self.client.send_message(message)

    def request_verification_code(self, email):
        self.client.request_verification_code(email)

    def verify_verification_code(self, email, verification_code):
        self.client.verify_verification_code(email, verification_code)
        
    def register_user(self, email, password, salt):
        self.client.register_user(email, password, salt)
        
    def login(self, email, password):
        self.client.login(email, password)

    def close(self):
        self.client.close()

    def handle_message_received(self, message):
        if message == 'Send email fail':
            self.send_email_fail.emit()
        elif message == 'Verification successful':
            self.verify_success.emit()
        elif message == 'Verification failed':
            self.verify_fail.emit()
        elif message == 'Register successful':
            self.register_success.emit()
        elif message == 'The account has already been registered':
            self.duplicate_registration.emit()
        elif message == 'Login successful':
            self.login_success.emit()
        elif message == 'Login fail':
            self.login_fail.emit()