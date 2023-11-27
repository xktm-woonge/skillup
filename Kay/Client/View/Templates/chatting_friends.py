# ./view/templates/friend_list_widget.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QApplication, QDialog, QLineEdit
from PyQt5.QtCore import Qt, pyqtSignal, QSize, QEvent
from PyQt5.QtGui import QPixmap, QPainter, QImage, qGray
from pathlib import Path
import sys

try:
    from utils import *
except ImportError:
    sys.path.append(str(Path(__file__).parents[2]))
    from utils import *


class AddFriendDialog(QDialog):
    friend_added_signal = pyqtSignal(str)

    def __init__(self, parent=None):
        super(AddFriendDialog, self).__init__(parent)
        
        # '?' 버튼 제거 및 닫기 버튼만 남김
        self.setWindowFlags(self.windowFlags() & ~Qt.WindowContextHelpButtonHint)

        self.setWindowTitle("친구 추가")
        self.setFixedSize(280, 120)  # 창 크기 조정

        self.layout = QVBoxLayout(self)

        # 이름 입력 필드
        self.name_input = QLineEdit(self)
        self.name_input.setFixedHeight(40)  # 높이 조정
        self.layout.addWidget(self.name_input)

        # 버튼 레이아웃
        button_layout = QHBoxLayout()
        self.add_button = QPushButton("추가", self)
        self.cancel_button = QPushButton("취소", self)

        # 버튼 높이 조정
        self.add_button.setFixedHeight(40)
        self.cancel_button.setFixedHeight(40)
        
        # 버튼 스타일 설정
        self.add_button.setStyleSheet("QPushButton { border: 1px solid black; }")
        self.cancel_button.setStyleSheet("QPushButton { border: 1px solid black; }")

        button_layout.addWidget(self.add_button)
        button_layout.addWidget(self.cancel_button)
        self.layout.addLayout(button_layout)

        # 시그널 연결
        self.add_button.clicked.connect(self.add_friend)
        self.cancel_button.clicked.connect(self.close)

    def add_friend(self):
        name = self.name_input.text()
        if name:
            self.friend_added_signal.emit(name)
        self.close()



class FriendWidget(QWidget):
    # 사용자 정의 신호 생성, 필요한 경우 사용
    friend_action_signal = pyqtSignal(str)
    doubleClicked = pyqtSignal(str, str, str)

    def __init__(self, name, email, image_path, status, parent=None):
        super(FriendWidget, self).__init__(parent)
        self.setObjectName("FriendWidget")
        self.image_path = image_path
        self.status = status

        # 전체 위젯에 대한 QHBoxLayout
        outer_layout = QHBoxLayout(self)
        self.setFixedSize(275, 70)

        # 내부 위젯 생성 및 스타일 설정
        self.inner_widget = QWidget()
        self.inner_widget.setObjectName("InnerWidget")
        layout = QHBoxLayout(self.inner_widget)
        outer_layout.addWidget(self.inner_widget)

        # 프로필 이미지
        self.img_label = QLabel(self.inner_widget)
        self.img_label.setPixmap(self.modify_image())
        layout.addWidget(self.img_label)

        # 이름과 이메일 레이블에 대한 참조를 저장합니다.
        self.name_label = QLabel(name, self.inner_widget)
        self.email_label = QLabel(email, self.inner_widget)

        # 이름과 상태, 이메일 레이아웃 추가
        name_status_layout = QVBoxLayout()  # 이름과 상태, 이메일을 수직 레이아웃에 추가
        name_status_layout.addWidget(self.name_label)
        name_status_layout.addWidget(self.email_label)
        layout.addLayout(name_status_layout)  # 기존 수평 레이아웃에 수직 레이아웃 추가

        layout.addStretch(1)

        # 마우스 hover 이벤트 설정
        self.inner_widget.installEventFilter(self)

    def modify_image(self):
        # 이미지를 로드하고 크기를 조정합니다.
        pixmap = QPixmap(self.image_path)
        pixmap = pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        # 회색조 처리를 여기에서 수행합니다.
        if self.status == 'offline':
            image = pixmap.toImage()
            image = image.convertToFormat(QImage.Format_Grayscale8)
            pixmap = QPixmap.fromImage(image)

        return pixmap

    def set_offline_style(self):
        self.inner_widget.setStyleSheet("QLabel { color: #C0C0C0; }")

    # 이벤트 필터를 사용하여 마우스 hover 시 변경 사항을 적용
    def eventFilter(self, source, event):
        if source == self.inner_widget:
            if event.type() == QEvent.Enter:
                self.setStyleSheet("background-color: lightgrey;")  # 배경색 변경
            elif event.type() == QEvent.Leave:
                self.setStyleSheet("background-color: none;")  # 원래 스타일로 복구
        return super().eventFilter(source, event)
    
    def mouseDoubleClickEvent(self, event):
        # 더블 클릭 시그널을 발생시킵니다.
        self.doubleClicked.emit(self.name_label.text(), self.email_label.text(), self.image_path)

class FriendListWidget(QWidget):
    new_friend_added = pyqtSignal(str)

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
        self.add_button.clicked.connect(self.show_add_friend_dialog)

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

    def show_add_friend_dialog(self):
        self.dialog = AddFriendDialog(self)
        self.dialog.friend_added_signal.connect(self.new_friend_added.emit)
        self.dialog.show()
        
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