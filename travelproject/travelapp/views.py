from django.shortcuts import render
from django.http import HttpResponse
from .models import Place
# Create your views here.


def demo(request):
    obj=Place.objects.all()
    return render(request,"home.html",{"results":obj})
def addition(request):
    x=int(request.GET['num1'])
    y=int(request.GET['num2'])
    res=x+y
    return render(request,'result.html',{"result":res})
def about(request):
    return render(request,"about.html")
def contact(request):
    return render(request,"contact.html")
