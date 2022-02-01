# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path
from .views import login_view, register_user
from django.contrib.auth.views import LogoutView
from .views import StudentSignUpView, TeacherSignUpView, ParentSignUpView
from .. import students

urlpatterns = [
    path('login/', login_view, name="login"),
    path('register/', register_user, name="register"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('studentsignup/', StudentSignUpView.as_view(), name='student_signup'),
    path('teachersignup/', TeacherSignUpView.as_view(), name='teacher_signup'),
    path('parentsignup/', ParentSignUpView.as_view(), name='parent_signup'),
    # path('ownersignup/', OwnerSignUpView.as_view(), name='teacher_signup'),
    # path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]
