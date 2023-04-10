from django.urls import path
from chat.views import all_chats, chat

urlpatterns = [
    path('all/', all_chats, name='all_chats'),
    path('', chat, name='chat'),
]