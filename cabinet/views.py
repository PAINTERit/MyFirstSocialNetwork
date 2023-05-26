from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from cabinet.models import Person
from post.models import Post
from friend.models import Friend


@login_required
def account(request, user_username):
    user = Person.objects.filter(username=request.user.username).first()
    user_posts = Post.objects.filter(author_id=user.id).values('title', 'content')
    user_friends = Friend.objects.filter(user=user).select_related('friend')
    friends_info = []
    for friend in user_friends:
        friend_info = {
            'avatar': friend.friend.avatar,
            'first_name': friend.friend.first_name,
            'last_name': friend.friend.last_name,
            'email': friend.friend.email,
        }
        friends_info.append(friend_info)
    context = {'user_posts': user_posts,
               'user_friends': friends_info}
    return render(request, 'cabinet/account.html', context)


@login_required
def update_info(request):
    if request.method == 'POST':
        user = Person.objects.filter(id=request.user.id).first()
        user.avatar = request.FILES.get('avatar')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.country = request.POST.get('country')
        user.city = request.POST.get('city')
        user.birth_date = request.POST.get('birth_date')
        user.description = request.POST.get('description')
        user.save()
        return render(request, 'cabinet/account.html')
    return render(request, 'cabinet/update_info.html')
