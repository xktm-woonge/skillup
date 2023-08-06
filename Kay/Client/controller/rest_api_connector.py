# ./controller/rest_api_connector.py

from PyQt5.QtCore import QThread, pyqtSignal
import json

try:
    from model.rest_api import RestClient
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from model.rest_api import RestClient
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
        self.client = RestClient('localhost', 8000)

    def request_verification_code(self, email):
        result = self.client.request_verification_code(email)
        if result['status'] == 'FAIL':
            self.send_email_fail.emit(result['message'])
        elif result['status'] == 'DUPLICATE':
            self.duplicate_registration.emit(result['message'])

    def verify_verification_code(self, email, verification_code):
        result = self.client.verify_verification_code(email, verification_code)
        if result['status'] == 'SUCCESS':
            self.verify_success.emit(result['message'])
        elif result['status'] == 'FAIL':
            self.verify_fail.emit(result['message'])

    def register_user(self, email, password, salt):
        result = self.client.register_user(email, password, salt)
        if result['status'] == 'SUCCESS':
            self.register_success.emit(result['message'])

    def login(self, email, password):
        result = self.client.login(email, password)
        if result['status'] == 'SUCCESS':
            self.login_success.emit(result['data'])
        elif result['status'] == 'FAIL':
            self.login_fail.emit(result['message'])
        elif result['status'] == 'UNREGISTERED':
            self.non_existent_email.emit(result['message'])
