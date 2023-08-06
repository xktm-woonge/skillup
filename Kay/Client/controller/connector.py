# ./controller/connector.py

from PyQt5.QtCore import QThread, pyqtSignal
import json

try:
    from model.rest_api import Client
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from model.rest_api import Client
    from utils import *
    

class RestApiThread(QThread):
    send_email_success = pyqtSignal(str)
    send_email_fail = pyqtSignal(str)
    verify_success = pyqtSignal(str)
    verify_fail = pyqtSignal(str)
    register_success = pyqtSignal(str)
    duplicate_registration = pyqtSignal(str)
    login_success = pyqtSignal(dict)
    login_fail = pyqtSignal(str)
    non_existent_email = pyqtSignal(str)
    
    def __init__(self):
        super().__init__()
        self.client = Client('localhost', 8000, self.handle_message_received)

    def run(self):
        self.client.connect()

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

    def handle_message_received(self, received_message):
        str_received_message = json.loads(received_message)
        command = str_received_message['command']
        status = str_received_message['status']
        message = str_received_message['message']
        data = str_received_message['data']

        if command == 'VERIFICATIONCODE':
            if status == 'FAIL':
                self.send_email_fail.emit(message)
            elif status == 'DUPLICATE':
                self.duplicate_registration.emit(message)
        elif command == 'VERIFY':
            if status == 'SUCCESS':
                self.verify_success.emit(message)
            elif status == 'FAIL':
                self.verify_fail.emit(message)
        elif command == 'LOGIN':
            if status == 'SUCCESS':
                self.login_success.emit(data)
            elif status == 'FAIL':
                self.login_fail.emit(message)
            elif status == 'UNREGISTERED':
                self.non_existent_email.emit(message)
        elif command == 'REGISTER' and status == 'SUCCESS':
            self.register_success.emit(message)