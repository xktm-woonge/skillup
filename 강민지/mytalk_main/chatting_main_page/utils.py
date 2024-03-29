
from .models import *
from django.contrib.auth import get_user_model
from datetime import datetime
from django.templatetags.static import static

user_model = get_user_model()

def notice_pretreatment(data):
    try:
        sender_name = user_model.objects.get(id=data.sender_id).name
    except user_model.DoesNotExist:
        sender_name = 'SYSTEM'
        
    if data.type in ['system', 'danger']:
        img_src = static('icon/Notification.svg')
    else:
        get_sender_profile_pic = user_model.objects.get(id=data.sender_id).profile_picture
        img_src = static(f'img/{get_sender_profile_pic}')
    return sender_name, img_src

def set_notice_box_data(notice):
    sender_name, img_src = notice_pretreatment(notice)
    context = {
        'noti_type' : notice.type,
        'noti_num' : f'num_{notice.id}',
        'img_src' : img_src,
        'content' : notice.content if not notice.type == "friends" else sender_name,
        'title' : sender_name,
        'button_type': notice.type,
    }
    return context

def create_message_box(data, prev_date):     
    context = {
        'message' : '',
        'time' : '',
        'message_box__date' : '',
    }
    if data:
        context['message'] = data['message_text']
        context['time'] = data['timestamp'].strftime("%H:%M")
        
        if data['timestamp'].date() != prev_date.date():
            context['message_box__date'] = f'<time class="message_box__date" datetime="{data["timestamp"]}">{data["timestamp"].strftime("%Y-%m-%d")}</time>'
            prev_date = data['timestamp']

    return prev_date, context

def make_friends(user, friend):
    Friends.objects.create(friend_id=friend, user_id=user)
    Friends.objects.create(friend_id=user, user_id=friend)

def set_friend_list_data(friend_info):
    if friend_info.status == 'offline':
        show_user_status = False
    else:
        show_user_status = friend_info.is_online
    
    context = {
        "name" : friend_info.name,
        "team" : '',
        "status" : 'offline' if not friend_info.is_online else friend_info.status,
        "status_message" : friend_info.status_message if friend_info.status_message and friend_info.status_message != "None" else "",
        "profile_picture" : friend_info.profile_picture,
    }
    return show_user_status, context

def create_chatting_room(user_data, room, room_type, user):
    try:
        last_message = Messages.objects.filter(conversation_id=room).last()
        final_message = last_message.message_text
        final_message_time = last_message.timestamp
        
    except AttributeError:
        final_message = ''
        final_message_time = ''
    show_user_status = 'offline' if not user_data.is_online else user_data.status
    
    if room_type == "private":
        room_name = user_data.name
    else :
        room_user = list(ConversationParticipants.objects.filter(conversation_id=room).exclude(user_id=user).values_list("user_id", flat=True))
        room_name = []
        for i in room_user:
            user_name = user_model.objects.get(id=i).name
            room_name.append(user_name)
        room_name = ', '.join(room_name)
        
    
    context = {
        'conv_user_name' : room_name, 
        'conv_final_message' : final_message,
        'conv_picture' : user_data.profile_picture,
        'user_status' : show_user_status,
        'room_num' : room,
        'team' : '',
        'type' : room_type,
        'time': final_message_time,
    } 
    return context

def check_new_message(user, room_num):
    messages = Messages.objects.filter(conversation_id=room_num).exclude(sender_id=user).values_list('id', flat=True)
    for message_id in messages:
        result = MessageReceivers.objects.filter(message_id=message_id, receiver_id=user, is_read=False).exists()
        if result:
            return "new"
    return ""