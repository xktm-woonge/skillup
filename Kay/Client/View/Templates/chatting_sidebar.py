# ./view/templates/chatting_sidebar.py

from PyQt5.QtWidgets import QWidget, QHBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon

try:
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))
    from utils import *


class SidebarWidget(QWidget):
    """사이드바 넓이를 조절하는 class

    Args:
        QWidget (_type_): _description_
    """
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(50)

    def enterEvent(self, event):
        self.setFixedWidth(150)
        self.parent().expandSidebar()
        QWidget.enterEvent(self, event)

    def leaveEvent(self, event):
        self.setFixedWidth(50)
        self.parent().collapseSidebar()
        QWidget.leaveEvent(self, event)
        
        
class ButtonLabelWidget(QWidget):
    """사이드바내 버튼과 레이블을 하나로 묶은 class

    Args:
        QWidget (_type_): _description_
    """
    def __init__(self, button, label, parent=None):
        super().__init__(parent)
        self.button = button
        self.label = label
        self.original_icon = QIcon(self.button.property('icon_path'))  # Save the original icon

        # 이렇게 연결
        self.button.clicked.connect(self.handleButtonClicked)

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove layout border gap
        layout.setSpacing(0)                   # Remove gap between widgets inside the layout
        layout.addWidget(button)
        layout.addWidget(label)

        self.setLayout(layout)

    def handleButtonClicked(self):
        self.parent().parent().handleButtonClicked(self.button)

    def enterEvent(self, event):
        if self.parent().parent().currentButton:
            self.parent().parent().currentButton.setStyleSheet("") 
            if self.parent().parent().currentButton != self.parent().parent().profile_setting_button:
                currentButton_iconPath = self.parent().parent().currentButton.property('icon_path')
                black_icon = change_svg_color(currentButton_iconPath, "#000000")
                self.parent().parent().currentButton.setIcon(black_icon)
            
        if self.button != self.parent().parent().profile_setting_button:
            icon_path = self.button.property('icon_path')
            white_icon = change_svg_color(icon_path, "#FFFFFF")  # 흰색으로 변경
            self.button.setIcon(white_icon)
        self.setStyleSheet("background-color: rgb(79, 42, 184);")
        self.label.setStyleSheet("color: white;")
        self.setCursor(Qt.PointingHandCursor)  # 손모양 커서로 변경
        QWidget.enterEvent(self, event)

    def leaveEvent(self, event):
        if (self.button != self.parent().parent().profile_setting_button and
            self.button != self.parent().parent().currentButton):
            self.button.setIcon(self.original_icon)  # Restore the original icon
        
        if (self.parent().parent().currentButton and
            self.parent().parent().currentButton != self.parent().parent().profile_setting_button):
            currentButton_iconPath = self.parent().parent().currentButton.property('icon_path')
            white_icon = change_svg_color(currentButton_iconPath, "#FFFFFF")
            self.parent().parent().currentButton.setIcon(white_icon)
        
        if self.parent().parent().currentButton:
            self.parent().parent().currentButton.setStyleSheet("background-color: rgb(79, 42, 184);")
            
        self.setStyleSheet("")
        self.label.setStyleSheet("")
        self.setCursor(Qt.ArrowCursor)  # 일반 화살표 커서로 변경
        QWidget.leaveEvent(self, event)