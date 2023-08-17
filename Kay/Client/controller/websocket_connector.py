# controller/realtime_connector.py

from model.websocket_communication import RealtimeCommunication

class RealtimeConnector:
    def __init__(self, url):
        self.realtime_communication = RealtimeCommunication(url, self.on_message_received)
        self.realtime_communication.start()

    def on_message_received(self, message):
        print(f"Received message: {message}")

    def send_message(self, message):
        self.realtime_communication.send_message(message)