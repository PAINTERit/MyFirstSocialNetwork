from django.shortcuts import render
from cabinet.models import Person
from post.models import Post


def account(request, user_username):
    user = Person.objects.filter(username=user_username).first()
    user_posts = Post.objects.filter(author_id=user.id).values('title', 'content')
    context = {'user_posts': user_posts}
    return render(request, 'cabinet/account.html', context)


def update_info(request):
    if request.method == 'POST':
        user = Person.objects.filter(id=request.user.id).first()
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.country = request.POST.get('country')
        user.city = request.POST.get('city')
        user.date_of_birth = request.POST.get('date_of_birth')
        user.description = request.POST.get('description')
        user.save()
    return render(request, 'cabinet/update_info.html')
