from django.http import HttpResponseNotAllowed, Http404
from rest_framework import generics, mixins
from rest_framework.response import Response

from .serializers import ChatSerializer, MessageSerializer
from chats.models import Chat, Message
from users.models import User


class ChatAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = ChatSerializer

    def get_queryset(self):
        return Chat.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class MessageAPIView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = MessageSerializer

    def get_queryset(self):
        chat_id = self.request.GET.get('chat')
        if chat_id and Chat.objects.filter(id=chat_id).exists():
            chat = Chat.objects.get(id=chat_id)
            return chat.messages
        return Message.objects.all()

    def post(self, request, *args, **kwargs):
        user_id = request.data.get('author')
        chat_id = request.data.get('chat')
        if (user_id and chat_id and User.objects.filter(id=user_id).exists()
                and Chat.objects.filter(id=chat_id).exists()):
            chat = Chat.objects.get(id=chat_id)
            if chat.participants.filter(id=user_id).exists():
                return self.create(request, *args, **kwargs)
            else:
                return Response("You do not have permissions to send message in this chat")
        return Response("User or chat does not exist")

