from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QListWidget, \
                            QTextEdit, QHBoxLayout, QApplication, QDesktopWidget
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.Qt import QSize, QSizePolicy
from pathlib import Path
import sys

class MyApp(QWidget):
    def __init__(self):
        super().__init__()

        self.sidebar_width = 50
        self.middle_width = 300
        self.right_width = 900
        self.height = 600

        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)  # Main layout border gap removal
        hbox.setSpacing(0)  # Gap removal between widgets inside main layout

        # Side Bar
        side_bar = QWidget()
        side_bar.setObjectName('sidebar')
        side_bar.setFixedWidth(self.sidebar_width)  # setFixedSize를 이용하여 크기 고정

        side_layout = QVBoxLayout(side_bar)
        side_layout.setContentsMargins(0, 0, 0, 0)  # Side layout border gap removal
        side_layout.setSpacing(0)  # Gap removal between widgets inside side layout

        notification_icon = self.set_sidebar_icon(
            f'{Path(__file__).parents[1]}/static/img/sidebar_notification_icon.png')
        self.notification_button = QPushButton(notification_icon, "")
        self.notification_button.setFixedSize(50, 50)
        friend_list_icon = self.set_sidebar_icon(
            f'{Path(__file__).parents[1]}/static/img/sidebar_friends_icon.png')
        self.friend_list_button = QPushButton(friend_list_icon, "")
        self.friend_list_button.setFixedSize(50, 50)
        chat_window_icon = self.set_sidebar_icon(
            f'{Path(__file__).parents[1]}/static/img/sidebar_chatting_icon.png')
        self.chat_window_button = QPushButton(chat_window_icon, "")
        self.chat_window_button.setFixedSize(50, 50)
        profile_setting_icon = self.set_sidebar_icon(
            f'{Path(__file__).parents[1]}/static/img/sidebar_chatting_icon.png')
        self.profile_setting_button = QPushButton(profile_setting_icon, "")
        self.profile_setting_button.setFixedSize(50, 50)

        self.notification_button.setObjectName('notification_button')
        self.friend_list_button.setObjectName('friend_list_button')
        self.chat_window_button.setObjectName('chat_window_button')
        self.profile_setting_button.setObjectName('profile_setting_button')

        # Add widgets to the side layout
        side_layout.addWidget(self.notification_button, 0, Qt.AlignTop)
        side_layout.addWidget(self.friend_list_button, 0, Qt.AlignTop)
        side_layout.addWidget(self.chat_window_button, 0, Qt.AlignTop)
        side_layout.addWidget(self.profile_setting_button, 0, Qt.AlignTop)
        side_layout.addStretch(1)

        middle_area = QVBoxLayout()
        middle_area.setContentsMargins(0, 0, 0, 0)  # Middle layout border gap removal
        middle_area.setSpacing(0)  # Gap removal between widgets inside middle layout
        middle_btn = QPushButton('Middle Area', self)
        middle_area.addWidget(middle_btn)

        chat_screen = QVBoxLayout()
        chat_screen.setContentsMargins(0, 0, 0, 0)  # Chat screen layout border gap removal
        chat_screen.setSpacing(0)  # Gap removal between widgets inside chat screen layout
        chat_btn = QPushButton('Chat Screen', self)
        chat_screen.addWidget(chat_btn)

        hbox.addWidget(side_bar)
        hbox.addLayout(middle_area)
        hbox.addLayout(chat_screen)

        self.setLayout(hbox)
        self._setStyle()

        self.setWindowTitle('WeChat Style')
        self.setGeometry(300, 300, 1250, 600)  # Adjusted as per your requirement
        self.show()

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
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
