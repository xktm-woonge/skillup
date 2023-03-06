import socket

class Client:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self.host, self.port))

    def send_message(self, message):
        self.socket.sendall(message.encode())

    def receive_message(self):
        data = self.socket.recv(1024)
        return data.decode()

    def close(self):
        self.socket.close()
