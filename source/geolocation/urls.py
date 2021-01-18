from django.urls import path
from .views import address

urlpatterns = [
    path('address/', address)
]