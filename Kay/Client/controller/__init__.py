import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[0]))
sys.path.append(str(Path(__file__).parents[1]))

from View.Templates.login import LoginWindow
from View.Templates.register import RegisterWindow
from login_controller import LoginController
from register_controller import RegisterController

__all__ = [
    "LoginWindow",
    "RegisterWindow",
    "LoginController",
    "RegisterController"
]