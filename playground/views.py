from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def landing_page(request):
    return render(request,'desktop1.html',{'name':'Keshav'})

def login_page(request):
    return render(request,'main.html')