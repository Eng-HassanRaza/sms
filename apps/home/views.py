# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from apps.students.models import Students
from apps.teachers.models import Teachers
from apps.parents.models import Parents



@login_required(login_url="/login/")
def index(request):
    total_students = Students.objects.count()
    total_teachers = Teachers.objects.count()
    total_parents = Parents.objects.count()
    context = {
               'segment': 'index',
                'total_students': total_students,
                'total_teachers': total_teachers,
                'total_parents': total_parents
               }

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


# @login_required(login_url="/login/")
# def pages(request):
#     context = {}
#     # All resource paths end in .html.
#     # Pick out the html file name from the url. And load that template.
#     try:
#
#         load_template = request.path.split('/')[-1]
#
#         if load_template == 'admin':
#            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 return HttpResponseRedirect(reverse('admin:index'))
#         context['segment'] = load_template
#
#         html_template = loader.get_template('home/' + load_template)
#         return HttpResponse(html_template.render(context, request))
#
#     except template.TemplateDoesNotExist:
#
#         html_template = loader.get_template('home/page-404.html')
#         return HttpResponse(html_template.render(context, request))
#
#     except:
#         html_template = loader.get_template('home/page-500.html')
#         return HttpResponse(html_template.render(context, request))
