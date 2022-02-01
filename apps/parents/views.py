from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from . models import Parents
from django.template import loader
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def parents(request):
    total_students = Parents.objects.count()
    students_data = Parents.objects.all()

    context = {
        'total_students': total_students,
        'students_data': students_data,
        # 'total_teachers': total_teachers,
        # 'total_parents': total_parents
    }

    html_template = loader.get_template('parents/parentsindex.html')
    print(html_template)
    return HttpResponse(html_template.render(context, request))

