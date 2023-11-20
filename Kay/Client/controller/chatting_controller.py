# ./controller/chatting_controller.py

from PyQt5.QtCore import Qt, QUrl, QSize, QObject, pyqtSlot
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest

try:
    from utils import *
    from view.templates import ChattingWindow
    from view.templates.chatting_notifications import NotificationWidget
    from view.templates.chatting_friends import FriendWidget
    from controller.websocket_connector import WebSocketConnector
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from utils import *
    from view.templates import ChattingWindow
    from view.templates.chatting_notifications import NotificationWidget
    from view.templates.chatting_friends import FriendWidget
    from controller.websocket_connector import WebSocketConnector

class ChattingController(QObject):
    def __init__(self, user_id, data, token, api_thread):
        super().__init__()
        self.user_id = user_id
        self.userInfo = data['userInfo']
        self.friendsInfo = data['friendsInfo']
        self.conversations = data['conversations']
        self.notifications = data['notifications']
        self.token = token
        self.rest_api = api_thread
        self.websocket_api = WebSocketConnector(f"{WEBSOCKET_URL}/?user_id={self.user_id}")  # 메인 쓰레드에서 인스턴스화

        self.chatting_window = ChattingWindow()
        self.set_user_info()
        self.display_notifications()
        self.display_friendList()
        self.chatting_window.show()

        self.connect_slot()

    def connect_slot(self):
        self.websocket_api.add_friend.connect(self.add_friend)
        # self.chatting_window.notification_button.clicked.connect(self.show_notifications)
        # self.chatting_window.friend_list_button.clicked.connect(self.show_friend_list)
        # self.chatting_window.chat_window_button.clicked.connect(self.show_chats)
        # self.chatting_window.profile_setting_button.clicked.connect(self.show_profile_settings)
        # self.websocket_api.new_notification.connect(self.add_notifications)

    # @pyqtSlot()
    # def show_notifications(self):
    #     self._clear_middle_right_areas()
    #     notifications_list_widget = NotificationsListWidget()
    #     self.chatting_window.middle_area.addWidget(notifications_list_widget)
    #     # Similarly, add a widget to the right area if needed

    @pyqtSlot()
    def add_friend(self):
        pass
        # Similarly, add a widget to the right area if needed

    # @pyqtSlot()
    # def show_chats(self):
    #     self._clear_middle_right_areas()
    #     chat_list_widget = ChatListWidget()
    #     self.chatting_window.middle_area.addWidget(chat_list_widget)
    #     # Similarly, add a widget to the right area if needed

    # @pyqtSlot()
    # def show_profile_settings(self):
    #     self._clear_middle_right_areas()
    #     profile_setting_widget = ProfileSettingWidget()
    #     self.chatting_window.middle_area.addWidget(profile_setting_widget)
    #     # Similarly, add a widget to the right area if needed
    
    # @pyqtSlot(dict)
    # def add_notifications(self, data):
    #     # 데이터에서 필요한 정보 추출
    #     image_path = './view/static/img/sidebar_notification_icon'
    #     title = "친구 추가 요청"
    #     content = data['sender_id']
    #     date = data["created_at"]

    #     # NotificationWidget 생성 및 추가
    #     notification = NotificationWidget(image_path, title, content, date)
    #     self.chatting_window.notifications_list_widget.notifications_layout.addWidget(notification)
    
    def _clear_middle_areas(self):
        # Clear widgets in middle_area and right_area
        for i in reversed(range(self.chatting_window.middle_area.count())): 
            self.chatting_window.middle_area.itemAt(i).widget().setParent(None)
        # Do the same for the right area
        
    def set_user_info(self):
        # 프로필 사진 설정
        self.load_profile_picture()

        # 온라인 상태 설정
        if self.userInfo['status'] == 'online':
            self.chatting_window.sidebar.status_label.setStyleSheet("QLabel { background-color: green; border-radius: 5px; }")
        else:
            self.chatting_window.sidebar.status_label.setStyleSheet("QLabel { background-color: gray; border-radius: 5px; }")

    def load_profile_picture(self):
        url = QUrl(self.userInfo['profile_picture'])
        request = QNetworkRequest(url)
        self.manager = QNetworkAccessManager()
        reply = self.manager.get(request)
        reply.finished.connect(self.on_image_load)

    def on_image_load(self):
        reply = self.sender()
        img_data = reply.readAll()
        pixmap = QPixmap()
        if pixmap.loadFromData(img_data):
            profile_pic_resized = pixmap.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            icon_size = QSize(40, 40)
            self.chatting_window.sidebar.profile_setting_button.setIconSize(icon_size)
            self.chatting_window.sidebar.profile_setting_button.setIcon(QIcon(profile_pic_resized))
        else:
            clmn.HLOG.warning("Failed to load image!")
            
    def display_notifications(self):
        self.chatting_window.notifications_list_widget.clear_notifications()
        self.notification_widgets = {}

        for notification in self.notifications:
            image_path = './view/static/img/sidebar_notification_icon'
            # image_path = notification['image_path']
            title = "친구 추가 요청"
            content = notification['sender_email']
            date = notification["created_at"]
            
            notification_widget = NotificationWidget(image_path, title, content, date)
            self.chatting_window.notifications_list_widget.notifications_layout.addWidget(notification_widget)

            self.notification_widgets[content] = notification_widget

            notification_widget.response_signal.connect(
                lambda sender_id, response: self.handle_friend_response(sender_id, response, notification_widget))
            
    def display_friendList(self):
        self.chatting_window.friend_list_widget.clear_friends()
        self.friends_widgets = {}

        for friendInfo in self.friendsInfo:
            name = friendInfo['name']
            email = friendInfo['email']
            image_path = friendInfo['profile_picture']
            status = friendInfo['status']

            self.chatting_window.friend_list_widget.add_friend(name, email, image_path, status)

    def handle_friend_response(self, sender_id, response, widget):
        # 서버에 메시지 전송
        message = {
            "event": "sendFriendResponse",
            "user_id": self.user_id,
            "sender_id": sender_id,
            "response": response
        }
        self.websocket_api.send_message(message)

        # 위젯 삭제
        if response in ["accepted", "rejected", "deleted"]:
            widget.setParent(None)
            widget.deleteLater()
            if sender_id in self.notification_widgets:
                del self.notification_widgets[sender_id]