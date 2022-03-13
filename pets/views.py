from django.shortcuts import redirect, render
from .models import Pet, Like

def list_pets(req):
    all_pets = Pet.objects.all()
    context = {
        'pets': all_pets 
    }

    return render(req, 'pet_list.html', context)

def pet_details(req, pk):
    pet = Pet.objects.get(pk=pk)
    likes_count = pet.like_set.count()
    context = {
        'pet': pet,
        'likes':likes_count,
    }
    return render(req, 'pet_detail.html', context )


def like_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    like = Like(pet=pet)
    like.save()
    return redirect('dtls', pet.id)
