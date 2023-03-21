from PyQt5.QtCore import QThread, pyqtSignal


class ClientThread(QThread):
    message_received = pyqtSignal(str)

    def __init__(self, client, view):
        super().__init__()
        self.client = client
        self.view = view

    def run(self):
        self.client.connect()
        while True:
            message = self.client.receive_message()
            self.message_received.emit(message)

    def send_message(self, message):
        self.client.send_message(message)

    def __del__(self):
        self.client.close()