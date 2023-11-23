# ./view/templates/chatting_main.py

from PyQt5.QtWidgets import QWidget, QLabel, QApplication, QDesktopWidget, QStackedWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import QFile, pyqtSlot, Qt, QSize
from PyQt5.QtSvg import QSvgWidget
from pathlib import Path
import sys

try:
    from utils import *
    from view.templates.chatting_sidebar import Sidebar
    from view.templates.chatting_notifications import NotificationsListWidget
    from view.templates.chatting_friends import FriendListWidget
    from view.templates.chatting_list import ChatListWidget
    from view.templates.chatting_messages import ChattingInterface
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))
    from utils import *
    from view.templates.chatting_sidebar import Sidebar
    from view.templates.chatting_notifications import NotificationsListWidget
    from view.templates.chatting_friends import FriendListWidget
    from view.templates.chatting_messages import ChattingInterface


class ChattingWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.sidebar_width = 50
        self.middle_width = 300
        self.right_width = 900
        self.height = 600

        self.sidebar_expanded = False
        self.sidebar_labels = []

        self.initUI()

    def initUI(self):

        self.sidebar = Sidebar(self)
        self.sidebar.setGeometry(0, 0, self.sidebar_width, self.height)

        # Middle Area
        self.middle_area_widget = QStackedWidget(self)
        self.middle_area_widget.setGeometry(self.sidebar_width, 0, self.middle_width, self.height)
        
        # 예시로 NotificationsListWidget을 추가합니다.
        # 다른 위젯도 여기에 추가하면 됩니다.
        self.notifications_list_widget = NotificationsListWidget()
        self.middle_area_widget.addWidget(self.notifications_list_widget)

        self.friend_list_widget = FriendListWidget()
        self.middle_area_widget.addWidget(self.friend_list_widget)

        self.chatting_list_widget = ChatListWidget()
        self.middle_area_widget.addWidget(self.chatting_list_widget)
        
        # Right Area
        self.right_area_widget = QStackedWidget(self)
        self.right_area_widget.setGeometry(
            self.sidebar_width + self.middle_width, 0, self.right_width, self.height)
        
        self.chatting_messages = ChattingInterface()
        self.right_area_widget.addWidget(self.chatting_messages)
        
        # 중앙에 표시될 위젯을 위한 레이아웃
        central_layout = QVBoxLayout()
        central_layout.setAlignment(Qt.AlignCenter)  # 레이아웃의 내용을 가운데 정렬

        # SVG 이미지 추가
        svg_widget = QSvgWidget(f'{Path(__file__).parents[1]}/static/icon/Pets.svg')  # 실제 경로로 변경
        svg_widget.setFixedSize(30, 30)  # SVG 이미지 크기 조정
        central_layout.addWidget(svg_widget, alignment=Qt.AlignCenter)  # 중앙 레이아웃에 위젯 추가

        # QLabel에 "No more message" 텍스트 추가
        no_message_label = QLabel('No more message', self)
        no_message_label.setAlignment(Qt.AlignCenter)  # 가운데 정렬
        central_layout.addWidget(no_message_label)  # 중앙 레이아웃에 위젯 추가

        # Right Area에 레이아웃 설정
        central_widget = QWidget()
        central_widget.setLayout(central_layout)
        self.right_area_widget.addWidget(central_widget)
        
        self.connect_slot()
        self.sidebar.notification_button.click()

        self._setStyle()

        self.setWindowTitle('Chatting')
        self.setGeometry(300, 300, 1250, 600)  # Adjusted as per your requirement
        self.setMinimumSize(QSize(1250, 600))
        self.show()
        
    def connect_slot(self):
        self.sidebar.notification_button.clicked.connect(self.show_notifications)
        self.sidebar.friend_list_button.clicked.connect(self.show_friends)
        self.sidebar.chat_window_button.clicked.connect(self.show_chattings)

    @pyqtSlot()
    def show_notifications(self):
        # self.clear_middle_areas()
        self.middle_area_widget.setCurrentWidget(self.notifications_list_widget)
        # Similarly, add a widget to the right area if needed

    @pyqtSlot()
    def show_friends(self):
        # self.clear_middle_areas()
        self.middle_area_widget.setCurrentWidget(self.friend_list_widget)

    @pyqtSlot()
    def show_chattings(self):
        # self.clear_middle_areas()
        self.middle_area_widget.setCurrentWidget(self.chatting_list_widget)

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

    def _setStyle(self):
        # Main QSS (if you have separate styles for main)
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
    font.Init()
    ex = ChattingWindow()
    sys.exit(app.exec_())