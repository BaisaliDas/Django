from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def admin(response):
    return HttpResponse('<h1> hello every one this is from app2 Goodly</h1>')
def admin2(response):
    return render(response,'index.html')