from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def planet(request):
    return render(request,'planet.html')
def person(request):
    return HttpResponse('<h1>Namaste Everyone . Welcome to India .</h1>')
