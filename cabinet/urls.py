from django.urls import path
from cabinet.views import account, update_info

urlpatterns = [
    path('update/', update_info, name='update_info'),
    path('<str:user_username>/', account, name='account'),
]
