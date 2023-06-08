import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit

class ChatWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Chat Window')
        self.setGeometry(100, 100, 800, 600)

        self.chat_history = QTextEdit()
        self.chat_history.setReadOnly(True)
        self.message_input = QLineEdit()
        self.send_button = QPushButton('Send')

        vbox = QVBoxLayout()
        vbox.addWidget(self.chat_history)
        hbox = QHBoxLayout()
        hbox.addWidget(self.message_input)
        hbox.addWidget(self.send_button)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

    def append_message(self, message):
        self.chat_history.append(message)

    def clear_message_input(self):
        self.message_input.clear()

if __name__ == '__main__':
    pass