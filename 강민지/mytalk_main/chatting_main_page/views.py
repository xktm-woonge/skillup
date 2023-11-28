import json
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, logout
from django.template.loader import get_template
from django.utils.safestring import mark_safe
from datetime import datetime
from .models import *
from .utils import *
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError

user_model = get_user_model()
        
def get_notice_list(request):
    notice_contents = {}
    received_notices = NotificationReceivers.objects.filter(receiver=request.user.id, is_conform=False).order_by('-received_at')
    if received_notices :
        for receicved, i in zip(received_notices.values(), range(received_notices.count())):
            notice = Notifications.objects.get(id=receicved['notification_id'])
            timestamp_string = receicved['received_at'].strftime('%Y-%m-%d %H:%M:%S')
            notice_contents[f'{i}'] = set_notice_box_data(notice)
            notice_contents[f'{i}']['received_at'] = timestamp_string
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

def get_chatting_room_list(request):
    chatting_list_contents = {}
    user = request.user.id
    chat_sort_list = list(Conversations.objects.order_by("-last_chat_at").values_list("id", flat=True))
    chat_lists = list(ConversationParticipants.objects.filter(user_id=user).values_list('conversation_id', flat=True))
    chat_lists = [value for value in chat_sort_list if value in chat_lists]
    
    if chat_lists:
        for chat, i in zip(chat_lists, range(len(chat_lists))):
            conv_room = ConversationParticipants.objects.filter(conversation_id=chat).exclude(user_id=user).first()
            room_type = Conversations.objects.get(id=chat).type
            
            user_data = user_model.objects.get(id=conv_room.user_id)
            chatting_list_contents[f'{i}'] = create_chatting_room(user_data, conv_room.conversation_id, room_type, user)
            chatting_list_contents[f'{i}']['get_new'] = check_new_message(user, chat)
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
    try:
        last_reply_time = Messages.objects.filter(conversation_id=roomnum).exclude(sender_id=user).last().timestamp.strftime("%Y-%m-%d %H:%M:%S")
    except AttributeError:
        last_reply_time = ''
    
    room_type = Conversations.objects.get(id=roomnum).type
        
    if room_type == 'private':
        room_name = conv_user.name
        conv_status = 'offline'
        if conv_user.is_online :
            if conv_user.status == 'online':
                conv_status = 'online'
            elif conv_user.status == 'away' :
                conv_status = 'away'
    else:
        conv_status = ''
        room_user = list(ConversationParticipants.objects.filter(conversation_id=roomnum).exclude(user_id=user).values_list("user_id", flat=True))
        room_name = []
        for i in room_user:
            user_name = user_model.objects.get(id=i).name
            room_name.append(user_name)
        room_name = ', '.join(room_name)
        
                    
    conv_user_content = {
        'conv_user' : room_name,
        'conv_status' : conv_status,
        'conv_pic' : conv_user.profile_picture,
        'last_reply_time' : last_reply_time,
        'room_number' : roomnum,
        'type' : room_type,
    }
    return conv_user_content
        
 
def get_message_data(request):
    chat_content = ""
    message_contents = ""
    conv_user_content = {}
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

def set_changed_user_info(request):
    user_info = json.loads(request.body.decode('utf-8'))
    try:
        user_model.objects.filter(id=request.user.id).update(name=user_info["text"], status_message=user_info["textarea"])
        return JsonResponse({'message':'Success'})
    except IntegrityError:
        return JsonResponse({'message':'user_name_duplication'})
    
def request_pretreatment(user, friend):  
    try:
        user_request = Notifications.objects.filter(type="friends", sender_id=user).values_list("id", flat=True)
        for notinum in user_request:
            NotificationReceivers.objects.get(notification_id=notinum, receiver_id=friend, is_conform=False)
            return True, notinum
        return False, ""
    except ObjectDoesNotExist:
        return False, ""
    
def friend_request(request):
    if request.method == "POST":
        user = request.user.id
        email = json.loads(request.body.decode('utf-8'))["email"]
        try:
            requested_friend_id = user_model.objects.get(email=email).id
            friends = Friends.objects.filter(user_id=user).values_list("friend_id", flat=True)
            if requested_friend_id in friends:
                raise Exception
        except ObjectDoesNotExist:
            return JsonResponse({'message':'unsubscribed_email'})
        except Exception:
            return JsonResponse({"message":"already_executed"})
        else :
            has_user_request, _ = request_pretreatment(user, requested_friend_id)
            has_friend_request, notinum = request_pretreatment(requested_friend_id, user)
            
            if has_user_request:
                return JsonResponse({"message":"request_duplication"})
            elif not has_user_request and has_friend_request:
                return JsonResponse({"message":"request_to_each_other",'noti_num':notinum})
            elif not has_user_request and not has_friend_request:
                last_num = Notifications.objects.filter().last().id + 1
                Notifications.objects.create(id=last_num, type='friends', sender_id=user)
                NotificationReceivers.objects.create(notification_id=last_num, receiver_id=requested_friend_id)
                return JsonResponse({'message':'success', 'noti_num':last_num})

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