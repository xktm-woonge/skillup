# ./controller/chatting_controller.py

from PyQt5.QtCore import QObject, pyqtSlot
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from view.templates import ChattingWindow
# from view.templates import NotificationsListWidget, FriendListWidget, ChatListWidget, ProfileSettingWidget

class ChattingController(QObject):
    def __init__(self, msg):
        super().__init__()
        self.msg = msg
        self.profile_img_url = msg['user']['profile_img_url']

        self.chatting_window = ChattingWindow()
        self.set_user_info('online')
        self.chatting_window.show()

        # # Connect button click signals to slots
        # self.chatting_window.notification_button.clicked.connect(self.show_notifications)
        # self.chatting_window.friend_list_button.clicked.connect(self.show_friend_list)
        # self.chatting_window.chat_window_button.clicked.connect(self.show_chats)
        # self.chatting_window.profile_setting_button.clicked.connect(self.show_profile_settings)

    # @pyqtSlot()
    # def show_notifications(self):
    #     self._clear_middle_right_areas()
    #     notifications_list_widget = NotificationsListWidget()
    #     self.chatting_window.middle_area.addWidget(notifications_list_widget)
    #     # Similarly, add a widget to the right area if needed

    # @pyqtSlot()
    # def show_friend_list(self):
    #     self._clear_middle_right_areas()
    #     friend_list_widget = FriendListWidget()
    #     self.chatting_window.middle_area.addWidget(friend_list_widget)
    #     # Similarly, add a widget to the right area if needed

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
        
    def set_user_info(self, online):
        # 프로필 사진 설정
        profile_pic = QPixmap(self.profile_img_url)
        profile_pic_resized = profile_pic.scaled(50, 50, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.chatting_window.profile_setting_button.setIcon(QIcon(profile_pic_resized))

        # 온라인 상태 설정
        if online:
            self.chatting_window.status_label.setStyleSheet("QLabel { background-color: green; border-radius: 5px; }")
        else:
            self.chatting_window.status_label.setStyleSheet("QLabel { background-color: gray; border-radius: 5px; }")

    def _clear_middle_right_areas(self):
        # Clear widgets in middle_area and right_area
        for i in reversed(range(self.chatting_window.middle_area.count())): 
            self.chatting_window.middle_area.itemAt(i).widget().setParent(None)
        # Do the same for the right area


# class ChattingController(QObject):
#     pass