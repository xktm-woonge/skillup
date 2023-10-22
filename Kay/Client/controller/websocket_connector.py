# controller/websocket_connector.py

import json
from PyQt5.QtCore import QObject, pyqtSignal, QThread

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
    new_notification = pyqtSignal(dict)
    
    def __init__(self, url):
        super().__init__()
        self.realtime_communication = RealtimeCommunication(url, self.on_message_received)
        self.realtime_communication.start()

    def on_message_received(self, message):
        data = json.loads(message)
        clmn.HLOG.debug(f"Received data type: {data['type']}, message: {data['data']}")
        if data['type'] == 'FRIEND_REQUEST':
            self.new_notification.emit(data)

    def send_message(self, message):
        self.realtime_communication.send_message(message)