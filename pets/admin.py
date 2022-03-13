from django.contrib import admin
from .models import Pet

class PetAdmin(admin.ModelAdmin):
    list_display = ['type','name','likes_count']

    def likes_count(self, obj):
        return obj.like_set.count()
    
admin.site.register(Pet, PetAdmin)
