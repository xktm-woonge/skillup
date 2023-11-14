
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
        context['message_box__date'] = f'<time class="message_box--date">{data["timestamp"].strftime("%B %d, %Y")}</time>'
        prev_date = data['timestamp']
    else :
        context['message_box__date'] = ''
    return prev_date, context