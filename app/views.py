from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def sachivji(request):
    d={'name':'rinky'}
    return render(request,'sachivji.html',d)