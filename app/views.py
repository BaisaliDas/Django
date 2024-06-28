from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def telugu(response):
    return HttpResponse("This is our telugu movie function")

def Baisali(response):
    return HttpResponse('<h1><marquee>shant kuutte, Era kukka <marquee></h1>')

def moovie(response):
    return HttpResponse('<h1><marquee>watch movie<marquee></h1>')

