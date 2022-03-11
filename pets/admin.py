from django.contrib import admin
from .models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ['type','name','age']
    
admin.site.register(Pet, PetAdmin)
