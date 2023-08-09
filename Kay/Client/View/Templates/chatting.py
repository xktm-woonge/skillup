# ./view/templates/chatting.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, \
                            QHBoxLayout, QApplication, QDesktopWidget
from PyQt5.QtCore import Qt, QFile
from PyQt5.QtGui import QIcon, QPixmap, QImage, QPainter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.Qt import QSize, QSizePolicy
from xml.etree import ElementTree
import re
from pathlib import Path
import sys


class SidebarWidget(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedWidth(50)

    def enterEvent(self, event):
        self.setFixedWidth(150)
        self.parent().expandSidebar()
        QWidget.enterEvent(self, event)

    def leaveEvent(self, event):
        self.setFixedWidth(50)
        self.parent().collapseSidebar()
        QWidget.leaveEvent(self, event)


class ChattingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.sidebar_width = 50
        self.middle_width = 300
        self.right_width = 900
        self.height = 600

        self.sidebar_icon_size = (30, 30)
        self.sidebar_button_size = (50, 50)

        # Keep track of the current selected button
        self.currentButton = None

        self.sidebar_expanded = False
        self.sidebar_labels = []

        self.initUI()

        # Initialize labels as hidden
        self.notification_label.hide()
        self.friend_list_label.hide()
        self.chat_window_label.hide()
        self.profile_setting_label.hide()
        self.setup_label.hide()

        self.connect_slot()

    def initUI(self):
        hbox = QHBoxLayout()
        hbox.setContentsMargins(0, 0, 0, 0)
        hbox.setSpacing(0)

        # Side Bar
        side_bar = SidebarWidget(self)
        side_bar.setObjectName('sidebar')

        side_layout = QVBoxLayout(side_bar)
        side_layout.setContentsMargins(0, 0, 0, 0)  # Side layout border gap removal
        side_layout.setSpacing(0)  # Gap removal between widgets inside side layout

        notification_icon_path = f'{Path(__file__).parents[1]}/static/icon/-notifations-none_90255.svg'
        notification_icon = QIcon(notification_icon_path)
        self.notification_button = QPushButton()
        self.notification_button.setIcon(notification_icon)
        self.notification_button.setIconSize(QSize(*self.sidebar_icon_size))
        self.notification_button.setFixedSize(*self.sidebar_button_size)
        self.notification_button.setProperty('icon_path', notification_icon_path)

        friend_list_icon_path = f'{Path(__file__).parents[1]}/static/icon/account_multiple_outline_icon_140049.svg'
        friend_list_icon = QIcon(friend_list_icon_path)
        self.friend_list_button = QPushButton()
        self.friend_list_button.setIcon(friend_list_icon)
        self.friend_list_button.setIconSize(QSize(*self.sidebar_icon_size))
        self.friend_list_button.setFixedSize(*self.sidebar_button_size)
        self.friend_list_button.setProperty('icon_path', friend_list_icon_path)

        chat_window_icon_path = f'{Path(__file__).parents[1]}/static/icon/message_text_outline_icon_139369.svg'
        chat_window_icon = QIcon(chat_window_icon_path)
        self.chat_window_button = QPushButton()
        self.chat_window_button.setIcon(chat_window_icon)
        self.chat_window_button.setIconSize(QSize(*self.sidebar_icon_size))
        self.chat_window_button.setFixedSize(*self.sidebar_button_size)
        self.chat_window_button.setProperty('icon_path', chat_window_icon_path)

        self.profile_setting_button = QPushButton()
        self.profile_setting_button.setFixedSize(50, 50)
        
        # 온라인 상태를 표시하기 위한 QLabel 추가
        self.status_label = QLabel()
        self.status_label.setFixedSize(10, 10)
        self.status_label.move(5, 5)  # 상태 원의 위치를 조정합니다
        self.status_label.setParent(self.profile_setting_button)

        setup_path = f'{Path(__file__).parents[1]}/static/icon/cog_outline_icon_139752.svg'
        setup_icon = QIcon(setup_path)
        self.setup_button = QPushButton()
        self.setup_button.setIcon(setup_icon)
        self.setup_button.setIconSize(QSize(*self.sidebar_icon_size))
        self.setup_button.setFixedSize(*self.sidebar_button_size)
        self.setup_button.setProperty('icon_path', setup_path)

        self.notification_button.setObjectName('notification_button')
        self.friend_list_button.setObjectName('friend_list_button')
        self.chat_window_button.setObjectName('chat_window_button')
        self.profile_setting_button.setObjectName('profile_setting_button')
        self.setup_button.setObjectName('setup_button')

        self.notification_label = QLabel('알림', self)
        self.sidebar_labels.append(self.notification_label)

        self.friend_list_label = QLabel('친구 목록', self)
        self.sidebar_labels.append(self.friend_list_label)

        self.chat_window_label = QLabel('대화 내용', self)
        self.sidebar_labels.append(self.chat_window_label)

        self.profile_setting_label = QLabel('내 정보', self)
        self.sidebar_labels.append(self.profile_setting_label)

        self.setup_label = QLabel('설정', self)
        self.sidebar_labels.append(self.setup_label)

        # Notification button with label
        notification_hbox = QHBoxLayout()
        notification_hbox.addWidget(self.notification_button)
        notification_hbox.addWidget(self.notification_label)
        side_layout.addLayout(notification_hbox)

        # Friend list button with label
        friend_list_hbox = QHBoxLayout()
        friend_list_hbox.addWidget(self.friend_list_button)
        friend_list_hbox.addWidget(self.friend_list_label)
        side_layout.addLayout(friend_list_hbox)

        # Chat window button with label
        chat_window_hbox = QHBoxLayout()
        chat_window_hbox.addWidget(self.chat_window_button)
        chat_window_hbox.addWidget(self.chat_window_label)
        side_layout.addLayout(chat_window_hbox)

        # Profile setting button
        profile_setting_hbox = QHBoxLayout()
        profile_setting_hbox.addWidget(self.profile_setting_button)
        profile_setting_hbox.addWidget(self.profile_setting_label)
        side_layout.addLayout(profile_setting_hbox)

        # Add widgets to the side layout
        side_layout.addStretch(1)

        setup_hbox = QHBoxLayout()
        setup_hbox.addWidget(self.setup_button)
        setup_hbox.addWidget(self.setup_label)
        side_layout.addLayout(setup_hbox)

        # Middle Area
        middle_area_widget = QWidget()
        middle_area_widget.setFixedSize(self.middle_width, self.height)
        middle_area_widget.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.middle_area = QVBoxLayout(middle_area_widget)
        self.middle_area.setContentsMargins(0, 0, 0, 0)  # Middle layout border gap removal
        self.middle_area.setSpacing(0)  # Gap removal between widgets inside middle layout
        middle_label = QLabel('Middle Area', self)
        self.middle_area.addWidget(middle_label)

        # Chat Screen
        right_area_widget = QWidget()
        self.right_area = QVBoxLayout(right_area_widget)
        right_area_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.right_area.setContentsMargins(0, 0, 0, 0)  # Chat screen layout border gap removal
        self.right_area.setSpacing(0)  # Gap removal between widgets inside chat screen layout
        chat_label = QLabel('Chat Screen', self)
        self.right_area.addWidget(chat_label)


        hbox.addWidget(side_bar)
        hbox.addWidget(middle_area_widget)
        hbox.addWidget(right_area_widget)

        self.setLayout(hbox)
        self._setStyle()

        self.setWindowTitle('WeChat Style')
        self.setGeometry(300, 300, 1250, 600)  # Adjusted as per your requirement
        self.setMinimumSize(QSize(1250, 600))
        self.show()

    def connect_slot(self):
        self.notification_button.clicked.connect(self.handleButtonClicked)
        self.friend_list_button.clicked.connect(self.handleButtonClicked)
        self.chat_window_button.clicked.connect(self.handleButtonClicked)

    def change_svg_color(self, path, color):
        tree = ElementTree.parse(path)
        root = tree.getroot()

        # SVG의 네임스페이스 정의
        namespaces = {'ns': 'http://www.w3.org/2000/svg'}

        for element in root.findall(".//ns:path", namespaces):
            element.attrib['fill'] = color  # 직접 'fill' 속성을 설정합니다.

        # 변환된 XML을 문자열로 변환
        xml = ElementTree.tostring(root, encoding='unicode')

        renderer = QSvgRenderer()
        renderer.load(bytearray(xml.encode('utf-8')))

        image = QImage(35, 35, QImage.Format_ARGB32)
        image.fill(Qt.transparent)

        painter = QPainter(image)
        renderer.render(painter)
        painter.end()

        pixmap = QPixmap.fromImage(image)
        return QIcon(pixmap)
        
    def handleButtonClicked(self):
        button = self.sender()

        if self.currentButton is not None:
            icon_path = self.currentButton.property('icon_path')
            icon = QIcon(icon_path)
            self.currentButton.setIcon(icon)
            self.currentButton.setStyleSheet("")

        icon_path = button.property('icon_path')
        clicked_icon = self.change_svg_color(icon_path, "#FFFFFF")  # 흰색으로 변경
        button.setIcon(clicked_icon)
        button.setStyleSheet("background-color: rgb(79, 42, 184);")

        self.currentButton = button

    def expandSidebar(self):
        for label in self.sidebar_labels:
            label.show()

    def collapseSidebar(self):
        for label in self.sidebar_labels:
            label.hide()

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
    ex = ChattingWindow()
    sys.exit(app.exec_())
