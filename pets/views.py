from django.shortcuts import redirect, render
from .models import Pet, Like
from .forms import CreatePetForm

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

def create_pet(req):
    if req.method == "GET":
        return render(req, 'pets/pet_create.html', {'form': CreatePetForm()})
    else:
        form = CreatePetForm(req.POST)
        if form.is_valid():
            form.save()
            return redirect('list pets')
        return render(req, 'pets/pet_create.html', {'form': form})

def edit_pet(req, pk):
    pet = Pet.objects.get(pk=pk)
    if req.method == "GET":
        return render(req, 'pets/pet_edit.html', {'form': CreatePetForm(instance=pet)})
    else:
        updated_pet = CreatePetForm(req.POST, instance=pet)
        if updated_pet.is_valid():
            updated_pet.save()
            return redirect("list pets")
        return render(req, 'pets/pet_edit.html', {'form': CreatePetForm(req.POST)})
 
def delete_pet(req, pk):
    print(req)
    pet = Pet.objects.get(pk=pk)
    pet.delete()
    return redirect('list pets')

# def delete_book_entry(req, pk):
#     book_for_deletion = Book.objects.get(pk=pk)
#     book_for_deletion.delete()
#     return render(req, 'deletion.html')