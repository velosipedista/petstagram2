from django.http import HttpResponse
from django.shortcuts import render

def pet_basic(req):
    return HttpResponse('Pets View')