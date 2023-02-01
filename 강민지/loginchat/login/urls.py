from django.urls import path, include
from . import views

app_name = 'login'

urlpatterns = [
    path('', views.loginView, name='login'),
    path('logout/', views.logoutView, name='logout'),
    path('signup/', views.signupView, name='signup'),
    path('chatbot/', include('chatbot.urls', namespace='chatbot')),
]