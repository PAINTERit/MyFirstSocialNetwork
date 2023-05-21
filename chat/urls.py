from django.urls import path
from chat.views import all_chats, room, check_room

urlpatterns = [
    path('all/', all_chats, name='all_chats'),
    path('check_room/', check_room, name='check_room'),
    path('<int:room_id>/', room, name='room'),
]