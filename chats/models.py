from django.db import models
from users.models import User


class Chat(models.Model):
    class Meta:
        db_table = "chats"

    name = models.CharField(max_length=250)
    participants = models.ManyToManyField(User)


class Message(models.Model):
    class Meta:
        db_table = "messages"

    text = models.TextField()
    chat = models.ForeignKey(Chat, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    data_time = models.DateTimeField(auto_now=True)
