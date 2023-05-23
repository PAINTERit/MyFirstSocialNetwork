from django.db import models
from cabinet.models import Person


class Room(models.Model):
    room_id = models.CharField(max_length=50)
    user_id = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='users_id')
    friend_id = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='friends_id')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user_id', 'friend_id')


class Message(models.Model):
    author = models.ForeignKey(Person, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def last_30_messages():
        return Message.objects.order_by('-created_at').all()[:30]
