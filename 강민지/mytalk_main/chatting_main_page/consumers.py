import json
from channels.generic.websocket import WebsocketConsumer


class ChatConsumer(WebsocketConsumer):
    def connect(self):
        self.accept()

    def disconnect(self, close_code):
        pass

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]

        self.send(text_data=json.dumps({"message": message}))
        
        
    def add_notice_boxs(self):
        pass
    
    def add_friends_list(self):
        pass
    
    def add_chat_list(self):
        pass
    
    def view_chatting_room(self):
        pass
    
    def add_message_box(self):
        pass