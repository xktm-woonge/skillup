# ./controller/realtime_connector.py

from PyQt5.QtCore import QThread, pyqtSignal

try:
    from model.realtime_communication import RealtimeClient
    from utils import *
except ImportError:
    import sys
    from pathlib import Path
    sys.path.append(str(Path(__file__).parents[1]))
    from model.realtime_communication import RealtimeClient
    from utils import *


class RealtimeThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.realtime_client = RealtimeClient('localhost', 8000, self.handle_message_received)

    def run(self):
        self.realtime_client.connect()

    def send_message(self, message):
        self.realtime_client.send_message(message)

    def handle_message_received(self, received_message):
        # 메시지 처리 로직
        pass

    def close(self):
        self.realtime_client.close()
