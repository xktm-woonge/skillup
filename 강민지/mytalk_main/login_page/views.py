from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model, authenticate, login
from django.http import JsonResponse

user_model = get_user_model()

def login_page_view(request):
    if request.method == 'GET':
        return render(request, 'login_page/login.html')
        
def try_login(request):
    # if request.method == 'POST':
    #     user_email = request.POST.get('email')
    #     password = request.POST.get('password')
    #     user = authenticate(request, email=user_email, password=password)
    #     if user is not None:
    #         login(request, user)
    #         return JsonResponse({'message':'Success'})
    #     else:
    #         return JsonResponse({'message': 'Error', 'error': 'login_fail'})
    return JsonResponse({'message':'Success'})