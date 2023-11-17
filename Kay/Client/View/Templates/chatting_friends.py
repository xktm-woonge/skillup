# ./view/templates/friend_list_widget.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QApplication
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
from PyQt5.QtCore import Qt, pyqtSignal, QSize, QUrl
from PyQt5.QtGui import QPixmap, QPainter, QImage, qGray
from pathlib import Path
import sys
import validators

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
    image_loaded_signal = pyqtSignal(QPixmap)

    def __init__(self, name, image_path, status, parent=None):
        super(FriendWidget, self).__init__(parent)
        self.setObjectName("FriendWidget")
        self.image_path = image_path
        self.status = status
        self.setFixedSize(275, 70)

        layout = QHBoxLayout(self)
        # 프로필 이미지
        self.img_label = QLabel(self)
        layout.addWidget(self.img_label)

        # 이름과 상태
        self.name_label = QLabel(name, self)
        self.name_label.setFont(font.NOTOSAN_FONT_BOLD)
        layout.addWidget(self.name_label)
        layout.addStretch(1)

        self.setLayout(layout)

        # Load the profile picture from the network
        self.load_profile_picture()

        # Connect the signal for when the image is loaded
        self.image_loaded_signal.connect(self.set_profile_picture)

    def load_profile_picture(self):
        # Check if the image path is a valid URL
        if validators.url(self.image_path):
            request = QNetworkRequest(QUrl(self.image_path))
            manager = QNetworkAccessManager()
            manager.finished.connect(self.on_image_load)
            manager.get(request)
        else:
            # Assume it is a local file path
            self.set_profile_picture(QPixmap(self.image_path))

    def on_image_load(self, reply):
        img_data = reply.readAll()
        pixmap = QPixmap()
        if pixmap.loadFromData(img_data):
            # Emit the signal with the loaded pixmap
            self.image_loaded_signal.emit(pixmap)
        else:
            print("Failed to load image from network.")

    def set_profile_picture(self, pixmap):
        # If the status is offline, convert the image to grayscale
        if self.status == 'offline':
            image = pixmap.toImage()
            for x in range(image.width()):
                for y in range(image.height()):
                    color = image.pixelColor(x, y)
                    gray = qGray(color.rgb())
                    color.setRed(gray)
                    color.setGreen(gray)
                    color.setBlue(gray)
                    image.setPixelColor(x, y, color)
            pixmap = QPixmap.fromImage(image)

        # Resize and set the pixmap
        self.img_label.setPixmap(pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation))

    def set_offline_style(self):
        # 이미지 회색조 처리는 이미 set_profile_picture 함수에서 수행됨
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

    def add_friend(self, name, image_path, status):
        widget = FriendWidget(name, image_path, status)
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
    friend_list_widget.add_friend("John Doe", f'{Path(__file__).parents[1]}/static/img/background.png', "online")
    friend_list_widget.add_friend("John Doe", f'{Path(__file__).parents[1]}/static/img/background.png', "online")
    friend_list_widget.add_friend("John Doe", f'{Path(__file__).parents[1]}/static/img/background.png', "online")
    friend_list_widget.add_friend("John Doe", f'{Path(__file__).parents[1]}/static/img/background.png', "offline")
    friend_list_widget.add_friend("John Doe", f'{Path(__file__).parents[1]}/static/img/background.png', "offline")
    friend_list_widget.add_friend("John Doe", f'{Path(__file__).parents[1]}/static/img/background.png', "offline")
    friend_list_widget.add_friend("John Doe", f'{Path(__file__).parents[1]}/static/img/background.png', "offline")
    friend_list_widget.add_friend("John Doe", f'{Path(__file__).parents[1]}/static/img/background.png', "offline")
    friend_list_widget.add_friend("John Doe", f'{Path(__file__).parents[1]}/static/img/background.png', "offline")
    friend_list_widget.add_friend("John Doe", f'{Path(__file__).parents[1]}/static/img/background.png', "offline")

    friend_list_widget.show()
    sys.exit(app.exec_())