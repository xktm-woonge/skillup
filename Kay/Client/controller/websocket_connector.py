# controller/realtime_connector.py

import json
from PyQt5.QtCore import pyqtSignal

try:
    from utils import *
    from model.websocket_communication import RealtimeCommunication
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from utils import *
    from model.websocket_communication import RealtimeCommunication

class WebSocketConnector:
    new_notification = pyqtSignal(dict)
    
    def __init__(self, url):
        self.realtime_communication = RealtimeCommunication(url, self.on_message_received)
        self.realtime_communication.start()

    def on_message_received(self, message):
        data = json.loads(message)
        clmn.HLOG.debug(f"Received data type: {data['type']}, message: {data['data']}")
        if data['type'] == 'notification':
            self.new_notification.emit(data)

    def send_message(self, message):
        self.realtime_communication.send_message(message)