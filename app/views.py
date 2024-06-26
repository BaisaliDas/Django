from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def telugu(request):
    return HttpResponse("This is our telugu movie function")

def Baisali(request):
    return HttpResponse('<h1><marquee>shant kuutte, Era kukka <marquee></h1>')

def moovie(request):
    return HttpResponse('<h1><marquee>watch movie<marquee></h1>')