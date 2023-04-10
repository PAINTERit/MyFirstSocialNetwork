from django.db import models


class Ticket(models.Model):
    email = models.EmailField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    closed = models.BooleanField(default=False)


def convert(ticket):
    ticket = dict(ticket)
    ticket.pop('csrfmiddlewaretoken')
    for key in ticket:
        ticket[key] = ''.join(ticket[key])
    return ticket
