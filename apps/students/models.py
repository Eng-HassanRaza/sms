from django.db import models
from apps.management.models import School, Class
from apps.teachers.models import Teachers
from apps.authentication.models import User

# Create your models here.


class Students(models.Model):
    MALE = 'M'
    FEMALE = 'F'
    GENDER_CHOICES = [
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    first_name = models.CharField(max_length=20, null=True)
    last_name = models.CharField(max_length=20, null=True)
    father_name = models.CharField(max_length=20, null=True)
    class_number = models.ForeignKey(Class, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    father_phone_number = models.CharField(max_length=255, null=True, blank=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    date_of_birth = models.DateField()
    address = models.CharField(max_length=255, null=True, blank=True)
    date_of_enrollement = models.DateField()
    date = models.DateTimeField(auto_now=True)
    assigned_teacher = models.ForeignKey(Teachers, on_delete=models.PROTECT)

    def __str__(self):
        return self.first_name


class Attendance(models.Model):
    PRESENT = 'P'
    ABSENT = 'A'
    LEAVE = 'L'
    ATTENDANCE_CHOICES = [
        (PRESENT, 'Present'),
        (ABSENT, 'Absent'),
        (LEAVE, 'Leave')
    ]
    student_name = models.ForeignKey(Students, on_delete=models.CASCADE)
    attandance = models.CharField(max_length=10, choices=ATTENDANCE_CHOICES)
    date = models.DateTimeField(auto_now=True)




