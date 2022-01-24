from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def management(request):
    # ...
    return HttpResponse('<h1>Management Page</h1>')

