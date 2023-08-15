import sys
from pathlib import Path
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QScrollArea, QPushButton, QHBoxLayout, QApplication, QSlider
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont, QPixmap, QIcon
from PyQt5.Qt import QSize

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
        
        self.middle_width = 300
        header_height = 50
        self.height = 600
        self.more_icon_size = (30, 30)
        self.more_button_size = (30, 30)
        header_font = get_NotoSan_font()
        
        self.setFixedWidth(self.middle_width)
        self.setMinimumHeight(self.height)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Header
        header = QWidget(self)
        header.setFixedSize(self.middle_width, header_height)
        header.setObjectName("header")
        header_layout = QHBoxLayout()
        header_label = QLabel(" 알림")
        header_label.setFont(header_font)
        header_label.setObjectName('header_label')

        # ON/OFF Slider
        self.toggle_slider = QSlider(Qt.Horizontal, self)
        self.toggle_slider.setFixedWidth(25)
        self.toggle_slider.setRange(0, 1)
        self.toggle_slider.setObjectName("toggle_slider")
        
        self.toggle_slider.valueChanged.connect(self.on_toggle_changed)

        more_icon_path = f'{Path(__file__).parents[1]}/static/icon/-more-horiz_90225.svg'
        more_icon_white = change_svg_color(more_icon_path, "#FFFFFF")  # 흰색으로 변경
        self.more_button = QPushButton()
        self.more_button.setIcon(more_icon_white)
        self.more_button.setIconSize(QSize(*self.more_icon_size))
        self.more_button.setFixedSize(*self.more_button_size)
        self.more_button.setProperty('icon_path', more_icon_path)
        self.more_button.setObjectName('more_button')

        header_layout.addWidget(header_label)
        header_layout.addWidget(self.toggle_slider)
        header_layout.addStretch(1)  # 중앙 공백 추가
        header_layout.addWidget(self.more_button)
        header.setLayout(header_layout)
        layout.addWidget(header)

        # Notifications Area
        notifications_area = QWidget(self)
        self.notifications_layout = QVBoxLayout()
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(notifications_area)
        notifications_area.setLayout(self.notifications_layout)
        layout.addWidget(self.scroll_area)

        self.setLayout(layout)
        self._setStyle()
            
    def on_toggle_changed(self, value):
        pass
        # if value == 0:
        #     self.toggle_label.setText("OFF")
        # else:
        #     self.toggle_label.setText("ON")
        
    def _setStyle(self):
        with open(f'{Path(__file__).parents[1]}/static/chatting_notifications.qss', 'r', encoding='utf-8') as file:
            qss = file.read()
            self.setStyleSheet(qss)

        self.more_button.setCursor(Qt.PointingHandCursor)
        self.toggle_slider.setCursor(Qt.PointingHandCursor)


if __name__ == "__main__": 
    app = QApplication(sys.argv)
    window = NotificationsListWidget()
    # Example Notifications
    for i in range(10):
        notification = NotificationWidget('image.png', 'Title', 'Content Content Content Content Content', '2023-08-13')
        window.notifications_layout.addWidget(notification)
    window.show()
    sys.exit(app.exec_())
