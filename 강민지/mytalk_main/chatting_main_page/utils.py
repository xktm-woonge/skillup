
from .models import *
from datetime import datetime

def create_message_box(data, prev_date):     
    context = {
        'message' : data['message_text'],
        'time' : data['timestamp'].strftime("%H:%M"),
    }
    
    if data['timestamp'].date() != prev_date.date():
        context['message_box__date'] = f'<time class="message_box__date" datetime="{data["timestamp"]}">{data["timestamp"].strftime("%Y-%m-%d")}</time>'
        prev_date = data['timestamp']
    else :
        context['message_box__date'] = ''
    return prev_date, context