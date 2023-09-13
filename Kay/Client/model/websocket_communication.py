# ./model/realtime_communication.py
from PyQt5.QtWebSockets import QWebSocket
from PyQt5.QtCore import QUrl, QThread, QTimer, qRegisterMetaType
import threading

try:
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from utils import *
    

class RealtimeCommunication(QThread):
    def __init__(self, url, on_message_received):
        super().__init__()
        qRegisterMetaType("QAbstractSocket::SocketState")
        self.url = url
        self.on_message_received = on_message_received
        self.websocket = None  # 초기화를 나중에 합니다.
        self.lock = threading.Lock()
        self.reconnect_timer = QTimer()
        self.reconnect_timer.timeout.connect(self.attempt_reconnect)
        self.reconnect_timer.setInterval(5000)  # Set reconnect interval to 5 seconds

    def run(self):
        self.websocket = QWebSocket()
        self.websocket.textMessageReceived.connect(self.on_message_received)
        self.websocket.disconnected.connect(self.on_disconnected)
        self.websocket.error.connect(self.on_error)
        
        self.attempt_connect()
        self.exec_()  # 이벤트 루프 시작

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
            with self.lock:
                self.websocket.sendTextMessage(message)
        except Exception as e:
            clmn.HLOG.error(f"Error sending message: {e}")