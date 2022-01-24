from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def teachers(request):
    # ...
    return HttpResponse('<h1>teachers Page</h1>')

