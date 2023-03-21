import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parents[0]))
sys.path.append(str(Path(__file__).parents[1]))

from View.Templates.login import LoginWindow
from View.Templates.register import RegisterWindow
import login_controller
import register_controller

__all__ = [
    "LoginWindow",
    "RegisterWindow",
    "login_controller",
    "register_controller"
]