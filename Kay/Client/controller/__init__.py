# try:
from controller.login_controller import LoginController
from controller.register_controller import RegisterController
from controller.chatting_controller import ChattingController
from controller.rest_api_connector import RestApiThread

# except ImportError:
#     import sys
#     from pathlib import Path
#     sys.path.append(str(Path(__file__).parents[1]))
#     from controller.login_controller import LoginController
#     from controller.register_controller import RegisterController

__all__ = [
    "LoginController",
    "RegisterController",
    "ChattingController",
    "RestApiThread",
]