
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QLineEdit
from model.client_model import Client
from controller import *

class RegisterController(QObject):
    back_button_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.register_window = RegisterWindow()
        self.register_window.btn_back.clicked.connect(self.back_button_clicked)
        self.register_window.btn_request_verification_code.clicked.connect(self.request_verification_code)
        self.register_window.btn_verify_verification_code.clicked.connect(self.verify_verification_code)

    def show_register(self):
        self.register_window.show()

    def close(self):
        lineEdits = self.register_window.findChildren(QLineEdit, "lineEdit")
        for lineEdit in lineEdits:
            lineEdit.clear()
        self.register_window.close()

    @pyqtSlot()
    def request_verification_code(self):
        client = Client('localhost', 8000)
        client.request_verification_code(self.register_window.lineEdit_email.text())

    @pyqtSlot()
    def verify_verification_code(self):
        client = Client('localhost', 8000)
        client.verify_verification_code(self.register_window.lineEdit_email.text(),
                                        self.register_window.lineEdit_verification_code.text())