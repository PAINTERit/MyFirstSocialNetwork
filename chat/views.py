import json

from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.shortcuts import render


@login_required
def all_chats(request):
    return render(request, 'chat/all_chats.html')


@login_required
def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name_json': mark_safe(json.dumps(room_name)),
                                              'username': mark_safe(json.dumps(request.user.username))})
