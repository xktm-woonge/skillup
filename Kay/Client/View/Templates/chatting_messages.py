from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sys
from pathlib import Path

try:
    from utils import *
except ImportError:
    sys.path.append(str(Path(__file__).parents[2]))
    from utils import *


class EnterTextEdit(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)

    def keyPressEvent(self, event):
        if (event.key() in [Qt.Key_Return, Qt.Key_Enter]) and not (event.modifiers() & Qt.ShiftModifier):
            self.parent().send_message()
        else:
            super().keyPressEvent(event)


class MessageBubble(QWidget):
    def __init__(self, text, sender, parent=None):
        super(MessageBubble, self).__init__(parent)
        self.text = self.insert_newlines(text, 70)
        self.sender = sender  # True if the user sent the message, False otherwise
        self.font = QFont()
        self.font.setFamily("Arial")
        self.font.setPointSize(12)
        self.metrics = QFontMetrics(self.font)
        self.padding = 10
        self.bubble_padding = 20  # 텍스트와 말풍선 테두리 사이의 여백
        self.calculateDimensions()

    def calculateDimensions(self):
        # 텍스트의 최대 너비를 설정합니다.
        self.text_max_width = 10000
        # 텍스트 렉트를 계산합니다.
        # Qt.TextWrapAnywhere를 사용하여 글자 단위로 줄바꿈합니다.
        text_rect = self.metrics.boundingRect(0, 0, self.text_max_width, 10000, Qt.TextWrapAnywhere, self.text)
        # 말풍선의 실제 크기를 계산합니다.
        self.bubble_width = text_rect.width() + self.bubble_padding
        self.bubble_height = text_rect.height() + self.bubble_padding + self.metrics.height()
        self.setFixedSize(self.bubble_width, self.bubble_height)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setFont(self.font)

        # Set colors based on who sent the message
        bubble_color = QColor("#4f2ab8") if self.sender else QColor("#D3D3D3")
        text_color = QColor("#FFFFFF") if self.sender else QColor("#000000")

        # Paint the bubble
        painter.setBrush(bubble_color)
        painter.setPen(Qt.NoPen)
        bubble_rect = QRect(0, 0, self.bubble_width, self.bubble_height - self.metrics.height())
        painter.drawRoundedRect(bubble_rect, 10, 10)

        # Paint the text
        painter.setPen(text_color)
        text_rect = QRect(self.bubble_padding // 2, self.bubble_padding // 2, 
                          self.bubble_width - self.bubble_padding, 
                          self.bubble_height - self.bubble_padding - self.metrics.height())
        painter.drawText(text_rect, Qt.AlignLeft | Qt.TextWordWrap, self.text)

        painter.end() 

    def sizeHint(self):
        # Provide a suggested size for the widget based on the text content
        return QSize(self.bubble_width, self.bubble_height)
    
    def insert_newlines(self, text, line_length):
        # 30자마다 줄바꿈을 추가하는 함수
        return '\n'.join(text[i:i+line_length] for i in range(0, len(text), line_length))


class ChattingInterface(QWidget):
    # This signal can be emitted when a new message is received
    new_message = pyqtSignal(str, str, bool)

    def __init__(self, profile_image_path, name, email):
        super().__init__()
        self.profile_image_path = profile_image_path
        self.name = name
        self.email = email
        self.initUI()

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
        top_layout.addStretch(1)
        
        # Middle Area
        self.messages_widget = QWidget()  # 내부 위젯을 먼저 생성
        self.messages_layout = QVBoxLayout(self.messages_widget)  # 내부 위젯에 레이아웃 적용
        self.messages_layout.setAlignment(Qt.AlignTop)
        self.messages_area = QScrollArea()  # 스크롤 영역 생성
        self.messages_area.setWidgetResizable(True)
        self.messages_area.setWidget(self.messages_widget)  # 스크롤 영역에 내부 위젯 설정

        # Bottom Area
        bottom_layout = QHBoxLayout()
        self.message_input = EnterTextEdit(self)
        self.message_input.setFixedHeight(50)
        send_button = QPushButton()
        send_icon = QIcon(f'{Path(__file__).parents[1]}/static/icon/Send.svg')  # SVG 이미지 파일 경로
        send_button.setIcon(send_icon)
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
        # 사용자 메시지를 추가하는 작업을 처리
        message_text = self.message_input.toPlainText()
        if message_text.strip():  # 메시지가 비어있지 않은 경우에만 처리
            # 현재 시간을 가져옵니다.
            current_time = QTime.currentTime().toString("HH:mm")
            self.add_message(message_text, current_time, True)
            self.message_input.clear()
            QApplication.processEvents()
            self.scroll_to_bottom()
            self.new_message.emit(message_text, current_time, True)

            # 입력창에 포커스를 되돌립니다.
            self.message_input.setFocus()

    def add_message(self, message, current_time, is_user):
        # 새 메시지 버블을 생성하고 레이아웃에 추가
        message_bubble = MessageBubble(message, is_user)
        message_bubble.calculateDimensions()
        # 각 메시지를 위한 가로 레이아웃을 생성합니다.
        message_layout = QHBoxLayout()
        current_time_label = QLabel(current_time)
        if is_user:
            # 사용자 메시지인 경우 오른쪽 정렬을 위해 왼쪽에 스트레치를 추가합니다.
            message_layout.addStretch(1)
            message_layout.addWidget(current_time_label)
            message_layout.addWidget(message_bubble)
        else:
            # 다른 사람 메시지인 경우 왼쪽 정렬을 위해 오른쪽에 스트레치를 추가합니다.
            message_layout.addWidget(message_bubble)
            message_layout.addWidget(current_time_label)
            message_layout.addStretch(1)
        
        # 메시지 레이아웃을 메시지 위젯에 추가합니다.
        self.messages_layout.addLayout(message_layout)

        # 이벤트 처리를 강제로 실행하여 위젯을 업데이트합니다.
        QApplication.processEvents()
        
        # 스크롤을 아래로 이동합니다.
        self.scroll_to_bottom()

    def scroll_to_bottom(self):
        # Scroll to the bottom of the messages area
        self.messages_area.verticalScrollBar().setValue(
            self.messages_area.verticalScrollBar().maximum()
        )


if __name__ == '__main__':
    app = QApplication(sys.argv)
    font.Init()
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