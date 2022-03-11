from django.http import HttpResponse, response
from django.shortcuts import render

def pet_all(req):
    return render(req, 'pet_list.html')