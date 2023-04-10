from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from support.models import Ticket, convert


@login_required
def support(request):
    if request.method == 'POST':
        Ticket.objects.create(**convert(request.POST))
    return render(request, 'support/support.html')
