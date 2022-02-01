from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
# from . models import Owners
from django.template import loader
from django.contrib.auth.decorators import login_required


@login_required(login_url="/login/")
def owners(request):
    # total_students = Parents.objects.count()
    # students_data = Parents.objects.all()

    context = {
        'total_students': "Testing",
        'students_data': "testing 2"
    }

    html_template = loader.get_template('owners/ownersindex.html')
    print(html_template)
    return HttpResponse(html_template.render(context, request))

