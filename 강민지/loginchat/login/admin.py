from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Users

@admin.register(Users)
class UserAdmin(admin.ModelAdmin):
    pass
