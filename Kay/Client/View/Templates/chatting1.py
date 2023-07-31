from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, \
                            QTextEdit, QHBoxLayout, QApplication, QDesktopWidget
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.Qt import QSize, QSizePolicy
from pathlib import Path


class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.sidebar_width = 50
        self.middle_width = 300
        self.right_width = 900
        self.height = 600

        # Set Window Properties
        self.setGeometry(0, 0, 1250, 600)  # Width: 72 + 500 + 1350, Height: 960
        self.setWindowTitle('Chat Application')
        self.setMinimumSize(QSize(1250, 600))
        self._moveToCenter()

        # Define Layouts
        main_layout = QHBoxLayout()
        main_layout.setContentsMargins(0, 0, 0, 0)

        # Define Widgets
        self.side_bar = QWidget()
        self.side_bar.setObjectName('sidebar')
        self.side_bar.setFixedWidth(self.sidebar_width)
        self.side_bar.setContentsMargins(0, 0, 0, 0)

        chat_list = QWidget()
        chat_list.setFixedWidth(self.middle_width)

        chat_screen = QWidget()

        # Side Bar
        side_layout = QVBoxLayout(self.side_bar)
        side_layout.setSpacing(0)

        notification_icon = self.set_sidebar_icon(f'{Path(__file__).parents[1]}/static/img/sidebar_notification_icon.png')
        self.notification_button = QPushButton(notification_icon, "")
        self.notification_button.setFixedSize(50, 50)
        friend_list_icon = self.set_sidebar_icon(f'{Path(__file__).parents[1]}/static/img/sidebar_friends_icon.png')
        self.friend_list_button = QPushButton(friend_list_icon, "")
        self.friend_list_button.setFixedSize(50, 50)
        chat_window_icon = self.set_sidebar_icon(f'{Path(__file__).parents[1]}/static/img/sidebar_chatting_icon.png')
        self.chat_window_button = QPushButton(chat_window_icon, "")
        self.chat_window_button.setFixedSize(50, 50)
        profile_setting_icon = self.set_sidebar_icon(f'{Path(__file__).parents[1]}/static/img/sidebar_chatting_icon.png')
        self.profile_setting_button = QPushButton(profile_setting_icon, "")
        self.profile_setting_button.setFixedSize(50, 50)

        # Add widgets to the side layout
        side_layout.addWidget(self.notification_button, 0, Qt.AlignTop)
        side_layout.addWidget(self.friend_list_button, 0, Qt.AlignTop)
        side_layout.addWidget(self.chat_window_button, 0, Qt.AlignTop)
        side_layout.addWidget(self.profile_setting_button, 0, Qt.AlignTop)
        side_layout.addStretch(1)

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

    def set_sidebar_icon(self, image_path):
        pixmap = QPixmap(image_path)
        pixmap_resized = pixmap.scaled(self.sidebar_width, self.sidebar_width, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon = QIcon(pixmap_resized)
        return icon
        
    def _setStyle(self):
        qss_file = QFile(f'{Path(__file__).parents[1]}/static/chatting.qss')
        qss_file.open(QFile.ReadOnly | QFile.Text)
        style_sheet = qss_file.readAll()
        self.setStyleSheet(str(style_sheet, encoding='utf-8'))

    def _moveToCenter(self):
        # 获取屏幕的矩形
        screenRect = QDesktopWidget().screenGeometry()

        # 获取窗口的矩形
        windowRect = self.frameGeometry()

        # 计算居中位置
        x = (screenRect.width() - windowRect.width()) // 2
        y = (screenRect.height() - windowRect.height()) // 2

        # 移动窗口
        self.move(x, y)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    win = ChatWindow()
    win.show()

    sys.exit(app.exec_())
