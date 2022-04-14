from django.urls import path
from .views import list_pets, pet_details, like_pet 
from .views import create_pet, edit_pet, delete_pet

urlpatterns = [
    path('', list_pets, name="list pets"),
    path('pet_details/<int:pk>', pet_details, name="dtls"),
    path('like/<int:pk>', like_pet, name="like pet"),
    path('create/', create_pet, name="create pet"),
    path('edit/<int:pk>', edit_pet, name="edit pet"),
    path('delete/<int:pk>', delete_pet, name="delete pet"),
]
