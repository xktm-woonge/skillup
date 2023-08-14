# ./view/templates/chatting_main.py

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QLabel, \
                            QApplication, QDesktopWidget, QStackedWidget
from PyQt5.QtCore import QFile, pyqtSlot
from PyQt5.QtGui import QIcon
from PyQt5.Qt import QSize, QSizePolicy
from pathlib import Path
import sys

try:
    from utils import *
    from view.templates.chatting_sidebar import SidebarWidget
    from view.templates.chatting_sidebar import ButtonLabelWidget
    from view.templates.chatting_notifications import NotificationsListWidget
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))
    from utils import *
    from view.templates.chatting_sidebar import SidebarWidget
    from view.templates.chatting_sidebar import ButtonLabelWidget
    from view.templates.chatting_notifications import NotificationsListWidget


class ChattingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.sidebar_width = 50
        self.middle_width = 300
        self.right_width = 900
        self.height = 600

        self.sidebar_icon_size = (25, 25)
        self.sidebar_button_size = (50, 50)
        
        self.font = get_NotoSan_font()
        self.font.setPointSize(12)

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

    def initUI(self):

        # Side Bar
        self.sidebar = SidebarWidget(self)
        self.sidebar.setGeometry(0, 0, self.sidebar_width, self.height)
        # Sidebar 스타일
        self.sidebar.setStyleSheet("""
            background-color: white;
        """)

        side_layout = QVBoxLayout(self.sidebar)
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

        self.notification_label = QLabel('  알림', self)
        self.notification_label.setFont(self.font)
        self.notification_label.setObjectName('notification_label')
        self.sidebar_labels.append(self.notification_label)

        self.friend_list_label = QLabel('  친구 목록', self)
        self.friend_list_label.setFont(self.font)
        self.friend_list_label.setObjectName('friend_list_label')
        self.sidebar_labels.append(self.friend_list_label)

        self.chat_window_label = QLabel('  대화 내용', self)
        self.chat_window_label.setFont(self.font)
        self.chat_window_label.setObjectName('chat_window_label')
        self.sidebar_labels.append(self.chat_window_label)

        self.profile_setting_label = QLabel('  내 정보', self)
        self.profile_setting_label.setFont(self.font)
        self.profile_setting_label.setObjectName('profile_setting_label')
        self.sidebar_labels.append(self.profile_setting_label)

        self.setup_label = QLabel('  설정', self)
        self.setup_label.setFont(self.font)
        self.setup_label.setObjectName('setup_label')
        self.sidebar_labels.append(self.setup_label)

        # Notification button with label
        self.notification_button_label_widget = ButtonLabelWidget(
            self.notification_button, self.notification_label)
        side_layout.addWidget(self.notification_button_label_widget)

        # Friend list button with label
        self.friend_list_button_label_widget = ButtonLabelWidget(
            self.friend_list_button, self.friend_list_label)
        side_layout.addWidget(self.friend_list_button_label_widget)

        # Chat window button with label
        self.chat_window_button_label_widget = ButtonLabelWidget(
            self.chat_window_button, self.chat_window_label)
        side_layout.addWidget(self.chat_window_button_label_widget)

        # Profile setting button
        self.profile_setting_button_label_widget = ButtonLabelWidget(
            self.profile_setting_button, self.profile_setting_label, self)
        side_layout.addWidget(self.profile_setting_button_label_widget)

        # Add widgets to the side layout
        side_layout.addStretch(1)

        self.setup_button_label_widget = ButtonLabelWidget(
            self.setup_button, self.setup_label)
        side_layout.addWidget(self.setup_button_label_widget)
        
        # Middle Area
        self.middle_area_widget = QStackedWidget(self)
        self.middle_area_widget.setGeometry(50, 0, self.middle_width, self.height)
        
        # 예시로 NotificationsListWidget을 추가합니다.
        # 다른 위젯도 여기에 추가하면 됩니다.
        self.notifications_list_widget = NotificationsListWidget()
        self.middle_area_widget.addWidget(self.notifications_list_widget)
        
        # Right Area
        self.right_area_widget = QStackedWidget(self)
        self.right_area_widget.setGeometry(50 + self.middle_width, 0, self.right_width, self.height)
        
        # 예시로 QLabel을 추가합니다. 실제로 필요한 위젯을 추가하세요.
        self.right_area_widget.addWidget(QLabel('Right Area', self))

        self._setStyle()

        self.setWindowTitle('Chatting')
        self.setGeometry(300, 300, 1250, 600)  # Adjusted as per your requirement
        self.setMinimumSize(QSize(1250, 600))
        self.show()
        
    def connect_slot(self):
        self.notification_button.clicked.connect(self.show_notifications)

    @pyqtSlot()
    def show_notifications(self):
        self._clear_middle_right_areas()
        self.middle_area_widget.setCurrentWidget(self.notifications_list_widget)
        # Similarly, add a widget to the right area if needed
    
    def _clear_middle_right_areas(self):
        # Clear widgets in middle_area and right_area
        self.middle_area_widget.setCurrentIndex(-1)
        self.right_area_widget.setCurrentIndex(-1)
        
    def handleButtonClicked(self, button):
        if button != self.profile_setting_button:
            if self.currentButton is not None:
                self.currentButton.setStyleSheet("")
                
                if self.currentButton != self.profile_setting_button:
                    icon_path = self.currentButton.property('icon_path')
                    icon = QIcon(icon_path)
                    self.currentButton.setIcon(icon)

            icon_path = button.property('icon_path')
            clicked_icon = change_svg_color(icon_path, "#FFFFFF")  # 흰색으로 변경
            button.setIcon(clicked_icon)
        
        button.setStyleSheet("background-color: rgb(79, 42, 184);")

        self.currentButton = button

    def enterEvent(self, event):
        self.sidebar.raise_()  # Make sure sidebar is above other widgets
        QWidget.enterEvent(self, event)

    def leaveEvent(self, event):
        self.sidebar.raise_()  # Make sure sidebar is above other widgets
        QWidget.leaveEvent(self, event)

    def resizeEvent(self, event):
        height = event.size().height()

        # 사이드바의 높이를 현재 창의 높이와 일치시킵니다.
        self.sidebar.setFixedHeight(height)

        # Middle Area의 높이를 현재 창의 높이와 일치시킵니다.
        self.middle_area_widget.setFixedHeight(height)

        # Chat Screen의 높이를 현재 창의 높이와 일치시킵니다.
        self.right_area_widget.setFixedHeight(height)

        super().resizeEvent(event)  # 이벤트의 부모 처리를 호출합니다.

    def expandSidebar(self):
        for label in self.sidebar_labels:
            label.show()

    def collapseSidebar(self):
        for label in self.sidebar_labels:
            label.hide()

    def _setStyle(self):
        qss_file = QFile(f'{Path(__file__).parents[1]}/static/chatting_main.qss')
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