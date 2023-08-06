# ./main.py
from PyQt5.QtWidgets import QApplication
from controller.login_controller import LoginController
from model.rest_api import RESTClient
from utils import *

if __name__ == '__main__':
    app = QApplication([])
    clmn.Init()
    base_url = "http://yourserver.com/api"  # 서버의 REST API 엔드포인트 주소
    rest_client = RESTClient(base_url)
    login_controller = LoginController(rest_client)
    app.exec_()