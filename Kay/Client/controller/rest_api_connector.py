# ./controller/rest_api_connector.py

from PyQt5.QtCore import QThread, pyqtSignal

try:
    from model.rest_api import RESTClient
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from model.rest_api import RESTClient
    from utils import *

class RestApiThread(QThread):
    send_email_success = pyqtSignal(str)
    send_email_fail = pyqtSignal(str)
    verify_success = pyqtSignal(str)
    verify_fail = pyqtSignal(str)
    register_success = pyqtSignal(str)
    duplicate_registration = pyqtSignal(str)
    login_success = pyqtSignal()
    login_fail = pyqtSignal(str)
    non_existent_email = pyqtSignal(str)
    get_userInfo_success = pyqtSignal(dict)
    get_userInfo_fail = pyqtSignal(str)

    def __init__(self, base_url):
        super().__init__()
        self.restClient = RESTClient(base_url)

    def request_verification_code(self, email):
        result = self.restClient.request_verification_code(email)
        if result.get('status') == 'FAIL':
            self.send_email_fail.emit(result['message'])
        elif result.get('status') == 'DUPLICATE':
            self.duplicate_registration.emit(result['message'])

    def verify_verification_code(self, email, verification_code):
        result = self.restClient.verify_verification_code(email, verification_code)
        if result.get('status') == 'SUCCESS':
            self.verify_success.emit(result['message'])
        elif result.get('status') == 'FAIL':
            self.verify_fail.emit(result['message'])

    def register_user(self, email, password, salt):
        result = self.restClient.register_user(email, password, salt)
        if result.get('status') == 'SUCCESS':
            self.register_success.emit(result['message'])

    def login(self, email, password):
        result = self.restClient.login(email, password)
        if result.get('status') == 'SUCCESS':
            self.login_success.emit()
        elif result.get('status') == 'FAIL':
            self.login_fail.emit(result['message'])
        elif result.get('status') == 'UNREGISTERED':
            self.non_existent_email.emit(result['message'])

    def get_userInfo(self, email):
        result = self.restClient.get_userInfo(email)
        return result