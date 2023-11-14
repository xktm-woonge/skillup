import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import *
from .utils import *
from django.contrib.auth import get_user_model
from .chatbot import Chatbot

connected_users = {}

class ChatConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        self.chatbot = Chatbot()
        super().__init__(*args, **kwargs)

    async def connect(self):
        await self.accept()
        self.user_model = get_user_model()
        self.curr_user = await self.get_curr_user_data()
        user_id = self.scope['url_route']['kwargs']['user_id']
        self.channels_layer = f"user_{user_id}"
        connected_users[user_id] = self

    async def disconnect(self, close_code):
        user_id = self.scope['url_route']['kwargs']['user_id']
        self.channels_layer = f"user_{user_id}"
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # print(text_data_json)
        message = text_data_json["message"]
        
        
        if self.curr_user is None:
            await self.send(json.dumps({'message':'user_auth_error'}))
        else:
            if message == 'add_notice':
                self.add_notice_boxs()
            elif message == 'add_friend':
                self.add_friends_list()
            elif message == 'add_chat':
                self.add_chat_list()
            elif message == 'enter_chatting_room':
                self.enter_chatting_room()
            elif message == 'send_message':
                get_data, is_chatbot_conv = await self.add_message_box(self.curr_user, text_data_json)
                await self.send(json.dumps({'message':'send_message', 'data': get_data}))
                if is_chatbot_conv:
                    chat_data = await self.chatbot_conv(text_data_json)
                    await self.send(json.dumps({'message':'recive_mesaage','data': chat_data}))
                else :
                    chat_data = await self.send_conneted_user(text_data_json['room_number'])
                    for user in chat_data.keys():
                        try:
                            await connected_users[f"{user}"].send(json.dumps({'message':'recive_mesaage','data': chat_data[f'{user}']}))
                        except KeyError:
                            continue
            elif message == 'change_user_status':
                await self.change_user_status(text_data_json)
                    
    @database_sync_to_async
    def get_curr_user_data(self):
        user = self.scope['user']
        if hasattr(user, 'is_authenticated') and user.is_authenticated:
            return user.id
        return None

        
    def add_notice_boxs(self):
        pass
    
    def add_friends_list(self):
        pass
    
    def add_chat_list(self):
        pass
    
    def enter_chatting_room(self):
        pass
        
    @database_sync_to_async
    def add_message_box(self, sender, data):
        send_user_id = sender
        send_message = data['send_text']
        room_number = data['room_number']
        is_chatbot_conv = Conversations.objects.get(id=room_number).is_chatbot
        sended_time = datetime.now()
        last_message_time = Messages.objects.filter(conversation_id=room_number).last().timestamp
        
        Messages.objects.create(message_text=send_message, conversation_id=room_number, sender_id=send_user_id, timestamp=sended_time)
        
        current_data = {
            'sender_id': send_user_id,
            'message_text': send_message,
            'timestamp': sended_time,
        }
        _, message_box_content = create_message_box(self.curr_user, current_data, last_message_time)
        message_box_content['add_data'] = {'last_message':send_message, 'roomnum' :room_number}
        return message_box_content, is_chatbot_conv
    
    @database_sync_to_async
    def chatbot_conv(self, data):
        answer = self.chatbot.receive_answer(data['send_text'])
        room_number = data['room_number']
        sended_time = datetime.now()
        last_message_time = Messages.objects.filter(conversation_id=data['room_number']).last().timestamp
        Messages.objects.create(message_text=answer, conversation_id=room_number, sender_id=3, timestamp=sended_time)
        data = {
            'sender_id' : 3,
            'message_text' : answer,
            'timestamp' : sended_time,
        }
        _, message_box_content = create_message_box(self.curr_user, data, last_message_time)
        message_box_content['add_data'] = {'last_message':answer, 'roomnum' :room_number}
        return message_box_content

    @database_sync_to_async
    def change_user_status(self, data):
        self.user_model.objects.filter(id=self.curr_user).update(status=data['changed_status'])
        friends = self.get_curr_user_friends()
        
    def get_curr_user_friends(self):
        get_user_id = self.user_model.objects.get(id=self.curr_user).id
        return Friends.objects.filter(user_id=get_user_id)
    
    @database_sync_to_async
    def send_conneted_user(self, room_num):
        given_message = Messages.objects.filter(conversation_id=room_num).last()
        send_user_id = given_message.sender_id
        last_message_time = given_message.timestamp
        given_message = given_message.message_text
        get_room_members = ConversationParticipants.objects.filter(conversation_id=room_num).exclude(user_id=self.curr_user)
        member_data = {}
        
        current_data = {
            'sender_id': send_user_id,
            'message_text': given_message,
            'timestamp': last_message_time,
        }
        for member in get_room_members.values():
            _, message_box_content = create_message_box(member['user_id'], current_data, last_message_time)
            message_box_content['add_data'] = {'last_message':given_message, 'roomnum' :room_num}
            
            member_data[f"{member['user_id']}"] = message_box_content
        return member_data