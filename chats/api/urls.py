from .views import ChatAPIView, MessageAPIView
from users.api.views import UserAPIView, UserDestroyView
from django.urls import path

app_name = 'api_chats'
urlpatterns = [
    path('group_chat/', ChatAPIView.as_view(), name="chat_api"),
    path('messages/', MessageAPIView.as_view(), name="messages_api"),
    path('group_chat/<int:chat_id>/participants/', UserAPIView.as_view(), name="add_participant_api"),
    path('group_chat/<int:chat_id>/participants/<int:id>/',
         UserDestroyView.as_view(), name="remove_participant_api"),
]
