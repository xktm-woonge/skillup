# ./main.py
from PyQt5.QtWidgets import QApplication
from controller.connector import ClientThread
from controller.login_controller import LoginController
from utils import *

if __name__ == '__main__':
    app = QApplication([])
    clmn.Init()
    client_thread = ClientThread()
    login_controller = LoginController(client_thread)
    client_thread.start()
    app.exec_()