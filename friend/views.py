from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def friends(request):
    return render(request, 'friend/friends.html')


@login_required
def find_friend(request):
    return render(request, 'friend/find_friend.html')
