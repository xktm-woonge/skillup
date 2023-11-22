
from .models import *
from datetime import datetime

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

def create_chatting_room(user_data, room):
    try:
        final_message = Messages.objects.filter(conversation_id=room).last().message_text
    except AttributeError:
        final_message = ''
    show_user_status = 'offline' if not user_data.is_online else user_data.status
    
    context = {
        'conv_user_name' : user_data.name, 
        'conv_final_message' : final_message,
        'conv_picture' : user_data.profile_picture,
        'user_status' : show_user_status,
        'room_num' : room,
        'team' : '',
    } 
    return context

def check_new_message(user, room_num):
    messages = Messages.objects.filter(conversation_id=room_num).exclude(sender_id=user).values_list('id', flat=True)
    for message_id in messages:
        result = MessageReceivers.objects.filter(message_id=message_id, receiver_id=user, is_read=False).exists()
        if result:
            return "new"
    return ""