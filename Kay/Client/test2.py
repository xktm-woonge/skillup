import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebSockets import QWebSocket, QWebSocketProtocol

class WebSocketClient:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.websocket = QWebSocket("", QWebSocketProtocol.Version13, None)

        # Signals
        self.websocket.connected.connect(self.on_connected)
        self.websocket.disconnected.connect(self.on_disconnected)
        self.websocket.textMessageReceived.connect(self.on_message_received)

        # Connect to the WebSocket server
        self.websocket.open(QUrl("ws://localhost:3000/"))

        sys.exit(self.app.exec_())

    def on_connected(self):
        print("Connected to server")
        self.websocket.sendTextMessage("Hello from QWebSocket client!")

    def on_disconnected(self):
        print("Disconnected from server")

    def on_message_received(self, message):
        print("Message from server:", message)

if __name__ == '__main__':
    client = WebSocketClient()
