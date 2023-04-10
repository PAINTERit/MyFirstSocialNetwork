from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from post.models import Post


@login_required
def index(request):
    user_posts = Post.objects.all().values('title', 'content')
    context = {'user_posts': user_posts}
    return render(request, 'other/index.html', context)
