from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

from apps.teachers.models import Teachers


def teachers(request):
    query = Teachers.objects.all()
    total=query.count()
    context = {
        'query': query,
        'total': total,
    }

    return render(request,'teachers/teachersindex.html',context)

