from django.urls import path
from friend.views import friends, find_friend

urlpatterns = [
    path('friendlist/', friends, name='friends'),
    path('search/', find_friend, name='find_friend'),
]