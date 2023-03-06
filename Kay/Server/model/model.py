class ChatRoom:
    def __init__(self):
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)

    def remove_client(self, client):
        self.clients.remove(client)

    def broadcast(self, sender, message):
        for client in self.clients:
            if client != sender:
                client.send(message)
