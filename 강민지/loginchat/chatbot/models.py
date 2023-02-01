from django.db import models

class MessagesWithChatBot(models.Model):
    class Meta:
        db_table = "MessagesWithChatBot"
    speaker = models.CharField(max_length=30)
    chat_text = models.TextField()