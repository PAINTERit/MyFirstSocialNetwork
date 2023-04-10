from django.db import models

from cabinet.models import Person


class Friend(models.Model):
    user = models.ForeignKey(Person, on_delete=models.CASCADE, related_name='friends')
    friend = models.ForeignKey(Person, on_delete=models.CASCADE)
