from django.urls import path
from .views import list_pets, pet_details


urlpatterns = [
    path('', list_pets, name="list pets"),
    path('pet_details/<int:pk>', pet_details, name="dtls"),
]
