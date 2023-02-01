from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import authenticate, login, logout
from .models import Users
import json

def loginCheck(request):
    if request.user.is_authenticated:
        return True
    else:
        return False

def loginView(request):
    if request.method == 'GET':
        loginCheck(request)
    elif request.method == 'POST':
        userID = request.POST['userID']
        userPW = request.POST['userPW']
        user = authenticate(username=userID, password=userPW)
        if user is not None:
            login(request, user)
    if loginCheck(request):
        return redirect('/chatbot')
    else:
        return render(request, 'login/login.html')
    
def logoutView(request):
    logout(request)
    return redirect('login:login')

# def getUserModel(request):
#     usermodel = Users.objects.all()
#     context = {
#         "users":usermodel,
#         "user":json.dumps([user.json() for user in usermodel])
#     }
    
#     print(context)

def signupView(request):
    # usermodels = getUserModel(request)
    if request.method == 'POST':
        userID = request.POST['userID']
        userPW = request.POST['userPW']
        userName = request.POST['userName']
        userEmail = request.POST['userEmail']
        
        # user = Users.objects.create_user(userID, userEmail, userPW)
        # user.name = userName
        # user.save()
        return redirect('login:login')
    return render(request, 'login/signup.html')