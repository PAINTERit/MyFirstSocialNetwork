from django.db import models

from cabinet.models import Person


class Post(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)


def convert(post):
    post = dict(post)
    del post['csrfmiddlewaretoken']
    for key in post:
        post[key] = ''.join(post[key])
    return post
