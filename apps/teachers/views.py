from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from apps.teachers.models import Teachers


def teachers(request):
    query = Teachers.objects.all()
    context = {
        'query': query
    }

    return render(request,'icons.html',context)

