import json

from django.contrib.auth.decorators import login_required
from django.utils.safestring import mark_safe
from django.shortcuts import render, redirect
from chat.models import Room
from cabinet.models import Person
import random


@login_required
def all_chats(request):
    return render(request, 'chat/all_chats.html')


@login_required
def room(request, room_id):
    return render(request, 'chat/room.html', {'room_name_json': mark_safe(json.dumps(room_id)),
                                              'username': mark_safe(json.dumps(request.user.username))})


def create_room(request):
    if request.method == 'POST':
        room_id = random.randint(1, 999999)
        user_id = Person.objects.filter(id=request.user.id).first()
        friend_id = Person.objects.filter(id=request.POST.get('friend_id')).first()
        rooms = list(Room.objects.filter(room_id=room_id).all())

        while True:
            if room in rooms:
                room_id = random.randint(1, 999999)
            break

        Room.objects.create(room_id=room_id, user_id=user_id, friend_id=friend_id)
        Room.objects.create(room_id=room_id, user_id=friend_id, friend_id=user_id)
        return redirect('room', room_id=room_id)


def check_room(request):
    if request.method == 'POST':
        user_id = Person.objects.filter(id=request.user.id).first()
        friend_id = Person.objects.filter(id=request.POST.get('friend_id')).first()
        room = Room.objects.filter(user_id=user_id, friend_id=friend_id).first()
        if room is None:
            return create_room(request)
        else:
            room_id = room.room_id
            return redirect('room', room_id=room_id)
