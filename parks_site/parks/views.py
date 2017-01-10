from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("This will become a list of all Parks.")

