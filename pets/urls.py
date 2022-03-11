from django.urls import path
from .views import pet_all


urlpatterns = [
    path('', pet_all)
]
