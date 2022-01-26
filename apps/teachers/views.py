from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from apps.teachers.models import Teachers


def teachers(request):
    total=Teachers.objects.all().count()
    query = Teachers.objects.all()
    context = {
        'query': query,
        'total': total,
    }

    return render(request,'home/icons.html',context)

