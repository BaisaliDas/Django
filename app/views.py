from django.shortcuts import render
<<<<<<< HEAD

# Create your views here.
def australia(request):
    return render(request,'australia.html')
def brisbane(request):
    return render(request,'brisbane.html')
=======
from django.http import HttpResponse
# Create your views here.
def telugu(response):
    return HttpResponse("This is our telugu movie function")

def Baisali(response):
    return HttpResponse('<h1><marquee>shant kuutte, Era kukka <marquee></h1>')

def moovie(response):
    return HttpResponse('<h1><marquee>watch movie<marquee></h1>')

>>>>>>> 5b155ec8e3e8ef898c7105968d345dfa7d0c3c98
