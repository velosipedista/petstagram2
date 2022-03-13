from django.urls import path
from .views import list_pets


urlpatterns = [
    path('', list_pets, name="list pets")
]
