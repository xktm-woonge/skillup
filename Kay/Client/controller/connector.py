# controller/connector.py
from PyQt5.QtCore import QThread, pyqtSignal
from model.client_model import Client

class ClientThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.client = Client('192.168.35.167', 8000)

    def run(self):
        self.client.connect()
        # self.client.receive_messages()

    def send_message(self, message):
        self.client.send_message(message)

    def request_verification_code(self, email):
        self.client.request_verification_code(email)

    def verify_verification_code(self, email, verification_code):
        self.client.verify_verification_code(email, verification_code)

    def close(self):
        self.client.close()
