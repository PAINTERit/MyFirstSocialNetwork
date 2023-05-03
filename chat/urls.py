from django.urls import path
from chat.views import all_chats, room

urlpatterns = [
    path('all/', all_chats, name='all_chats'),
    path('<str:room_name>/', room, name='room'),
]