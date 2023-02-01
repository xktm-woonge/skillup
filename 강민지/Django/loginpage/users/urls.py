from django.urls import path
from . import views

app_name = "user"

urlpatterns = [
    path('', views.loginView, name="login"),
    path('logout', views.logoutView, name="logout"), 
    path('signup/', views.signupView, name="signup"), 
]
