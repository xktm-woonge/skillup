try:
    from controller.login_controller import LoginController
    from controller.register_controller import RegisterController
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from controller.login_controller import LoginController
    from controller.register_controller import RegisterController

__all__ = [
    "LoginController",
    "RegisterController",
]