import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import *
from .utils import *
from django.contrib.auth import get_user_model
from .chatbot import Chatbot
from datetime import datetime



class MainPageConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def connect(self):
        await self.accept()
        self.curr_user = dp.get_curr_user_data(self.scope['user'])
        user_id = self.scope['url_route']['kwargs']['user_id']
        connected_users[user_id] = self
        # main_page_consumers = {k: v for k, v in connected_users.items() if isinstance(v, MainPageConsumer)}
        # print(main_page_consumers, 'main', sep='/')
        

    async def disconnect(self, close_code):
        user_id = self.scope['url_route']['kwargs']['user_id']
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # print(text_data_json)
        message = text_data_json["message"]
        
        
        if self.curr_user is None:
            await self.send(json.dumps({'message':'user_auth_error'}))
        else:
            if message == 'add_notice':
                dp.add_notice_boxs()
            elif message == 'add_friend':
                dp.add_friends_list()
            elif message == 'add_chat':
                dp.add_chat_list()
            elif message == 'change_user_status':
                dp.change_user_status(self.curr_user, text_data_json)
    
        
    
    
class ChatRoomConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        self.curr_user = dp.get_curr_user_data(self.scope['user'])
        user_id = self.scope['url_route']['kwargs']['user_id']
        connected_users[user_id] = self
        self.room_number = self.scope['url_route']['kwargs']['room_num']
        self.room_group_name = f"chat_{self.room_number}"

        # 채널 그룹에 입장할 때
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        # print(self.scope['url_route']['kwargs']['room_num'])
        # chat_room_consumers = {k: v for k, v in connected_users.items() if isinstance(v, ChatRoomConsumer)}
        # print(chat_room_consumers, 'room', sep='/')

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # print(text_data_json)
        message = text_data_json["message"]
        
        if message == 'enter_chatting_room':
                dp.enter_chatting_room()
        elif message == 'send_message':
            message_box_data, is_chatbot_conv = await dp.create_message_data(text_data_json, self.curr_user)
            message_box_data['direction'] = 'send'
            message_box_data['roomnum'] = text_data_json['room_number']
            await self.send(json.dumps({'message':'send_message', 'data': message_box_data}))
            if is_chatbot_conv:
                chat_data = await dp.chatbot_conv(self.curr_user, text_data_json)
                await self.send(json.dumps({'message':'recive_mesaage','data': chat_data}))
            else :
                message_box_data['direction'] = 'given'
                await self.channel_layer.group_send(
                    self.room_group_name,  # 그룹 이름
                    {'type': 'recive_mesaage','data': message_box_data, 'sender_channel_name': self.channel_name},
                )

    async def recive_mesaage(self, event):
        if self.channel_name != event.get('sender_channel_name'):
            await self.send(text_data=json.dumps({'message':'recive_mesaage', 'data':event['data']}))
                    
                    
class DataProvider():
    def __init__(self):
        pass
        
    def get_curr_user_data(self, user_scope):
        user = user_scope
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
    def create_message_data(self, data, sender=None):
        send_message = data['send_text']
        room_number = data['room_number']
        is_chatbot_conv = Conversations.objects.get(id=room_number).is_chatbot
        last_message_time = Messages.objects.filter(conversation_id=room_number).last().timestamp
        
        # if sender is not None:
        #     Messages.objects.create(message_text=send_message, conversation_id=room_number, sender_id=sender)
        current_message_time = Messages.objects.filter(conversation_id=room_number).last().timestamp
        
        current_data = {
            'message': send_message,
            'time': current_message_time.strftime("%H:%M"),
            'roomnum' :room_number,
        }
        if current_message_time.date() != last_message_time.date():
            current_data['message_box__date'] = f'<time class="message_box--date">{current_data["timestamp"].strftime("%B %d, %Y")}</time>'
        else :
            current_data['message_box__date'] = ''
        
        return current_data, is_chatbot_conv
    
    
    
    @database_sync_to_async
    def chatbot_conv(self, curr_user,data):
        answer = chatbot.receive_answer(data['send_text'])
        room_number = data['room_number']
        sended_time = datetime.now()
        last_message_time = Messages.objects.filter(conversation_id=data['room_number']).last().timestamp
        # Messages.objects.create(message_text=answer, conversation_id=room_number, sender_id=3, timestamp=sended_time)
        data = {
            'sender_id' : 3,
            'message_text' : answer,
            'timestamp' : sended_time,
        }
        _, message_box_content = create_message_box(curr_user, data, last_message_time)
        message_box_content['add_data'] = {'last_message':answer, 'roomnum' :room_number}
        return message_box_content

    @database_sync_to_async
    def change_user_status(self, curr_user, data):
        user_model.objects.filter(id=curr_user).update(status=data['changed_status'])
        friends = self.get_curr_user_friends(curr_user)
    
    @database_sync_to_async
    def get_curr_user_friends(self, curr_user):
        get_user_id = user_model.objects.get(id=curr_user).id
        return Friends.objects.filter(user_id=get_user_id)
    
    @database_sync_to_async
    def send_conneted_user(self, curr_user,room_num):
        given_message = Messages.objects.filter(conversation_id=room_num).last()
        send_user_id = given_message.sender_id
        last_message_time = given_message.timestamp
        given_message = given_message.message_text
        get_room_members = ConversationParticipants.objects.filter(conversation_id=room_num).exclude(user_id=curr_user)
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
    
connected_users = {}
dp = DataProvider()
chatbot = Chatbot()
user_model = get_user_model()