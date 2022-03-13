from django.urls import path
from .views import list_pets, pet_details, like_pet


urlpatterns = [
    path('', list_pets, name="list pets"),
    path('pet_details/<int:pk>', pet_details, name="dtls"),
    path('like/<int:pk>', like_pet, name="like pet"),
]
