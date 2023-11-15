# ./view/templates/friend_list_widget.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QApplication
from PyQt5.QtCore import Qt, pyqtSignal, QSize
from PyQt5.QtGui import QPixmap, QIcon
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

    def __init__(self, name, image_path, status, parent=None):
        super(FriendWidget, self).__init__(parent)
        self.setFixedSize(275, 70)

        layout = QHBoxLayout(self)
        # 프로필 이미지
        self.img_label = QLabel(self)
        pixmap = QPixmap(image_path).scaled(50, 50, Qt.KeepAspectRatio)  # 프로필 이미지 스케일링
        self.img_label.setPixmap(pixmap)
        layout.addWidget(self.img_label)

        # 이름과 상태
        self.name_label = QLabel(name, self)
        # self.name_label.setFont(font.NOTOSAN_FONT_BOLD)
        layout.addWidget(self.name_label)

        # 온라인 상태 표시
        if status == 'online':
            self.status_label = QLabel(self)
            self.status_label.setStyleSheet("QLabel { background-color: green; border-radius: 5px; }")
            layout.addWidget(self.status_label)

        self.setLayout(layout)

    def set_offline_style(self):
        # 이미지 회색조 처리
        self.img_label.setStyleSheet("QLabel { background-color: #C0C0C0; }")
        # 텍스트 회색조 처리
        self.name_label.setStyleSheet("QLabel { color: #C0C0C0; }")

class FriendListWidget(QWidget):
    def __init__(self, parent=None):
        super(FriendListWidget, self).__init__(parent)
        
        self.setFixedSize(300, 600)
        
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)

        # 친구 목록 헤더
        header = QWidget(self)
        header.setFixedHeight(50)
        header_layout = QHBoxLayout(header)
        header_label = QLabel("친구목록", header)
        # header_label.setFont(font.NOTOSAN_FONT_BOLD)
        header_layout.addWidget(header_label)

        add_button = QPushButton(header)
        add_icon = QIcon(f'{Path(__file__).parents[1]}/static/icon/add.svg')  # 실제 경로로 변경
        add_button.setIcon(add_icon)
        add_button.setIconSize(QSize(24, 24))
        add_button.setFixedSize(30, 30)
        header_layout.addWidget(add_button)

        layout.addWidget(header)

        # 친구 목록 스크롤 영역
        self.scroll_area = QScrollArea(self)
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area_widget = QWidget()
        self.scroll_area.setWidget(self.scroll_area_widget)
        self.friend_list_layout = QVBoxLayout(self.scroll_area_widget)
        self.friend_list_layout.setAlignment(Qt.AlignTop)
        layout.addWidget(self.scroll_area)

        self.online_label = QLabel("온라인", self)  # 온라인 구분자 추가
        # self.online_label.setFont(font.NOTOSAN_FONT_MEDIUM)  # 폰트 설정
        self.online_label.setStyleSheet("color: #000000;")  # 색상 설정
        self.friend_list_layout.addWidget(self.online_label)

        self.offline_label = QLabel("오프라인", self)  # 오프라인 구분자 추가
        # self.offline_label.setFont(font.NOTOSAN_FONT_MEDIUM)  # 폰트 설정
        self.offline_label.setStyleSheet("color: #C0C0C0;")  # 색상 설정

        self.setLayout(layout)
        self._setStyle()

    def _setStyle(self):
        with open(f'{Path(__file__).parents[1]}/static/friend_list.qss', 'r', encoding='utf-8') as file:
            qss = file.read()
            self.setStyleSheet(qss)

    def add_friend(self, name, image_path, status):
        widget = FriendWidget(name, image_path, status)
        if status == 'online':
            self.friend_list_layout.insertWidget(self.friend_list_layout.count() - 1, widget)
        else:
            if not hasattr(self, 'offline_added'):
                self.friend_list_layout.addWidget(self.offline_label)  # 오프라인 라벨 추가
                setattr(self, 'offline_added', True)
            self.friend_list_layout.addWidget(widget)
            widget.set_offline_style()


if __name__ == '__main__':
    # font.Init()
    app = QApplication(sys.argv)
    friend_list_widget = FriendListWidget()

    # 친구 위젯 추가 테스트
    friend_list_widget.add_friend("John Doe", r"D:\python_project\chatting_program\Kay\Client\view\static\img\back.png", "online")
    friend_list_widget.add_friend("Jane Doe", r"D:\python_project\chatting_program\Kay\Client\view\static\img\back.png", "offline")

    friend_list_widget.show()
    sys.exit(app.exec_())