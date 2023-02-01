from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import User

def loginView(request):
    if request.method == 'POST':
        userID = request.POST.get('userID', '')
        userPW = request.POST.get('userPW', '')
        user = authenticate(username= userID, password = userPW)
        if user is not None:
            login(request, user)
        else:
            pass
    return render(request, 'user/login.html')


def logoutView(request):
    logout(request)
    return redirect("user:login")

def signupView(request):
    if request.method == 'POST':
        username = request.POST.get('userID', '')
        password = request.POST.get('userPW', '')
        lastname = request.POST.get('lastname', '')
        firstname = request.POST.get('firstname', '')
        email = request.POST.get('email', '')
        
        user = User.objects.create_user(username, email, password)
        user.last_name = lastname
        user.first_name = firstname
        user.save()
        return redirect('user:login')
    
    return render(request, 'user/signup.html')