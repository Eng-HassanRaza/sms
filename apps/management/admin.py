from django.contrib import admin
from . models import Class

from apps.management.models import School, Admins, Class

admin.site.register(School)
admin.site.register(Admins)
admin.site.register(Class)
# Register your models here.

admin.site.register(Class)