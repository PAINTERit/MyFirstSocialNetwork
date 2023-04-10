from django.urls import path
from other.views import index

urlpatterns = [
    path('', index, name='index')
]
