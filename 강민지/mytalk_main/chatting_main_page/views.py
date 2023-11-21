import json
import pytz
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone
from django.contrib.auth import authenticate, get_user_model, logout
from django.template.loader import get_template
from django.templatetags.static import static
from django.utils.safestring import mark_safe
from datetime import datetime
from .models import *
from .utils import *
from django.core.exceptions import ObjectDoesNotExist

user_model = get_user_model()

def notice_pretreatment(data):
    timestamp = data.created_at.strftime('%Y-%m-%d %H:%M:%S')
    
    try:
        sender_name = user_model.objects.get(id=data.sender_id).name
    except user_model.DoesNotExist:
        sender_name = 'system'
    if data.type in ['system', 'danger']:
        img_src = static('icon/Notification.svg')
    else:
        get_sender_profile_pic = user_model.objects.get(id=data.sender_id).profile_picture
        img_src = static(f'img/{get_sender_profile_pic}')
    return timestamp, sender_name, img_src
        
def set_notice_box_data(notice):
    timestamp_string, sender_name, img_src = notice_pretreatment(notice)
    
    context = {
        'noti_type' : notice.type,
        'noti_num' : f'num_{notice.id}',
        'img_src' : img_src,
        'content' : notice.content,
        'title' : sender_name,
        'created_at' : timestamp_string,
        'button_type': notice.type,
    }
    return context

def set_friend_list_data(friend_info):
    if friend_info.status == 'offline':
        show_user_status = False
    else:
        show_user_status = friend_info.is_online
    
    context = {
        "name" : friend_info.name,
        "team" : '',
        "status" : friend_info.status,
        "status_message" : friend_info.status_message if friend_info.status_message and friend_info.status_message != "None" else "",
        "profile_picture" : friend_info.profile_picture,
    }
    return show_user_status, context


def create_chatting_room(user_data, room): 
    final_message = Messages.objects.filter(conversation_id=room['conversation_id']).last()
    
    context = {
        'conv_user_name' : user_data.name, 
        'conv_final_message' : final_message.message_text,
        'conv_picture' : user_data.profile_picture,
        'user_status' : f"{user_data.status}",
        'room_num' : room['conversation_id'],
        'team' : '',
    }
        
    return context

def get_notice_list(request):
    notice_contents = {}
    received_notices = NotificationReceivers.objects.filter(receiver=request.user.id, is_conform=False)
    if received_notices :
        for receicved, i in zip(received_notices.values(), range(received_notices.count())):
            notice = Notifications.objects.get(id=receicved['notification_id'])
            notice_contents[f'{i}'] = set_notice_box_data(notice)
    return notice_contents

def get_friend_list(request):
    online_contents, offline_contents = {}, {}
    friends = Friends.objects.filter(user_id = request.user.id)
    
    if friends :
        for friend, i in zip(friends.values(), range(friends.count())):
            friend_info = user_model.objects.get(id=friend['friend_id'])
            friend_status, friend_content = set_friend_list_data(friend_info)
            if friend_status :
                online_contents[f'{i}'] = friend_content
            else :
                offline_contents[f'{i}'] = friend_content
    return {'online' : online_contents, 'offline': offline_contents}

def check_new_message(user, room_num):
    messages = Messages.objects.filter(conversation_id=room_num).exclude(sender_id=user).values_list('id', flat=True)
    for message_id in messages:
        result = MessageReceivers.objects.filter(message_id=message_id, receiver_id=user, is_read=False).exists()
        if result:
            return "new"
    return ""
        

def get_chatting_room_list(request):
    chat_lists_num = []
    chatting_list_contents = {}
    chat_lists = ConversationParticipants.objects.filter(user_id=request.user.id)
    
    if chat_lists:
        for chatting in chat_lists.values() :
            chat_lists_num.append(chatting['conversation_id'])
        for chat in chat_lists_num:
            conv_room = ConversationParticipants.objects.filter(conversation_id=chat)
            for room, i in zip(conv_room.values(), range(conv_room.count())):
                user_data = user_model.objects.get(id=room['user_id'])
                if user_data.id != request.user.id:
                    chatting_list_contents[f'{i}'] = create_chatting_room(user_data, room)
                    chatting_list_contents[f'{i}']['get_new'] = check_new_message(request.user.id, chat)
                    
    return chatting_list_contents

