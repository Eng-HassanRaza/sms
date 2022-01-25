from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from . models import Students
from django.template import loader

def students(request):
    total_students = Students.objects.count()
    # total_teachers = Teachers.objects.count()
    # total_parents = Parents.objects.count()
    context = {
        'segment': 'index',
        'total_students': total_students,
        # 'total_teachers': total_teachers,
        # 'total_parents': total_parents
    }

    html_template = loader.get_template('home/students.html')
    return HttpResponse(html_template.render(context, request))

