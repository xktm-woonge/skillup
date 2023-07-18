try:
    from controller.auth_controller import AuthController
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from controller.auth_controller import AuthController

__all__ = [
    "AuthController",
]