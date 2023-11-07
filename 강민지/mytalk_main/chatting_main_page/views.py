import json
import pytz
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model, logout
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from datetime import datetime
from .models import *
from .chatbot import Chatbot


user_model = get_user_model()
chatbot = Chatbot()

def create_notice_box(notice):
    notice_template = get_template('chatting_main_page/notice_box.html')
    
    timestamp_string = notice.created_at.strftime('%Y-%m-%d %H:%M:%S')
    context = {
        'noti_type' : notice.type if notice.type and notice.type == "FRIEND_REQUEST" else f"{notice.type}_notice" ,
        'content' : notice.content,
        'sender_name' : user_model.objects.get(id=notice.sender_id),
        'created_at' : timestamp_string,
    }
    return notice_template.render(context)

def create_friend_list(friend_info):
    friend_template = get_template('chatting_main_page/friend_list.html')
    
    context = {
        "name" : friend_info.name,
        "status_message" : friend_info.status_message if friend_info.status_message and friend_info.status_message != "None" else "",
        "profile_picture" : friend_info.profile_picture,
    }
    return friend_info.status, friend_template.render(context)

def create_message_box(user_id, data, prev_date):
    message_template = get_template('chatting_main_page/message_box.html')
    
    direction = 'send' if data['sender_id'] == user_id else 'given'     
    context = {
                'direction' : direction,
                'message' : data['message_text'],
                'time' : data['timestamp'].strftime("%H:%M"),
            }
    
    if data['timestamp'].date() != prev_date.date():
        context['chat_date'] = f'<div class="chat_date">{data["timestamp"].strftime("%B %d, %Y")}</div>'
        prev_date = data['timestamp']
    else :
        context['chat_date'] = ''
    return prev_date, message_template.render(context)

def create_chatting_room(user_data, room):
    chatting_room_template = get_template('chatting_main_page/chat_list.html')
    final_message = Messages.objects.filter(conversation_id=room['conversation_id']).last()
    
    context = {
        'conv_user_name' : user_data, 
        'conv_final_message' : final_message.message_text,
        'conv_picture' : user_data.profile_picture,
        'user_status' : f"status_{user_data.status}",
        'room_num' : room['conversation_id'],
    }
    return chatting_room_template.render(context)

def get_notice_list(request):
    notice_contents = ""
    notices = Notifications.objects.filter(user_id=request.user.id)
    
    if not notices :
        for notice in notices.values():
            notice_contents += create_notice_box(notice)
    return notice_contents
            

def get_friend_list(request):
    online_contents, offline_contents = "", ""
    friends = Friends.objects.filter(user_id = request.user.id)
    
    if friends :
        for friend in friends.values():
            friend_info = user_model.objects.get(id=friend['friend_id'])
            friend_status, friend_content = create_friend_list(friend_info)
            if friend_status == "offline" :
                offline_contents += friend_content
            else :
                online_contents += friend_content
    return {'online' : online_contents, 'offline': offline_contents}
    
def get_chatting_room_list(request):
    chat_lists_num = []
    chatting_list_contents = ""
    chat_lists = ConversationParticipants.objects.filter(user_id=request.user.id)
    
    if chat_lists:
        for i in chat_lists.values() :
            chat_lists_num.append(i['conversation_id'])
        for chat in chat_lists_num:
            conv_room = ConversationParticipants.objects.filter(conversation_id=chat)
            for room in conv_room.values():
                user_data = user_model.objects.get(id=room['user_id'])
                if user_data.id != request.user.id:
                    chatting_list_contents += create_chatting_room(user_data, room)
    return chatting_list_contents

def get_curr_user_data(request):
    current_user_content = ""
    user_info_template = get_template('chatting_main_page/user_detail.html')
    current_user = user_model.objects.get(id=request.user.id)
    user_data = {
        'id' : current_user.id,
        'email' : current_user.email,
        'name' : current_user.name,
        'profile_picture' : current_user.profile_picture,
        'status_message' : current_user.status_message if current_user.status_message and current_user.status_message != "None" else "",
    }
    current_user_content = user_info_template.render(user_data)
    return current_user_content       


