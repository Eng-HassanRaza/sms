from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from . models import Students
from django.template import loader
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def students(request):
    total_students = Students.objects.count()
    students_data = Students.objects.all()
    # total_teachers = Teachers.objects.count()
    # total_parents = Parents.objects.count()
    context = {
        'total_students': total_students,
        'students_data': students_data,
        # 'total_teachers': total_teachers,
        # 'total_parents': total_parents
    }

    html_template = loader.get_template('home/students.html')
    print(html_template)
    return HttpResponse(html_template.render(context, request))

