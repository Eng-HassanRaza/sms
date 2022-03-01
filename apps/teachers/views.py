from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from apps.teachers.models import Teachers
from apps.students.models import Students, Attendance
from . forms import AttendanceForm


def teachers(request):
    teacher=request.user
    teacherdetails = Teachers.objects.get(user=teacher)
    total_classes_assigned = teacherdetails.classes.all().count()
    teacher_name = Teachers.objects.get(user=teacher)
    Total_Students_Assigned = Students.objects.filter(assigned_teacher=teacher_name).count()
    context = {
        'teacherdetails': teacherdetails,
        'TotalStudentsAssigned':Total_Students_Assigned,
        'total_classes_assigned': total_classes_assigned,
        'total': "total",
    }

    return render(request,'teachers/teachersindex.html',context)

def profile(request):
    teacher=request.user
    query = Teachers.objects.filter(user=teacher).first()
    context = {
        'profile': query,
        'total': "total",
    }

    return render(request,'teachers/teacherprofile.html', context)

def attendance(request):
    form = AttendanceForm()
    teacher = request.user
    teacherdetails = Teachers.objects.get(user=teacher)
    total_classes_assigned = teacherdetails.classes.all().count()
    Total_Students_Assigned = Students.objects.filter(assigned_teacher=teacherdetails).count()
    Students_Assigned = Students.objects.filter(assigned_teacher=teacherdetails)
    # query=Attendance.student_name
    attendance = Attendance.objects.filter(student_name=Students_Assigned)

    context = {
        'teacherdetails': teacherdetails,
        'TotalStudentsAssigned': Total_Students_Assigned,
        'total_classes_assigned': total_classes_assigned,
        'total': "total",
        'form':form,
    }

    return render(request,'teachers/studentattendance.html', context)


