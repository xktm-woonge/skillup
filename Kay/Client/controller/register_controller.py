# controller/register_controller.py
from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QLineEdit
from controller import *

class RegisterController(QObject):
    back_button_clicked = pyqtSignal()

    def __init__(self, client_thread):
        super().__init__()
        self.client_thread = client_thread
        self.register_window = RegisterWindow()
        self.register_window.backButton.clicked.connect(self.back_button_clicked)
        self.register_window.emailField.getButton().clicked.connect(self.request_verification_code)
        self.register_window.verifyField.getButton().clicked.connect(self.verify_verification_code)

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

    @pyqtSlot()
    def verify_verification_code(self):
        email = self.register_window.emailField.text()
        verification_code = self.register_window.verifyField.text()
        self.client_thread.verify_verification_code(email, verification_code)