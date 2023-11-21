# ./view/templates/friend_list_widget.py

from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QPushButton, QScrollArea, QApplication
from PyQt5.QtCore import Qt, pyqtSignal, QSize, QEvent
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

class ChatWidget(QWidget):
    doubleClicked = pyqtSignal(str, str, str)

    def __init__(self, name, email, image_path, parent=None):
        super(ChatWidget, self).__init__(parent)
        self.setObjectName("ChatWidget")
        self.image_path = image_path

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

        # 이름과 이메일 레이아웃 추가
        name_email_layout = QVBoxLayout()  # 이름과 이메일을 수직 레이아웃에 추가
        name_email_layout.addWidget(self.name_label)
        name_email_layout.addWidget(self.email_label)
        layout.addLayout(name_email_layout)  # 기존 수평 레이아웃에 수직 레이아웃 추가

        layout.addStretch(1)

        # 마우스 hover 이벤트 설정
        self.inner_widget.installEventFilter(self)

    def modify_image(self):
        # Load the image as a QPixmap
        pixmap = QPixmap(self.image_path)
        pixmap = pixmap.scaled(30, 30, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        return pixmap

    # 이벤트 필터를 사용하여 마우스 hover 시 변경 사항을 적용
    def eventFilter(self, source, event):
        if source == self.inner_widget:
            if event.type() == QEvent.Enter:
                self.setStyleSheet("background-color: lightgrey;")
            elif event.type() == QEvent.Leave:
                self.setStyleSheet("background-color: none;")
        return super().eventFilter(source, event)
    
    def mouseDoubleClickEvent(self, event):
        self.doubleClicked.emit(self.name_label.text(), self.email_label.text(), self.image_path)


class ChatListWidget(QWidget):
    def __init__(self, parent=None):
        super(ChatListWidget, self).__init__(parent)
        
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
        header_label = QLabel(" 채팅 목록")
        header_label.setFont(header_font)
        header_label.setObjectName('header_label')

        header_layout.addWidget(header_label)
        # header_layout.addWidget(self.toggle_slider)
        header_layout.addStretch(1)  # 중앙 공백 추가
        header.setLayout(header_layout)
        layout.setSpacing(0)
        layout.addWidget(header)

        # chatting_list_area
        chatting_list_area = QWidget(self)
        self.chatting_list_layout = QVBoxLayout()
        self.chatting_list_layout.setSpacing(0)  
        
        self.chatting_list_layout.setAlignment(Qt.AlignTop)

        # # 오프라인 상태 텍스트 레이블
        # self.offline_label = QLabel("오프라인")
        # self.chatting_list_layout.addWidget(self.offline_label)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(chatting_list_area)
        chatting_list_area.setLayout(self.chatting_list_layout)
        layout.addWidget(self.scroll_area)

        self.setLayout(layout)
        self._setStyle()
        
    def clear_chatting_list(self):
        for i in reversed(range(self.chatting_list_layout.count())): 
            widget = self.chatting_list_layout.itemAt(i).widget()
            if widget is not None:
                widget.deleteLater()
        
    def _setStyle(self):
        with open(f'{Path(__file__).parents[1]}/static/chatting_message_list.qss', 'r', encoding='utf-8') as file:
            qss = file.read()
            self.setStyleSheet(qss)

    def add_friend(self, name, email, image_path):
        widget = ChatWidget(name, email, image_path)
        self.chatting_list_layout.addWidget(widget)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    font.Init()
    chat_list_widget = ChatListWidget()

    # 친구 위젯 추가 테스트
    chat_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png')
    chat_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png')
    chat_list_widget.add_friend("John Doe", "john@example.com", f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png')

    chat_list_widget.show()
    sys.exit(app.exec_())