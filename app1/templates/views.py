from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'homepage.html')

def contact(request):
    return render(request, 'contact.html')