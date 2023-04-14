from django.db import models
from cabinet.models import Person


class Friend(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='friendship_creator_set')
    friend = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='friend_set')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'friend')


class FriendRequest(models.Model):
    from_user = models.ForeignKey(Person, related_name='friend_requests_sent', on_delete=models.CASCADE)
    to_user = models.ForeignKey(Person, related_name='friend_requests_received', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('from_user', 'to_user')
