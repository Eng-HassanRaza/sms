# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.forms import ModelForm
from apps.students.models import Students, Attendance


class AttendanceForm(ModelForm):
    class Meta:
        model = Attendance
        fields = '__all__'
    # name = forms.CharField(
    #     widget=forms.TextInput(
    #         attrs={
    #             "placeholder": "Username",
    #             "class": "form-control"
    #         }
    #     ))
    # email = forms.EmailField(
    #     widget=forms.EmailInput(
    #         attrs={
    #             "placeholder": "Email",
    #             "class": "form-control"
    #         }
    #     ))
    # password1 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Password",
    #             "class": "form-control"
    #         }
    #     ))
    # password2 = forms.CharField(
    #     widget=forms.PasswordInput(
    #         attrs={
    #             "placeholder": "Password check",
    #             "class": "form-control"
    #         }
    #     ))
