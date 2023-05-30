
# from PyQt5.QtCore import QObject, pyqtSlot
# from PyQt5.QtWidgets import QLineEdit, QMessageBox, QApplication
# import re
# import smtplib
# import random
# from email.mime.text import MIMEText
# from email.header import Header

# from Controller import *

# class RegisterController(QObject):
#     login_controller = None

#     def __init__(self, window:RegisterWindow):
#         super().__init__()
#         self.register_window = window
#         # self.register_window = registerView
#         # self.email = self.register_window.lineEdit_send_email.text()
#         self.register_window.btn_back.clicked.connect(self.show_login_window)
#         # self.register_window.show()
#         # self.register_window.btn_send_email.clicked.connect(self.send_verifyCode)

#     @pyqtSlot()
#     def show_login_window(self):
#         lineEdits = self.register_window.findChildren(QLineEdit, "lineEdit")
#         for lineEdit in lineEdits:
#             lineEdit.clear()

#         # x = self.register_window.pos().x()
#         # y = self.register_window.pos().y()
#         # self.register_window.hide()
#         # self.login_window.move(x, y)
#         self.register_window.close()

#         # if not RegisterController.login_controller:
#         self.login_window = LoginWindow()
#         # self.register_window.close()
#         if not RegisterController.login_controller:
#             RegisterController.login_controller = LoginController(self.login_window)
#         else:
#             RegisterController.login_controller.login_window = self.login_window
#         self.login_window.show()
#         # self.login_window.show()

# #     @pyqtSlot()
# #     def send_verifyCode(self):
# #         if not is_valid_email(self.email):
# #             QMessageBox.warning(self, "错误", "请输入一个合法的邮箱地址")
# #             return
# #         else:
# #             code = ''.join([str(random.randint(0, 9)) for _ in range(6)])

# #             # 邮件内容
# #             message = MIMEText(f"您的验证码是：{code}", 'plain', 'utf-8')
# #             message['From'] = Header("聊天软件", 'utf-8')
# #             message['To'] = Header(self.email, 'utf-8')
# #             message['Subject'] = Header("邮箱验证", 'utf-8')

# #             # 发送邮件
# #             try:
# #                 smtp_obj = smtplib.SMTP('smtp.gmail.com', 587)
# #                 smtp_obj.starttls()
# #                 smtp_obj.login('youremail@gmail.com', 'yourpassword')
# #                 smtp_obj.sendmail('youremail@gmail.com', email, message.as_string())
# #                 smtp_obj.quit()
# #                 print("邮件发送成功")
# #                 return code
# #             except smtplib.SMTPException as e:
# #                 print("邮件发送失败:", e)

# # def is_valid_email(email):
# #     """
# #     验证邮箱地址是否合法
# #     """
# #     pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
# #     return re.match(pattern, email) is not None





from PyQt5.QtCore import QObject, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import QLineEdit
from Model.client_model import Client
from Controller import *

class RegisterController(QObject):
    back_button_clicked = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.register_window = RegisterWindow()
        self.register_window.btn_back.clicked.connect(self.back_button_clicked)
        self.register_window.btn_send_email.connect(self.send_verification_request)

    def show_register(self):
        self.register_window.show()

    def close(self):
        lineEdits = self.register_window.findChildren(QLineEdit, "lineEdit")
        for lineEdit in lineEdits:
            lineEdit.clear()
        self.register_window.close()

    @pyqtSlot()
    def send_verification_request(self):
        client = Client('localhost', 8000)
        client.connect()
        client.send_verification_code(self.register_window.lineEdit_send_email.text())