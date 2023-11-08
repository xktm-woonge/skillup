from django.shortcuts import render, redirect
from django.urls import reverse
from django.core.mail import send_mail
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from django.contrib.auth.hashers import make_password
from chatting_main_page.models import Friends
import random

user_model = get_user_model()

def load_register(request):
    '''
        회원 가입 페이지 로드 시 실행 될 코드
    '''
    if request.method == 'GET':
        request.session['ceri_result'] = 'Fail'
        return render(request, 'register_page/register.html')
    
def get_email(request):
    '''
        인증 메일을 보낼 메일 수신
    '''
    if request.method == 'POST':
        emailData = request.POST.get('email')
        if user_model.objects.filter(email=emailData).exists():
            return JsonResponse({'message': 'Error', 'error': 'email_duplicate'})
        else:
            send_email_certification(request, emailData)
            return JsonResponse({'message':'Success'})
    
def send_email_certification(request, email):
    random_number = make_random_ceri_code()
    print(random_number)
    subject = '회원 가입 확인 이메일'
    message = f'''
        안녕하세요.
        인증 번호를 입력하세요.
        인증 번호는 {random_number} 입니다.
    '''
    from_email = 'endgameteam@gmail.com'
    recipient_email_list = [email]
    # send_mail(subject, message, from_email, recipient_email_list)
    request.session['email'] = email
    print(request.session['email'])
    request.session['certification_number'] = random_number

    
def conf_email(request):
    if request.method == 'POST':
        current_email = request.POST.get('email')
        saved_email = request.session.get('email')
        if saved_email == current_email:
            return JsonResponse({'message': 'Success'})
        else:
            request.session['certification_number'] = 000000
            return JsonResponse({'message': 'Error', 'error': 'Invalid email'})

        
def conf_ceri_num(request):
    if request.method == 'POST':
        input_cert_num = int(request.POST.get('cert_num'))
        certification_number = request.session.get('certification_number')
        if input_cert_num == certification_number:
            request.session['ceri_result'] = 'Success'
            return JsonResponse({'message': 'Success'})
        else:
            return JsonResponse({'message': 'Error', 'error': 'Invalid certification number'})

def add_user(request):
    if request.method == 'POST':
        user_password = request.POST.get('password')
        request.session['password'] = user_password
        if request.session['ceri_result'] == 'Success':
            random_user_name = make_random_user_name()
            while True:
                if user_model.objects.filter(name=random_user_name).exists():
                    random_user_name = make_random_user_name()
                else:
                    break
            user_model.objects.create_user(email=request.session['email'], password=request.session['password'],name=random_user_name)
            add_friends_chatbot(user_model.objects.get(email=request.session['email']).id)
            return JsonResponse({'message':'Success'})
        else:
            return JsonResponse({'message':'Error', 'error':'cert_error'})

def make_random_ceri_code():
    min_value = 100000
    max_value = 999999
    
    return random.randint(min_value, max_value)

def make_random_user_name():
    random_name = f'USER_{random.randint(0000, 9999)}'
    return random_name

def add_friends_chatbot(user_id):
    chatbot_ted_id = user_model.objects.get(name='TED').id
    Friends.objects.create(friend_id=chatbot_ted_id, user_id=user_id)