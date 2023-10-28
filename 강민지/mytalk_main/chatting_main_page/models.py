from django.db import models
from django.conf import settings

class Friends(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='user_friends')
    friend = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='friend_users')

class Conversations(models.Model):
    TYPE_CHOICES = [
        ('private', 'Private'),
        ('group', 'Group'),
    ]
    
    type = models.CharField(max_length=10, choices=TYPE_CHOICES, default='private')
    name = models.CharField(max_length=255, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    is_chatbot = models.BooleanField(default=False)

class ConversationParticipants(models.Model):
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

class Messages(models.Model):
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    conversation = models.ForeignKey(Conversations, on_delete=models.CASCADE)
    message_text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

class Notifications(models.Model):
    TYPE_CHOICES = [
        ('SYSTEM', 'System'),
        ('FRIEND_REQUEST', 'Friend Request'),
    ]

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications_received')
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    content = models.TextField()
    sender = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)
