from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import Qt


class HoverButton(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setCursor(Qt.PointingHandCursor)
        # self.setStyleSheet("QPushButton:hover { color: white; }")
        
    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)

    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)