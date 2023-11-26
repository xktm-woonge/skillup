# ./controller/chatting_controller.py

from PyQt5.QtCore import Qt, QUrl, QSize, QObject, pyqtSlot, QDateTime
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtNetwork import QNetworkAccessManager, QNetworkRequest
import sys
from pathlib import Path

try:
    from utils import *
    from view.templates import ChattingWindow
    from view.templates.chatting_notifications import NotificationWidget
    from view.templates.chatting_friends import FriendWidget
    from view.templates.chatting_list import ChatWidget
    from view.templates.chatting_messages import ChattingInterface
    from controller.websocket_connector import WebSocketConnector
except ImportError:
    sys.path.append(str(Path(__file__).parents[1]))
    from utils import *
    from view.templates import ChattingWindow
    from view.templates.chatting_notifications import NotificationWidget
    from view.templates.chatting_friends import FriendWidget
    from view.templates.chatting_list import ChatWidget
    from view.templates.chatting_messages import ChattingInterface
    from controller.websocket_connector import WebSocketConnector

class ChattingController(QObject):
    def __init__(self, user_id, data, token, api_thread):
        super().__init__()
        self.user_id = user_id
        self.userInfo = data['userInfo']
        self.friendsInfo = data['friendsInfo']
        self.conversations = data['conversations']
        self.notifications = data['notifications']
        self.messages = data['messages']
        self.token = token
        self.rest_api = api_thread
        self.websocket_api = WebSocketConnector(f"{WEBSOCKET_URL}/?user_id={self.user_id}")  # 메인 쓰레드에서 인스턴스화

        self.chatting_window = ChattingWindow()
        self.set_user_info()
        self.display_notifications()
        self.display_friendList()
        self.add_conversations()
        self.chatting_window.show()

        self.connect_slot()

    def connect_slot(self):
        self.websocket_api.add_friend.connect(self.add_friend)
        self.websocket_api.call_conversation.connect(self.call_conversation)

    @pyqtSlot(dict)
    def add_friend(self, data):
        pass
        # Similarly, add a widget to the right area if needed

    @pyqtSlot(dict)
    def call_conversation(self, data):
        conversation_id = data['conversationId']
        name = data['name']
        email = data['email']
        image_path = data['imagePath']
        isNewConversation = data['isNewConversation']

        if isNewConversation:
            widget = ChatWidget(name, email, image_path, conversation_id)
            self.chatting_window.chatting_list_widget.add_friend(widget)

            conversation_widget = ChattingInterface(image_path, name, email, conversation_id)
            self.chatting_window.right_area_widget.addWidget(conversation_widget)
            self.conversation_index[conversation_id] = len(self.conversation_index) + 1

            widget.doubleClicked.connect(self.on_chat_widget_clicked)

        # 더블클릭한 창 표시
        self.chatting_window.right_area_widget.setCurrentIndex(self.conversation_index[conversation_id])

    @pyqtSlot(str, str, int)
    def send_message_to_server(self, email, message_text, conversation_id):
        info = {
            "sender_email": self.user_id,
            "conversation_id": conversation_id,
            "email": email,
            "message_text": message_text
        }
        message = make_websocket_message("sendMessage", info)
        self.websocket_api.send_message(message)
    
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
            # image_path = friendInfo['profile_picture']
            image_path = f'{Path(__file__).parents[1]}/view/static/img/base_profile-removebg-preview.png'
            status = friendInfo['status']

            friend_widget = FriendWidget(name, email, image_path, status)
            self.chatting_window.friend_list_widget.friends_layout.addWidget(friend_widget)

            # 더블 클릭 시그널에 슬롯 연결
            friend_widget.doubleClicked.connect(self.make_conversation)

    def add_conversations(self):
        self.conversation_index = {}

        for i, conversation in enumerate(self.conversations, start=1):
            conversation_id = conversation['conversation_id']
            email = conversation['sub_email']
            conversation_name = conversation['conversation_name']
            name = conversation['conversation_name']
            image_path = f'{Path(__file__).parents[1]}/view/static/img/base_profile-removebg-preview.png'

            widget = ChatWidget(conversation_name, email, image_path, conversation_id)
            self.chatting_window.chatting_list_widget.add_friend(widget)

            conversation_widget = ChattingInterface(image_path, name, email, conversation_id)
            self.chatting_window.right_area_widget.addWidget(conversation_widget)

            # 메시지를 표시합니다.
            self.display_messages(conversation_id, conversation_widget)

            self.conversation_index[conversation_id] = i
            conversation_widget.sending_message.connect(self.send_message_to_server)

            widget.doubleClicked.connect(self.on_chat_widget_clicked)

    def display_messages(self, conversation_id, conversation_widget):
        # 해당 대화방의 메시지를 필터링하고 표시합니다.
        for message in self.messages:
            if message['conversation_id'] == conversation_id:
                # 메시지 텍스트와 시간을 추출합니다.
                message_text = message['message_text']
                timestamp = message['timestamp']
                # 시간 형식을 'HH:mm AM/PM' 형태로 변환합니다.
                formatted_time = QDateTime.fromString(timestamp, Qt.ISODate).toString("hh:mm AP")
                # 메시지를 대화 인터페이스에 추가합니다.
                conversation_widget.add_message(message_text, formatted_time, message['sender_id'] == self.userInfo['id'])

    @pyqtSlot(int)
    def on_chat_widget_clicked(self, conversation_id):
        # conversation_id를 사용하여 right_area_widget에서 해당 대화 위젯을 찾아서 활성화
        if conversation_id in self.conversation_index:
            index = self.conversation_index[conversation_id]
            self.chatting_window.right_area_widget.setCurrentIndex(index)  

    # 더블 클릭 정보를 처리하는 슬롯
    def make_conversation(self, name, email, image_path):
        info = {
            "user_email": self.userInfo['email'],
            "name": name,
            "email": email,
            "image_path": image_path
        }
        message = make_websocket_message("makeConversation", info)
        self.websocket_api.send_message(message)

    def handle_friend_response(self, sender_id, response, widget):
        # 서버에 메시지 전송
        info = {
            "user_id": self.user_id,
            "sender_id": sender_id,
            "response": response
        }
        message = make_websocket_message('sendFriendResponse', info)
        self.websocket_api.send_message(message)

        # 위젯 삭제
        if response in ["accepted", "rejected", "deleted"]:
            widget.setParent(None)
            widget.deleteLater()
            if sender_id in self.notification_widgets:
                del self.notification_widgets[sender_id]