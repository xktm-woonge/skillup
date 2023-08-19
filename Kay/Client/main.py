# ./main.py

from PyQt5.QtWidgets import QApplication
from controller.login_controller import LoginController
from controller.rest_api_connector import RestApiThread
from utils import *

if __name__ == '__main__':
    app = QApplication([])
    clmn.Init()
    font.Init()
    api_thread = RestApiThread(RESTAPI_URL)
    login_controller = LoginController(api_thread)

    app.exec_()