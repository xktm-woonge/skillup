# ./model/realtime_communication.py
from PyQt5.QtWebSockets import QWebSocket
from PyQt5.QtCore import QUrl, QThread
import threading

class RealtimeCommunication(QThread):
    def __init__(self, url, on_message_received):
        super().__init__()
        self.url = url
        self.on_message_received = on_message_received
        self.websocket = QWebSocket()
        self.websocket.textMessageReceived.connect(self.on_message_received)
        self.lock = threading.Lock()

    def run(self):
        try:
            self.websocket.open(QUrl(self.url))
            self.websocket.connected.connect(self.on_connected)
            self.exec_()
        except Exception as e:
            print(f"Error in WebSocket connection: {e}")

    def on_connected(self):
        print("WebSocket connected")

    def send_message(self, message):
        try:
            with self.lock:
                self.websocket.sendTextMessage(message)
        except Exception as e:
            print(f"Error sending message: {e}")