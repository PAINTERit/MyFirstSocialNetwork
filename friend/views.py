from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cabinet.models import Person
from friend.models import Friend, FriendRequest


@login_required
def friends(request):
    user = Person.objects.filter(username=request.user.username).first()
    user_friends = Friend.objects.filter(user=user).select_related('friend')
    friend_list = []
    for friend in user_friends:
        friend_info = {
            'id': friend.friend.id,
            'first_name': friend.friend.first_name,
            'last_name': friend.friend.last_name,
        }
        friend_list.append(friend_info)
    context = {'friends': friend_list}
    return render(request, 'friend/friends.html', context)


@login_required
def find_friend(request):
    friends = Person.objects.all()
    friend_requests = FriendRequest.objects.all()
    to_users = friend_requests.values_list('to_user', flat=True)
    friend_list = []
    for friend in friends:
        if friend.username != request.user.username and friend.username != 'admin' and friend.id not in to_users:
            friend_info = Person.objects.filter(username=friend).values('first_name', 'last_name', 'id').first()
            friend_list.append(friend_info)
    context = {'friends': friend_list}
    return render(request, 'friend/find_friend.html', context)


@login_required
def send_friend_request(request, to_user_id):
    from_user = Person.objects.filter(username=request.user.username).first()
    to_user = Person.objects.filter(id=to_user_id).first()
    friend_request = FriendRequest.objects.create(from_user=from_user, to_user=to_user)
    friend_request.save()
    return render(request, 'friend/find_friend.html')


@login_required
def friend_request(request):
    users = FriendRequest.objects.all().values_list('from_user', flat=True)
    user_list = []
    for user in users:
        user_info = Person.objects.filter(id=user).values('first_name', 'last_name').first()
        user_list.append(user_info)
    friend_requests = FriendRequest.objects.filter(to_user=request.user).select_related('from_user')
    return render(request, 'friend/friend_request.html', {'friend_requests': friend_requests, 'users': user_list})


@login_required
def accept_friend_request(request):
    friend_request = FriendRequest.objects.filter(to_user=request.user).first()
    if request.method == 'POST':
        from_user = friend_request.from_user
        to_user = friend_request.to_user
        Friend.objects.create(user=to_user, friend=from_user)
        Friend.objects.create(user=from_user, friend=to_user)
        friend_request.delete()
    return render(request, 'friend/friend_request.html')


@login_required
def reject_friend_request(request):
    friend_request = FriendRequest.objects.filter(to_user=request.user).first()
    if request.method == 'POST':
        friend_request.delete()
    return render(request, 'friend/friend_request.html')
