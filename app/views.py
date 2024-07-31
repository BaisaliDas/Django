from django.shortcuts import render

# Create your views here.
def australia(request):
    return render(request,'australia.html')
def brisbane(request):
    return render(request,'brisbane.html')