from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def students(request):
    # ...
    return HttpResponse('<h1>students Page</h1>')

