from PyQt5.QtWidgets import QApplication
from Controller.login_controller import LoginController

if __name__ == '__main__':
    app = QApplication([])
    login_controller = LoginController()
    app.exec_()