import os
import sys
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFile, Qt, QSize
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QLabel, QDesktopWidget

try:
    from templates import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))

    from templates import *

class RegisterWindow(QWidget):
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        super().__init__()

        BUTTON_HEIGHT = 80
        ID_NOTICE = "영문으로 시작하는 영문, 숫자 조합 6~20자리"
        PASSWORD_NOTICE = "영문, 숫자, 특수 문자가 포함 8~16자리"
        NAME_NOTICE = "이름을 입력해주세요."
        EMAIL_NOTICE = "이메일 주소를 입력해주세요."

        self.setWindowTitle('Chatting')

        # 메인창 위치
        self.setGeometry(0, 0, 400, 600)
        self.setFixedSize(400, 600)
        self._moveToCenter()
        
        layout = QVBoxLayout()

        self.btn_back = HoverButton()
        self.btn_back.setIcon(QIcon("../static/back_icon.png"))
        self.btn_back.setIconSize(QSize(16, 16))

        layout.addWidget(self.btn_back)
        layout.setAlignment(self.btn_back, Qt.AlignLeft)

        label_signup = QLabel("REGISTER")
        label_signup.setObjectName("label_signup")
        layout.addWidget(label_signup)

        hboxLayout_send_email = QHBoxLayout()
        self.lineEdit_email = QLineEdit()
        self.lineEdit_email.setObjectName("lineEdit")
        self.lineEdit_email.setPlaceholderText("이메일")
        self.lineEdit_email.setFixedWidth(300)
        hboxLayout_send_email.addWidget(self.lineEdit_email)

        self.btn_request_verification_code = HoverButton("인증 요청")
        hboxLayout_send_email.addWidget(self.btn_request_verification_code)
        layout.addLayout(hboxLayout_send_email)

        hboxLayout_comfirm_email = QHBoxLayout()
        self.lineEdit_verification_code = QLineEdit()
        self.lineEdit_verification_code.setObjectName("lineEdit")
        self.lineEdit_verification_code.setPlaceholderText("인증 번호")
        self.lineEdit_verification_code.setFixedWidth(300)
        hboxLayout_comfirm_email.addWidget(self.lineEdit_verification_code)

        self.btn_verify_verification_code = HoverButton("확인")
        hboxLayout_comfirm_email.addWidget(self.btn_verify_verification_code)
        layout.addLayout(hboxLayout_comfirm_email)

        self.label_email_notice = QLabel(EMAIL_NOTICE)
        self.label_email_notice.setObjectName("notice")
        layout.addWidget(self.label_email_notice)
        
        self.lineEdit_pwd = QLineEdit()
        self.lineEdit_pwd.setObjectName("lineEdit")
        self.lineEdit_pwd.setPlaceholderText("비밀번호")
        layout.addWidget(self.lineEdit_pwd)

        self.label_pwd_notice = QLabel(PASSWORD_NOTICE)
        self.label_pwd_notice.setObjectName("notice")
        layout.addWidget(self.label_pwd_notice)

        self.lineEdit_confirm_pwd = QLineEdit()
        self.lineEdit_confirm_pwd.setObjectName("lineEdit")
        self.lineEdit_confirm_pwd.setPlaceholderText("비밀번호 확인")
        layout.addWidget(self.lineEdit_confirm_pwd)

        self.lineEdit_name = QLineEdit()
        self.lineEdit_name.setObjectName("lineEdit")
        self.lineEdit_name.setPlaceholderText("닉네임")
        layout.addWidget(self.lineEdit_name)

        self.label_name_notice = QLabel(NAME_NOTICE)
        self.label_name_notice.setObjectName("notice")
        layout.addWidget(self.label_name_notice)

        self.btn_register = HoverButton("REGISTER")
        self.btn_register.setFixedHeight(BUTTON_HEIGHT)
        self.btn_register.setObjectName("btn_register")
        layout.addWidget(self.btn_register)

        self._setStyle()
        self.setLayout(layout)

    def _moveToCenter(self):
        # 获取屏幕的矩形
        screenRect = QDesktopWidget().screenGeometry()

        # 获取窗口的矩形
        windowRect = self.frameGeometry()

        # 计算居中位置
        x = (screenRect.width() - windowRect.width()) // 2
        y = (screenRect.height() - windowRect.height()) // 2

        # 移动窗口
        self.move(x, y)

    def _setStyle(self):
        current_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(current_path)

        qss_file = QFile('../Static/signup.qss')
        qss_file.open(QFile.ReadOnly | QFile.Text)
        style_sheet = qss_file.readAll()
        self.setStyleSheet(str(style_sheet, encoding='utf-8'))


if __name__ == '__main__':
    app = QApplication([])
    loginWindow = RegisterWindow()
    loginWindow.show()
    app.exec_()
    print('aa')