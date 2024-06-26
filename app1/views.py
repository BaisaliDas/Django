from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def rip(response):
    return HttpResponse('Rest in peace')
def fruits(response):
    return render(response,'fruits.html')