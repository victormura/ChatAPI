from rest_framework import generics
from rest_framework.response import Response

from .serializers import UserSerializer
from users.models import User
from chats.models import Chat


class UserAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

    def post(self, request, *args, **kwargs):
        chat_id = kwargs.get('chat_id')
        if chat_id and Chat.objects.filter(id=chat_id).exists():
            chat = Chat.objects.get(id=chat_id)
            user = self.create(request, *args, **kwargs)
            chat.participants.add(user.data.get('id'))
            return user
        return self.create(request, *args, **kwargs)


class UserDestroyView(generics.DestroyAPIView):
    lookup_field = 'id'
    serializer_class = UserSerializer

    def delete(self, request, *args, **kwargs):
        chat_id = kwargs.get('chat_id')
        user_id = kwargs.get('id')
        if (chat_id and Chat.objects.filter(id=chat_id).exists()
                and user_id and User.objects.filter(id=user_id).exists()):
            chat = Chat.objects.get(id=chat_id)
            chat.participants.remove(user_id)
            return chat
        return self.delete(request, *args, **kwargs)