def get_message_data(request):
    chat_content = ""
    message_contents = ""
    conv_user_content = ""
    prev_message_date = datetime(2000, 1, 1) # 시간을 비교하기 위해 임의의 값으로 설정
    conversations_num = json.loads(request.body.decode('utf-8'))['room_num']
    chat_page_template = get_template('chatting_main_page/chatting.html')
    get_messages = Messages.objects.filter(conversation_id=conversations_num)
    
    if get_messages:
        for message in get_messages.values() :
            prev_message_date, get_temp = create_message_box(request.user.id, message, prev_message_date)
            message_contents += get_temp
            
        if Conversations.objects.get(id=conversations_num).type == 'private':
            conv_user = ConversationParticipants.objects.filter(conversation_id=conversations_num).exclude(user_id=request.user.id).first()
            conv_user = user_model.objects.get(id=conv_user.user_id)
            last_message = Messages.objects.filter(conversation_id=conversations_num, sender_id = conv_user.id).last()
            last_reply_time = last_message.timestamp.astimezone(pytz.utc).replace(tzinfo=None)
            delta = (datetime.now() - last_reply_time)
            if delta.total_seconds() < 60 :
                last_reply_time = f'{delta.seconds}초'
            else :
                if delta.total_seconds() < 3600 :
                    last_reply_time = f'{delta.seconds//60}분'
                else :
                    if delta.total_seconds() < 86400 :
                        last_reply_time = f'{delta.seconds//3600}시간'
                    else :
                        last_reply_time = f'{delta.days}일'
                    
            conv_user_content = {
                'conv_user' : conv_user.name,
                'conv_status' : '온라인' if conv_user.status == "online" else '오프라인',
                'conv_pic' : conv_user.profile_picture,
                'last_reply_time' : last_reply_time,
                'csrf_token' : request.META.get('CSRF_COOKIE'),
                'room_number' : conversations_num,
            }
        conv_user_content['message_boxs'] = message_contents
    chat_content = mark_safe(chat_page_template.render(conv_user_content))
    return JsonResponse({'message':'Success', 'data':chat_content})

def push_load_data(request):
    data_dic = {}
    
    data_dic['friend_list'] = get_friend_list(request)
    data_dic['chatting_room_list'] = get_chatting_room_list(request)
    data_dic['curr_user_data'] = get_curr_user_data(request)
    data_dic['notice_data'] = get_notice_list(request)
    return JsonResponse(data_dic)

def load_chattion_main_page(request):
    if request.method =="GET":
        if request.user.is_authenticated:
            context = {'csrf_token':request.META.get('CSRF_COOKIE')}
            return render(request, 'chatting_main_page/chatting_viewer_page.html', context)
        else:
            return redirect('../')


def sended_message_data(request):
    send_user_id = user_model.objects.get(id=request.user.id).id
    send_message = request.POST['send_text']
    room_number = request.POST['room_number']
    is_chatbot_conv = Conversations.objects.get(id=room_number).is_chatbot
    sended_time = datetime.now()
    last_message_time = Messages.objects.filter(conversation_id=room_number).last().timestamp
    
    # Messages.objects.create(message_text=send_message, conversation_id=room_number, sender_id=send_user_id, timestamp=sended_time)
    
    current_data = {
        'sender_id' : send_user_id,
        'message_text' : send_message,
        'timestamp' : sended_time,
    }
    _, message_box_content = create_message_box(send_user_id, current_data, last_message_time)
    return JsonResponse({'message':'Success', 'data': message_box_content, 'last_message':send_message, 'is_chatbot_conv':is_chatbot_conv})

def chatbot_conv(request):
    print(request.POST)
    answer = chatbot.receive_answer(request.POST['send_text'])
    sended_time = datetime.now()
    last_message_time = Messages.objects.filter(conversation_id=request.POST['room_number']).last().timestamp
    data = {
        'sender_id' : 3,
        'message_text' : answer,
        'timestamp' : sended_time,
    }
    _, message_box_content = create_message_box(request.user.id, data, last_message_time, )
    return JsonResponse({'message':'Success', 'data':message_box_content, 'last_message':answer})

def user_logout(request):
    if request.method == 'POST':
        # print(request.POST)
        current_user = user_model.objects.get(email=request.user.email)
        current_user.status = 'offline'
        current_user.save()
        logout(request)
        return JsonResponse({'message':'Success'})