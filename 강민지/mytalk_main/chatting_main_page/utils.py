
from .models import *
from datetime import datetime

def create_message_box(user_id, data, prev_date):
    
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
    return prev_date, context