# Create your views here.

from django.http import HttpResponse
from django.shortcuts import render, redirect

def owners(request):
    # ...
    print("request received")
    return render(request, 'accounts/login.html')

