import sys

from pathlib import Path
sys.path.append(str(Path(__file__).parents[1]))
from Client.Model.client_model import Client
from Client.View.Templates.chatting import ChatWindow

class ChatController:
    def __init__(self, host, port):
        self.client = Client(host, port)
        self.view = ChatWindow()
        self.view.send_button.clicked.connect(self.handle_send_button)
        self.client_thread = ClientThread(self.client, self.view)
        self.client_thread.start()

    def handle_send_button(self):
        message = self.view.message_input.text()
        self.client_thread.send_message(message)
        self.view.clear_message_input()