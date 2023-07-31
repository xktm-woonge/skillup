# ./controller/chatting_controller.py

from PyQt5.QtCore import QObject, pyqtSlot
from view.templates import ChattingWindow
from view.templates import NotificationsListWidget, FriendListWidget, ChatListWidget, ProfileSettingWidget

class ChattingController(QObject):
    def __init__(self):
        super().__init__()

        self.chatting_window = ChattingWindow()
        self.chatting_window.show()

        # Connect button click signals to slots
        self.chatting_window.notification_button.clicked.connect(self.show_notifications)
        self.chatting_window.friend_list_button.clicked.connect(self.show_friend_list)
        self.chatting_window.chat_window_button.clicked.connect(self.show_chats)
        self.chatting_window.profile_setting_button.clicked.connect(self.show_profile_settings)

    @pyqtSlot()
    def show_notifications(self):
        self._clear_middle_right_areas()
        notifications_list_widget = NotificationsListWidget()
        self.chatting_window.middle_area.addWidget(notifications_list_widget)
        # Similarly, add a widget to the right area if needed

    @pyqtSlot()
    def show_friend_list(self):
        self._clear_middle_right_areas()
        friend_list_widget = FriendListWidget()
        self.chatting_window.middle_area.addWidget(friend_list_widget)
        # Similarly, add a widget to the right area if needed

    @pyqtSlot()
    def show_chats(self):
        self._clear_middle_right_areas()
        chat_list_widget = ChatListWidget()
        self.chatting_window.middle_area.addWidget(chat_list_widget)
        # Similarly, add a widget to the right area if needed

    @pyqtSlot()
    def show_profile_settings(self):
        self._clear_middle_right_areas()
        profile_setting_widget = ProfileSettingWidget()
        self.chatting_window.middle_area.addWidget(profile_setting_widget)
        # Similarly, add a widget to the right area if needed

    def _clear_middle_right_areas(self):
        # Clear widgets in middle_area and right_area
        for i in reversed(range(self.chatting_window.middle_area.count())): 
            self.chatting_window.middle_area.itemAt(i).widget().setParent(None)
        # Do the same for the right area
