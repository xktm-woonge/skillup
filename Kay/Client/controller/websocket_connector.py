# controller/websocket_connector.py

import json
from PyQt5.QtCore import QObject, pyqtSignal

try:
    from utils import *
    from model.websocket_communication import RealtimeCommunication
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from utils import *
    from model.websocket_communication import RealtimeCommunication


class WebSocketConnector(QObject):
    add_friend = pyqtSignal(dict)
    call_conversation = pyqtSignal(dict)
    friend_request = pyqtSignal(dict)
    new_message = pyqtSignal(dict)
    
    def __init__(self, url):
        super().__init__()
        self.realtime_communication = RealtimeCommunication(url, self.on_message_received)
        self.realtime_communication.start()

    def on_message_received(self, message):
        data = json.loads(message)
        clmn.HLOG.debug(f"Received data type: {data['category']}, message: {data['message']}, data: {data['data']}")
        if data['category'] == 'notifications' and data['message'] == 'friendResponseSuccess':
            self.add_friend.emit(data['data'])
        elif data['category'] == 'conversations' and data['status'] == 'SUCCESS':
            self.call_conversation.emit(data['data'])
        elif data['category'] == 'notifications' and data['message'] == 'friendRequest':
            self.friend_request.emit(data['data'])
        elif data['category'] == 'messages':
            self.new_message.emit(data['data'])

    def send_message(self, message):
        self.realtime_communication.send_message(message)