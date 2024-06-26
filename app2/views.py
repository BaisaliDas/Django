from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def admin(response):
    return HttpResponse('<h1> hello every one this is from app2 Goodly</h1>')
def admin2(request):
    return render(request,'index.html')
def jinja_print(request):
    d={'name':'Baishu','age':24}
    return render(request,'jinja_print.html',context=d)
def jinja_operation(request):
    d={'name':'XYZ','age':26}
    return render(request,'jinja_operation.html',context=d)