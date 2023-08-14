try:
    from view.templates.login import LoginWindow
    from view.templates.register import RegisterWindow
    from view.templates.chatting_main import ChattingWindow
    from view.templates.alertBox import warningBox, informationBox
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))
    from view.templates.login import LoginWindow
    from view.templates.register import RegisterWindow
    from view.templates.chatting_main import ChattingWindow
    from view.templates.alertBox import warningBox, informationBox


__all__ = [
    "LoginWindow",
    "RegisterWindow",
    "warningBox",
    "informationBox",
    "ChattingWindow",
]