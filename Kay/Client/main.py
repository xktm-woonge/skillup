from PyQt5.QtWidgets import QApplication
from View.Templates.login import LoginWindow
from View.Templates.register import RegisterWindow
from Controller.login_controller import LoginController
from Controller.register_controller import RegisterController


if __name__ == '__main__':
    app = QApplication([])
    loginWindow = LoginWindow()
    loginController = LoginController(loginWindow)
    registerView = RegisterWindow()
    registerController = RegisterController(registerView)
    # loginView.show()
    app.exec_()