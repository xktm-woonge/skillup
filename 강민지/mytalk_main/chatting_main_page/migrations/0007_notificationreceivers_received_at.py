# Generated by Django 4.2.2 on 2023-11-28 13:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chatting_main_page', '0006_conversations_last_chat_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificationreceivers',
            name='received_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
