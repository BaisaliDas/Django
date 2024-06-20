from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def telugu(request):
    return HttpResponse("This is our telugu movie function")

def Baisali(request):
    return HttpResponse('<h1><marquee>shant kuutte, Era kukka <marquee></h1>')

def changu(request):
    return HttpResponse('<h1><marquee>mangu, changu, ill beat u<marquee></h1>')