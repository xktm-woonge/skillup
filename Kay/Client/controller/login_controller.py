from PyQt5.QtCore import QObject, pyqtSlot, pyqtSignal
from PyQt5.QtWidgets import QMessageBox
from Controller import *

class LoginController(QObject):
    def __init__(self):
        super().__init__()
        self.login_window = LoginWindow()
        self.register_controller = RegisterController()
        self.login_window.btn_register.clicked.connect(self.show_register_window)
        self.register_controller.back_button_clicked.connect(self.show_login_window)
        self.login_window.show()

    @pyqtSlot()
    def show_register_window(self):
        self.login_window.close()
        self.register_controller.show_register()

    @pyqtSlot()
    def show_login_window(self):
        self.register_controller.close()
        self.login_window.show()
