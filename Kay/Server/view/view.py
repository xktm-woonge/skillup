class ChatRoomView:
    def __init__(self, chat_room):
        self.chat_room = chat_room

    def display_message(self, sender, message):
        print("{}: {}".format(sender, message))
