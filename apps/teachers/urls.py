from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.teachers , name='teachers'),
    path('profile', views.profile , name='teacherprofile'),
    path('attendance',views.attendance, name='attendance'),
]