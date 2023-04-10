from django.urls import path
from support.views import support

urlpatterns = [
    path('', support, name='support')
]