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
    from view.templates.chatting_sidebar import Sidebar
    from view.templates.chatting_notifications import NotificationsListWidget, NotificationWidget
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[2]))
    from utils import *
    from view.templates.chatting_sidebar import Sidebar
    from view.templates.chatting_notifications import NotificationsListWidget, NotificationWidget


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
        for i in range(10):
            notification = NotificationWidget(r'D:\g_Project\2023_skillup_chatting\Kay\Client\view\static\img\sidebar_friends_icon.png', '시스템 알림', 
                                          '테스트테스트테스트테스트asdgsd', '2023-08-13 20:00:00')
            self.notifications_list_widget.notifications_layout.addWidget(notification)
        self.middle_area_widget.addWidget(self.notifications_list_widget)
        
        # Right Area
        self.right_area_widget = QStackedWidget(self)
        self.right_area_widget.setGeometry(
            self.sidebar_width + self.middle_width, 0, self.right_width, self.height)
        
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