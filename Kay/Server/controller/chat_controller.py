import socket
import threading

class ChatClient:
    def __init__(self, server_address, view):
        self.view = view
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.connect(server_address)
        self.socket.sendall("New client connected".encode())
        self.running = True
        self.listen_thread = threading.Thread(target=self.listen)
        self.listen_thread.start()

    def send(self, message):
        self.socket.sendall(message.encode())

    def listen(self):
        while self.running:
            message = self.socket.recv(1024).decode()
            sender, message = message.split(":", 1)
            self.view.display_message(sender, message)

    def stop(self):
        self.running = False
        self.socket.close()


class ChatServer:
    def __init__(self, host, port, view):
        self.view = view
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind((host, port))
        self.socket.listen()
        self.chat_room = ChatRoom()
        self.running = True
        self.accept_thread = threading.Thread(target=self.accept_clients)
        self.accept_thread.start()

    def accept_clients(self):
        while self.running:
            client_socket, client_address = self.socket.accept()
            self.view.display_message("ChatServer", "New client connected: {}".format(client_address))
            client = ChatClient(client_address, self.view)
            self.chat_room.add_client(client)

    def stop(self):
        self.running = False
        for client in self.chat_room.clients:
            client.stop()
        self.socket.close()

    def broadcast(self, sender, message):
        self.chat_room.broadcast(sender, message)
