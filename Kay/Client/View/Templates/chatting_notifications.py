import sys
from pathlib import Path
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QPushButton, QHBoxLayout, QApplication, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap

try:
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))
    from utils import *

class NotificationWidget(QWidget):
    def __init__(self, image_path, title, content, date, parent=None):
        super(NotificationWidget, self).__init__(parent)
        self.setFixedSize(290, 85)

        layout = QHBoxLayout()
        layout.setSpacing(10)

        # Image
        img_label = QLabel(self)
        pixmap = QPixmap(image_path)
        img_label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio))
        layout.addWidget(img_label)

        # Text Area
        text_layout = QVBoxLayout()
        title_label = QLabel(title)
        title_label.setFont(QFont('Arial', 10))
        content_label = QLabel(content)
        content_label.setFont(QFont('Arial', 8))
        content_label.setWordWrap(True)
        content_label.setMaximumHeight(34)
        content_label.setScaledContents(True)
        date_label = QLabel(date)
        date_label.setFont(QFont('Arial', 8))
        text_layout.addWidget(title_label)
        text_layout.addWidget(content_label)
        text_layout.addWidget(date_label)
        layout.addLayout(text_layout)

        # Delete Button
        delete_button = QPushButton('X', self)
        delete_button.setFixedSize(15, 15)
        layout.addWidget(delete_button)

        self.setLayout(layout)


class NotificationsListWidget(QWidget):
    def __init__(self, parent=None):
        super(NotificationsListWidget, self).__init__(parent)
        self.setFixedSize(300, 600)
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        header_font = get_NotoSan_font()

        # Header
        header = QWidget(self)
        header.setFixedSize(300, 50)
        header.setObjectName("header")
        header_layout = QHBoxLayout()
        header_label = QLabel(" 알림")
        header_label.setFont(header_font)
        header_label.setObjectName('header_label')

        # ON/OFF Slider
        self.toggle_slider = QSlider(Qt.Horizontal, self)
        self.toggle_slider.setFixedSize(60, 25)
        self.toggle_slider.setRange(0, 1)

        svg_button = QPushButton("SVG")  # Replace this with your SVG button
        header_layout.addWidget(header_label)
        header_layout.addWidget(self.toggle_slider)
        header_layout.addWidget(svg_button)
        header.setLayout(header_layout)
        layout.addWidget(header)

        # Notifications Area
        notifications_area = QWidget(self)
        notifications_layout = QVBoxLayout()
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(notifications_area)
        notifications_area.setLayout(notifications_layout)
        layout.addWidget(scroll_area)

        self.setLayout(layout)
        self._setStyle()

        # Example Notifications
        for i in range(6):
            notification = NotificationWidget('image.png', 'Title', 'Content Content Content Content Content', '2023-08-13')
            notifications_layout.addWidget(notification)
            
    def _setStyle(self):
        with open(f'{Path(__file__).parents[1]}/static/chatting_notifications.qss', 'r', encoding='utf-8') as file:
            qss = file.read()
            self.setStyleSheet(qss)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotificationsListWidget()
    window.show()
    sys.exit(app.exec_())
