from django.urls import path
from .views import pet_basic


urlpatterns = [
    path('', pet_basic)
]
