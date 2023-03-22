
from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtWidgets import QLineEdit, QMessageBox, QApplication
import re
import smtplib
import random
from email.mime.text import MIMEText
from email.header import Header

from Controller import *

class LoginController(QObject):
    register_controller = None

    def __init__(self, window:LoginWindow):
        super().__init__()
        self.login_window = window
        # self.register_window = RegisterWindow()
        # self.login_window.show()
        self.login_window.btn_register.clicked.connect(self.show_register_window)

    @pyqtSlot()
    def show_register_window(self):
        # lineEdits = self.login_window.findChildren(QLineEdit, "lineEdit")
        # for lineEdit in lineEdits:
        #     lineEdit.clear()

        # x = self.login_window.pos().x()
        # y = self.login_window.pos().y()
        # self.login_window.hide()
        # self.register_window.move(x, y)
        # register_window = RegisterWindow()
        # self.register_window.show()
        self.login_window.close()
        if not LoginController.register_controller:
            self.register_window = RegisterWindow()
            LoginController.register_controller = RegisterController(self.register_window)
        self.register_window.show()