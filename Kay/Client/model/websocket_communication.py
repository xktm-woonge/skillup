# ./model/websocket_communication.py

import json
from PyQt5.QtWebSockets import QWebSocket
from PyQt5.QtCore import QUrl, QObject, QTimer

try:
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from utils import *
    

class RealtimeCommunication(QObject):  # QObject 상속
    def __init__(self, url, on_message_received):
        super().__init__()
        self.url = url
        self.on_message_received = on_message_received
        self.websocket = QWebSocket()
        self.reconnect_timer = QTimer()
        self.reconnect_timer.timeout.connect(self.attempt_reconnect)
        self.reconnect_timer.setInterval(5000)  # Set reconnect interval to 5 seconds

    def start(self):
        self.websocket = QWebSocket()
        self.websocket.textMessageReceived.connect(self.on_message_received)
        self.websocket.disconnected.connect(self.on_disconnected)
        self.websocket.error.connect(self.on_error)
        
        self.attempt_connect()

    def attempt_connect(self):
        try:
            self.websocket.open(QUrl(self.url))
            self.websocket.connected.connect(self.on_connected)
        except Exception as e:
            clmn.HLOG.error(f"Error in WebSocket connection: {e}")
            self.reconnect_timer.start()

    def on_connected(self):
        clmn.HLOG.debug("WebSocket connected")
        self.reconnect_timer.stop()  # Stop the reconnect timer when connected

    def on_disconnected(self):
        clmn.HLOG.warning("WebSocket disconnected. Attempting to reconnect...")
        self.reconnect_timer.start()

    def on_error(self, error_code):
        clmn.HLOG.error(f"WebSocket error: {error_code}. Attempting to reconnect...")
        self.reconnect_timer.start()

    def attempt_reconnect(self):
        if not self.websocket.isValid():
            self.attempt_connect()

    def send_message(self, message):
        try:
            # 딕셔너리를 JSON 문자열로 변환
            json_message = json.dumps(message)
            self.websocket.sendTextMessage(json_message)
        except Exception as e:
            clmn.HLOG.error(f"Error sending message: {e}")