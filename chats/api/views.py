from rest_framework import generics, mixins

from .serializers import ChatSerializer, MessageSerializer
from chats.models import Chat, Message


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
        return self.create(request, *args, **kwargs)

