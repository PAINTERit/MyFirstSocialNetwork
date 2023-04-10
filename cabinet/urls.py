from django.urls import path
from cabinet.views import account, update_info

urlpatterns = [
    path('<str:user_username>/', account, name='account'),
    path('update/', update_info, name='update_info')
]
