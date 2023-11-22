import json
import os
import base64
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from .models import *
from .utils import *
from django.contrib.auth import get_user_model
from .chatbot import Chatbot
from datetime import datetime
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist

class MainPageConsumer(AsyncWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def connect(self):
        await self.accept()
        self.curr_user = dp.get_curr_user_data(self.scope['user'])
        user_id = self.scope['url_route']['kwargs']['user_id']
        connected_users[user_id] = self
        

    async def disconnect(self, close_code):
        user_id = self.scope['url_route']['kwargs']['user_id']
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json["message"]
        
        
        if self.curr_user is None:
            await self.send(json.dumps({'message':'user_auth_error'}))
        else:
            await dp.message_read(message, text_data_json, self.curr_user)
    
    
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

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        # print(text_data_json)
        message = text_data_json["message"]
        
        if self.curr_user is None:
            await self.send(json.dumps({'message':'user_auth_error'}))
        elif message == 'send_message':
            message_box_data, is_chatbot_conv = await dp.create_message_data(text_data_json, self.curr_user)
            message_box_data['direction'] = 'send'
            message_box_data['roomnum'] = text_data_json['room_number']
            await self.send(json.dumps({'message':'send_message', 'data': message_box_data}))
            await self.comform_conv_user(is_chatbot_conv, text_data_json, self.curr_user, message_box_data)
        else:
            await dp.message_read(message, text_data_json, self.curr_user)
        
    async def comform_conv_user(self, ischatbot, data, user, message_box_data):
        if ischatbot:
            chat_data = await dp.chatbot_conv(user, data)
            await self.send(json.dumps({'message':'receive_mesaage','data': chat_data}))
        else :
            message_box_data['direction'] = 'given'
            await self.channel_layer.group_send(
                self.room_group_name,  # 그룹 이름
                {'type': 'receive_mesaage','data': message_box_data, 'sender_channel_name': self.channel_name},
            )
            
                
    async def receive_mesaage(self, event):
        if self.channel_name != event.get('sender_channel_name'):
            await self.send(text_data=json.dumps({'message':'receive_mesaage', 'data':event['data']}))            
                    
class DataProvider():
    def __init__(self):
        self.send_data = {}
    
    async def message_read(self, message, data, user):
        if message == 'add_notice':
            self.add_notice_boxs()
        elif message == 'add_friend':
            self.add_friends_list()
        elif message == 'add_chat_list':
            chat_list_context = await self.add_chat_list(data['room_number'], user)
            self.send_data = {'message':'add_chat_list','data':chat_list_context}
        elif message == 'change_user_status':
            await self.change_user_status(user, data)
        elif message == 'change_user_info':
            await self.change_user_info(data, user)
        elif message == 'change_user_pic':
            await self.change_user_pic(data['data'], user)
        elif message == 'enter_chatting_room':
            await self.enter_chatting_room(data['room_number'], user)
        elif message == 'delete_notice':
            await self.delete_notice(data, user)
            self.send_data = {'message':'delete_notice','noti_num':data['noti_num']}
        elif message in ['accept_friend', 'reject_friend']:
            friends = await self.process_friends_request(data, user)
            self.send_data = {'message':'delete_notice','noti_num':data['noti_num']}
        elif message == 'enter_chat_from_friends':
            room_num, is_new_chat = await self.enter_chat_from_friends(data['friend_name'], user)
            self.send_data = {'message':'enter_chat_room_from_friend', 'room_num':room_num, 'is_new_chat':is_new_chat}
        
        if message in ['change_user_status', 'change_user_info', 'user_logout', 'user_login']:
            friends_id = await self.get_curr_user_friends(user)
            for i in friends_id:
                try:
                    await connected_users[f"{i}"].send(json.dumps({'message':'reload'}))
                except KeyError:
                    continue
        if message in ['add_chat_list', 'delete_notice', 'accept_friend', 'reject_friend', 'enter_chat_from_friends']:
            await self.send_to_client(self.send_data, user)
    
    async def send_to_client(self, send_data, user):
        await connected_users[f'{user}'].send(json.dumps(send_data))
        
  
            
        
    def get_curr_user_data(self, user_scope):
        user = user_scope
        if hasattr(user, 'is_authenticated') and user.is_authenticated:
            return user.id
        return None
    
    def add_notice_boxs(self):
        pass
    
    def add_friends_list(self):
        pass
    
    @database_sync_to_async
    def add_chat_list(self, room_num, user):
        conv_user_id = ConversationParticipants.objects.filter(conversation_id=room_num).exclude(user_id=user).first().user_id
        user_data = user_model.objects.get(id=conv_user_id)
        context = create_chatting_room(user_data, room_num)
        context['get_new'] = check_new_message(user, room_num)
        return context
        
    
    @database_sync_to_async
    def enter_chat_from_friends(self, friend_name, user):
        room_num = ''
        is_chatbot = False
        is_new_chat = False
        friend_id = user_model.objects.get(name=friend_name).id
        part_chat_id = ConversationParticipants.objects.filter(user_id=user).values_list('conversation_id', flat=True)
        
        if friend_id == 3:
            is_chatbot = True
            chatbot_room_list = Conversations.objects.filter(is_chatbot=is_chatbot).values_list('id', flat=True)
            room_num_list = set(part_chat_id) & set(chatbot_room_list)
            
        else:
            private_room_id = Conversations.objects.filter(type='private').exclude(is_chatbot=True).values_list('id', flat=True)
            friend_room_id = ConversationParticipants.objects.filter(user_id=friend_id).values_list('conversation_id', flat=True)
            user_private_room_id = set(part_chat_id) & set(private_room_id)
            room_num_list = user_private_room_id & set(friend_room_id)
                
        if room_num_list:
                room_num = room_num_list.pop()
        else:
            last_conv_num =  Conversations.objects.filter().last().id
            room_num = last_conv_num + 1
            Conversations.objects.create(id=room_num,is_chatbot=is_chatbot)
            ConversationParticipants.objects.create(conversation_id=room_num, user_id=user)
            ConversationParticipants.objects.create(conversation_id=room_num, user_id=friend_id)
            is_new_chat = True
            if is_chatbot:
                text = '당신의 챗팅 친구 TED입니다. 무엇이 궁금하세요?'
                Messages.objects.create(message_text=text, conversation_id=room_num, sender_id=friend_id)
                last_message_id = Messages.objects.filter(sender_id=friend_id).last().id
                MessageReceivers.objects.create(message_id=last_message_id, receiver_id=user)
        return room_num, is_new_chat
            
    
    @database_sync_to_async
    def process_friends_request(self, data, user):
        notice_number = data['noti_num']
        friend_requester = Notifications.objects.get(id=notice_number).sender_id
        if data['message'] == 'accept_friend':
            print(f"frinends_requester={friend_requester}, user={user}")
            # Friends.objects.create(friend_id=friend_requester, user_id=user)
            # Friends.objects.create(friend_id=user, user_id=friend_requester)
        else:
            print('거절이야')
        # NotificationReceivers.objects.filter(notification_id=notice_number, receiver_id=user).update(is_conform=True)
            
        
    @database_sync_to_async
    def delete_notice(self, data, user):
        notice_number = data['noti_num']
        NotificationReceivers.objects.filter(notification_id=notice_number, receiver_id=user).update(is_conform=True)
        
    @database_sync_to_async
    def enter_chatting_room(self, room_num, user):
        messages = Messages.objects.filter(conversation_id=room_num).values_list('id', flat=True)
        for message_id in messages:
            try:
                MessageReceivers.objects.filter(message_id=message_id, receiver_id=user).update(is_read=True)
            except ObjectDoesNotExist:
                continue
    
    @database_sync_to_async
    def change_user_pic(self, data, user):
        file_info, encoded_data = data.split(';base64,')
        decoded_data = base64.b64decode(encoded_data)
        
        _, file_format = file_info.split('/')
        file_name = f'user_{user}.{file_format}'
        file_path =  f'{settings.STATICFILES_DIRS[0]}/img/user/'

        for before_file in os.listdir(file_path):
            if before_file.startswith(f'user_{user}.'):
                os.remove(f'{file_path}{before_file}')
        
        with open(f'{file_path}{file_name}', 'wb') as file:
            file.write(decoded_data)
        user_model.objects.filter(id=user).update(profile_picture=f'user/{file_name}')
    
    @database_sync_to_async
    def change_user_info(self, data, user):
        name = data['text']
        status_message = data['textarea']
        
        user_model.objects.filter(id=user).update(name=name, status_message=status_message)
    
    @database_sync_to_async
    def create_message_data(self, data, sender=None):
        send_message = data['send_text']
        room_number = data['room_number']
        is_chatbot_conv = Conversations.objects.get(id=room_number).is_chatbot
        last_message_time = Messages.objects.filter(conversation_id=room_number).last().timestamp
        
        if sender is not None:
            # Messages.objects.create(message_text=send_message, conversation_id=room_number, sender_id=sender)
            # message_id = Messages.objects.filter(conversation_id=room_number).last().id
            receviers = ConversationParticipants.objects.filter(conversation_id=room_number).exclude(user_id=sender)
            for receiver in receviers.values():
                # MessageReceivers.objects.create(message_id=message_id, receiver_id=receiver['user_id'])
                pass
        current_message_time = Messages.objects.filter(conversation_id=room_number).last().timestamp
        
        current_data = {
            'message': send_message,
            'time': current_message_time.strftime("%H:%M"),
            'roomnum' :room_number,
        }
        if current_message_time.date() != last_message_time.date():
            current_data['message_box__date'] = f'<time class="message_box__date" datetime="{current_data["time"]}">{current_data["time"].strftime("%Y-%m-%d")}</time>'
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
    
    @database_sync_to_async
    def get_curr_user_friends(self, curr_user):
        friends_id = []
        get_user_id = user_model.objects.get(id=curr_user).id
        for i in Friends.objects.filter(user_id=get_user_id).values():
            friends_id.append(i['friend_id'])
        return friends_id
        
    
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