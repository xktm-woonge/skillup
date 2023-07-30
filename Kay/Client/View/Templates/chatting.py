from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, QTextEdit, QHBoxLayout, QStackedWidget, QApplication
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.Qt import QSize
from pathlib import Path


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set Window Properties
        self.setGeometry(100, 100, 1250, 600)  # Width: 72 + 500 + 1350, Height: 960
        self.setWindowTitle('Chat Application')
        self.setMinimumSize(QSize(1250, 600))

        # Define Layouts
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Set sizes of each layout
        sidebar_size = QSize(50, 600)
        middle_size = QSize(300, 600)
        right_size = QSize(900, 600)

        # Define Widgets
        self.side_bar = QWidget()
        self.side_bar.setObjectName('sidebar')
        self.side_bar.setFixedSize(sidebar_size)

        chat_list = QWidget()
        chat_list.setFixedSize(middle_size)

        chat_screen = QWidget()

        # Side Bar
        side_layout = QVBoxLayout(self.side_bar)

        self.notification_button = QPushButton(QIcon(QPixmap(f'{Path(__file__).parents[1]}/static/img/sidebar_notification_icon.png')), "")
        self.friend_list_button = QPushButton(QIcon(QPixmap(f'{Path(__file__).parents[1]}/static/img/sidebar_friends_icon.png')), "")
        self.chat_window_button = QPushButton(QIcon(QPixmap(f'{Path(__file__).parents[1]}/static/img/sidebar_chatting_icon.png')), "")
        self.chat_window_button.setStyleSheet("border: none;")
        self.profile_setting_button = QPushButton(QIcon(QPixmap(f'{Path(__file__).parents[1]}/static/img/sidebar_chatting_icon.png')), "")

        # Add widgets to the side layout
        side_layout.addWidget(self.notification_button, 0, Qt.AlignTop)
        side_layout.addWidget(self.friend_list_button, 0, Qt.AlignTop)
        side_layout.addWidget(self.chat_window_button, 0, Qt.AlignTop)
        side_layout.addWidget(self.profile_setting_button, 0, Qt.AlignTop)

        # Chat list
        chat_layout = QVBoxLayout(chat_list)
        self.chat_list_widget = QListWidget()
        chat_layout.addWidget(self.chat_list_widget)

        # Chat Screen
        chat_screen_layout = QVBoxLayout(chat_screen)
        self.text_edit = QTextEdit()
        self.file_transfer_button = QPushButton("파일 전송")
        self.voice_call_button = QPushButton("음성통화")
        self.video_call_button = QPushButton("영상통화")

        chat_screen_layout.addWidget(self.text_edit)
        chat_screen_layout.addWidget(self.file_transfer_button)
        chat_screen_layout.addWidget(self.voice_call_button)
        chat_screen_layout.addWidget(self.video_call_button)

        # Add Widgets to the Main Layout
        main_layout.addWidget(self.side_bar)
        main_layout.addWidget(chat_list)
        main_layout.addWidget(chat_screen)

        self._setStyle()
        # Set the main layout
        self.setLayout(main_layout)
        
    def _setStyle(self):
        qss_file = QFile(f'{Path(__file__).parents[1]}/static/chatting.qss')
        qss_file.open(QFile.ReadOnly | QFile.Text)
        style_sheet = qss_file.readAll()
        self.setStyleSheet(str(style_sheet, encoding='utf-8'))

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    win = ChatWindow()
    win.show()

    sys.exit(app.exec_())
