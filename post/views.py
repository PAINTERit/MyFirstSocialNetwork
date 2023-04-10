from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from post.models import Post, convert


@login_required
def create_post(request):
    if request.method == 'POST':
        post_data = convert(request.POST)
        post_data['author_id'] = request.user.id
        Post.objects.create(**post_data)
    return render(request, 'post/create_post.html')
