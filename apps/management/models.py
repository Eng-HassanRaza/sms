from django.db import models

# Create your models here.


class School(models.Model):
    name = models.CharField(max_length=255, null= True)
    school_email = models.EmailField(max_length=255, null=True, blank=True)
    school_phone_number= models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    website= models.URLField(null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.first_name


class Admins(models.Model):

    first_name = models.CharField(max_length=255, null= True)
    last_name = models.CharField(max_length=255, null=True)
    email = models.EmailField(max_length=255, null=True, blank=True)
    phone_number = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=255, null=True, blank=True)
    date = models.DateTimeField(auto_now=True)

    def __init__(self):
        return self.first_name


class Class(models.Model):
    class_name = models.CharField(max_length=255)
    subjects = models.CharField(max_length=255)


