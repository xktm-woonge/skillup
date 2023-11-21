from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea, QFrame
)
from PyQt5.QtCore import Qt, pyqtSignal
from PyQt5.QtGui import QPixmap
import sys
from pathlib import Path

class MessageBubble(QLabel):
    def __init__(self, message, timestamp, is_user):
        super().__init__(message)
        self.timestamp = QLabel(timestamp)
        self.is_user = is_user
        self.initUI()

    def initUI(self):
        self.setWordWrap(True)
        self.setFrameStyle(QFrame.StyledPanel)
        self.setStyleSheet("""
            QLabel {
                background-color: #83d0c9;
                border-radius: 10px;
                padding: 5px 10px;
                margin: 5px;
            }
        """)
        self.timestamp.setStyleSheet("font-size: 8pt; color: #555;")

        layout = QVBoxLayout() if self.is_user else QVBoxLayout()
        layout.addWidget(self, alignment=Qt.AlignRight if self.is_user else Qt.AlignLeft)
        layout.addWidget(self.timestamp, alignment=Qt.AlignRight if self.is_user else Qt.AlignLeft)
        self.setLayout(layout)


class ChattingInterface(QWidget):
    # This signal can be emitted when a new message is received
    new_message = pyqtSignal(str, str, bool)

    def __init__(self, profile_image_path, name, email):
        super().__init__()
        self.profile_image_path = profile_image_path
        self.name = name
        self.email = email
        self.initUI()
        self.new_message.connect(self.add_message)

    def initUI(self):
        # Top Area
        top_layout = QHBoxLayout()
        profile_pic_label = QLabel()
        profile_pixmap = QPixmap(self.profile_image_path)
        profile_pic_label.setPixmap(profile_pixmap.scaledToHeight(50))  # Adjust the size as needed
        name_label = QLabel(self.name)
        email_label = QLabel(self.email)
        
        # Arrange name and email vertically
        name_email_layout = QVBoxLayout()
        name_email_layout.addWidget(name_label)
        name_email_layout.addWidget(email_label)

        top_layout.addWidget(profile_pic_label)
        top_layout.addLayout(name_email_layout)
        
        # Middle Area
        self.messages_widget = QWidget()  # 내부 위젯을 먼저 생성
        self.messages_layout = QVBoxLayout(self.messages_widget)  # 내부 위젯에 레이아웃 적용
        self.messages_area = QScrollArea()  # 스크롤 영역 생성
        self.messages_area.setWidgetResizable(True)
        self.messages_area.setWidget(self.messages_widget)  # 스크롤 영역에 내부 위젯 설정

        # Bottom Area
        bottom_layout = QHBoxLayout()
        self.message_input = QLineEdit()
        send_button = QPushButton("Send")
        send_button.clicked.connect(self.send_message)
        bottom_layout.addWidget(self.message_input)
        bottom_layout.addWidget(send_button)

        # Main Layout
        main_layout = QVBoxLayout()
        main_layout.addLayout(top_layout)
        main_layout.addWidget(self.messages_area)  # 스크롤 영역 추가
        main_layout.addLayout(bottom_layout)

        self.setLayout(main_layout)
    
    def send_message(self):
        # Emit the new_message signal with the input text, current timestamp, and True to indicate it's a user message
        self.new_message.emit(self.message_input.text(), "Now", True)
        self.message_input.clear()

    def add_message(self, message, timestamp, is_user):
        # Create a new message bubble and add it to the layout
        message_bubble = MessageBubble(message, timestamp, is_user)
        self.messages_layout.addWidget(message_bubble)
        self.scroll_to_bottom()

    def scroll_to_bottom(self):
        # Scroll to the bottom of the messages area
        self.messages_area.verticalScrollBar().setValue(
            self.messages_area.verticalScrollBar().maximum()
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # 프로필 정보 설정
    profile_image_path = f'{Path(__file__).parents[1]}/static/img/base_profile-removebg-preview.png'
    name = '홍길동'
    email = 'hong@gildong.com'
    
    # ChattingInterface 인스턴스 생성
    chatting_interface = ChattingInterface(profile_image_path, name, email)
    
    # 테스트 메시지 추가
    chatting_interface.add_message('안녕하세요, 채팅 테스트 중입니다.', '10:45 AM', False)
    chatting_interface.add_message('네, 안녕하세요!', '10:46 AM', True)
    
    # 위젯 표시
    chatting_interface.show()
    sys.exit(app.exec_())