from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.parents, name="parents"),
]