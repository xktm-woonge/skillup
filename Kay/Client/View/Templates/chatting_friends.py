# ./view/templates/friend_list_widget.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QApplication
from PyQt5.QtCore import Qt, pyqtSignal, QSize
from PyQt5.QtGui import QPixmap, QPainter, QImage, qGray
from pathlib import Path
import sys

try:
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))
    from utils import *

class FriendWidget(QWidget):
    # 사용자 정의 신호 생성, 필요한 경우 사용
    friend_action_signal = pyqtSignal(str)

    def __init__(self, name, email, image_path, status, parent=None):
        super(FriendWidget, self).__init__(parent)
        self.setObjectName("FriendWidget")
        self.image_path = image_path
        self.status = status
        self.setFixedSize(275, 70)

        layout = QHBoxLayout(self)
        # 프로필 이미지
        self.img_label = QLabel(self)
        self.img_label.setPixmap(self.modify_image())
        layout.addWidget(self.img_label)

        # 이름과 상태
        self.name_label = QLabel(name, self)
        self.name_label.setFont(font.NOTOSAN_FONT_BOLD)
        layout.addWidget(self.name_label)

        # 이메일 라벨 추가
        self.email_label = QLabel(email, self)
        self.email_label.setFont(font.NOTOSAN_FONT_BOLD)  # 폰트 설정 (NOTOSAN_FONT_BOLD보다 작은 폰트 사용)
        self.email_label.setStyleSheet("QLabel { font-size: 10pt; }")  # 폰트 사이즈 조정

        # 이름과 상태, 이메일 레이아웃 추가
        name_status_layout = QVBoxLayout()  # 이름과 상태, 이메일을 수직 레이아웃에 추가
        name_status_layout.addWidget(self.name_label)
        name_status_layout.addWidget(self.email_label)
        layout.addLayout(name_status_layout)  # 기존 수평 레이아웃에 수직 레이아웃 추가

        layout.addStretch(1)

        self.setLayout(layout)

    def modify_image(self):
        # Load the image as QImage for manipulation
        image = QImage(self.image_path)

        # Check if the status is offline to apply the grayscale effect
        if self.status == 'offline':
            for x in range(image.width()):
                for y in range(image.height()):
                    color = image.pixelColor(x, y)
                    # Convert the pixel to grayscale
                    gray = qGray(color.rgb())
                    color.setRed(gray)
                    color.setGreen(gray)
                    color.setBlue(gray)
                    image.setPixelColor(x, y, color)

        # Convert QImage back to QPixmap to display it
        pixmap = QPixmap.fromImage(image)
        output_pixmap = QPixmap(QSize(50, 50))
        output_pixmap.fill(Qt.transparent)  # Fill with transparent background

        # Prepare to draw on the pixmap
        painter = QPainter(output_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)  # For smooth edges
        painter.setRenderHint(QPainter.SmoothPixmapTransform)

        # Draw the main image
        painter.drawPixmap(output_pixmap.rect(), pixmap)

        # Finish drawing
        painter.end()

        # Use or save the resulting image
        return output_pixmap

    def set_offline_style(self):
        # 이미지 회색조 처리
        self.img_label.setStyleSheet("QLabel { background-color: #C0C0C0; }")
        # 텍스트 회색조 처리
        self.name_label.setStyleSheet("QLabel { color: #C0C0C0; }")

class FriendListWidget(QWidget):
    def __init__(self, parent=None):
        super(FriendListWidget, self).__init__(parent)
        
        self.middle_width = 300
        header_height = 50
        self.height = 600
        self.add_icon_size = (30, 30)
        self.add_button_size = (30, 30)
        header_font = font.NOTOSAN_FONT_BOLD
        
        self.setFixedWidth(self.middle_width)
        self.setMinimumHeight(self.height)
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Header
        header = QWidget(self)
        header.setFixedSize(self.middle_width, header_height)
        header.setObjectName("header")
        header_layout = QHBoxLayout()
        header_label = QLabel(" 친구 목록")
        header_label.setFont(header_font)
        header_label.setObjectName('header_label')

        add_icon_path = f'{Path(__file__).parents[1]}/static/icon/add.svg'
        add_icon_white = change_svg_color(add_icon_path, "#FFFFFF")  # 흰색으로 변경
        self.add_button = QPushButton()
        self.add_button.setIcon(add_icon_white)
        self.add_button.setIconSize(QSize(*self.add_icon_size))
        self.add_button.setFixedSize(*self.add_button_size)
        self.add_button.setProperty('icon_path', add_icon_path)
        self.add_button.setObjectName('add_button')

        header_layout.addWidget(header_label)
        # header_layout.addWidget(self.toggle_slider)
        header_layout.addStretch(1)  # 중앙 공백 추가
        header_layout.addWidget(self.add_button)
        header.setLayout(header_layout)
        layout.setSpacing(0)
        layout.addWidget(header)

        # friends_area
        friends_area = QWidget(self)
        self.friends_layout = QVBoxLayout()
        self.friends_layout.setSpacing(0)  
        
        self.friends_layout.setAlignment(Qt.AlignTop)

        # # 오프라인 상태 텍스트 레이블
        # self.offline_label = QLabel("오프라인")
        # self.friends_layout.addWidget(self.offline_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(friends_area)
        friends_area.setLayout(self.friends_layout)
        layout.addWidget(self.scroll_area)

        self.setLayout(layout)
        self._setStyle()
        
    def clear_friends(self):
        for i in reversed(range(self.friends_layout.count())): 
            widget = self.friends_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
    def _setStyle(self):
        with open(f'{Path(__file__).parents[1]}/static/chatting_friends.qss', 'r', encoding='utf-8') as file:
            qss = file.read()
            self.setStyleSheet(qss)

        self.add_button.setCursor(Qt.PointingHandCursor)

    def add_friend(self, name, email, image_path, status):
        widget = FriendWidget(name, email, image_path, status)
        if status == 'online':
            self.friends_layout.insertWidget(self.friends_layout.count() - 1, widget)
        else:
            # if not hasattr(self, 'offline_added'):
            #     self.friends_layout.addWidget(self.offline_label)  # 오프라인 라벨 추가
            #     setattr(self, 'offline_added', True)
            self.friends_layout.addWidget(widget)
            widget.set_offline_style()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    font.Init()
    friend_list_widget = FriendListWidget()

    # 친구 위젯 추가 테스트
    friend_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png', "online")
    friend_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png', "online")
    friend_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png', "online")
    friend_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png', "online")
    friend_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png', "online")
    friend_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png', "offline")
    friend_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png', "offline")
    friend_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png', "offline")
    friend_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png', "offline")
    friend_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png', "offline")

    friend_list_widget.show()
    sys.exit(app.exec_())