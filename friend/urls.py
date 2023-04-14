from django.urls import path
from friend.views import friends, find_friend, send_friend_request, friend_request, accept_friend_request, \
    reject_friend_request

urlpatterns = [
    path('search/send_friend_request/<int:to_user_id>/', send_friend_request, name='send_friend_request'),
    path('friendlist/', friends, name='friends'),
    path('search/', find_friend, name='find_friend'),
    path('friend_request/', friend_request, name='friend_request'),
    path('friend_request/accept/', accept_friend_request, name='accept_friend_request'),
    path('friend_request/reject/', reject_friend_request, name='reject_friend_request'),
]