def get_curr_user_data(request):
    current_user_content = ""
    user_info_template = get_template('include/user_detail.html')
    current_user = user_model.objects.get(id=request.user.id)
    user_data = {
        'id' : current_user.id,
        'email' : current_user.email,
        'name' : current_user.name,
        'profile_picture' : current_user.profile_picture,
        'status_message' : current_user.status_message if current_user.status_message and current_user.status_message != "None" else "",
    }
    current_user_content = user_info_template.render(user_data)
    return current_user_content , current_user.status 

def conv_user_data(user, roomnum):
    conv_user = ConversationParticipants.objects.filter(conversation_id=roomnum).exclude(user_id=user).first()    
    conv_user = user_model.objects.get(id=conv_user.user_id)
    last_message = Messages.objects.filter(conversation_id=roomnum).exclude(sender_id=user).last()
    last_reply_time = last_message.timestamp.strftime("%Y-%m-%d %H:%M:%S")
    if Conversations.objects.get(id=roomnum).type == 'private':
        conv_status = 'offline'
        if conv_user.is_online :
            if conv_user.status == 'online':
                conv_status = 'online'
            elif conv_user.status == 'away' :
                conv_status = 'away'
    else:
        conv_status = ''
                    
    conv_user_content = {
        'conv_user' : conv_user.name,
        'conv_status' : conv_status,
        'conv_pic' : conv_user.profile_picture,
        'last_reply_time' : last_reply_time,
        'room_number' : roomnum,
    }
    return conv_user_content            
        
 
def get_message_data(request):
    chat_content = ""
    message_contents = ""
    conv_user_content = ""
    prev_message_date = datetime(2000, 1, 1) # 시간을 비교하기 위해 임의의 값으로 설정
    conversations_num = json.loads(request.body.decode('utf-8'))['room_num']
    chat_page_template = get_template('contents/chatting.html')
    get_messages = Messages.objects.filter(conversation_id=conversations_num)
    message_template = get_template('include/message_box.html')
    
    
    if get_messages:
        for message in get_messages.values() :
            prev_message_date, get_temp = create_message_box(message, prev_message_date)
            try:
                MessageReceivers.objects.get(message_id=message['id'], receiver_id=request.user.id)
                get_temp['direction'] = 'given'
            except ObjectDoesNotExist:
                get_temp['direction'] = 'send'
            message_contents += message_template.render(get_temp)
        conv_user_content = conv_user_data(request.user.id, conversations_num)
        conv_user_content['message_boxs'] = message_contents
        conv_user_content['csrf_token'] = request.META.get('CSRF_COOKIE'),
        
    chat_content = mark_safe(chat_page_template.render(conv_user_content))
    return JsonResponse({'message':'Success', 'data':chat_content})

def push_load_data(request):
    data_dic = {}

    data_dic['notice_data'] = get_notice_list(request)
    data_dic['friend_list'] = get_friend_list(request)
    data_dic['chatting_room_list'] = get_chatting_room_list(request)
    data_dic['curr_user_data'], status = get_curr_user_data(request)
    data_dic['present_status'] = status
    return JsonResponse(data_dic)

def load_chatting_main_page(request):
    if request.method =="GET":
        if request.user.is_authenticated:
            context = {
                'csrf_token':request.META.get('CSRF_COOKIE'),
                'user_id' : request.user.id,
                }
            
            return render(request, 'contents/chatting_viewer_page.html', context)
        else:
            return redirect('../')

def user_logout(request):
    if request.method == 'POST':
        # print(request.POST)
        current_user = user_model.objects.get(email=request.user.email)
        current_user.is_online = False
        current_user.save()
        logout(request)
        return JsonResponse({'message':'Success'})