from django.db import models
from cabinet.models import Person


class Message(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def last_30_messages():
        return Message.objects.order_by('-created_at').all()[:30]
