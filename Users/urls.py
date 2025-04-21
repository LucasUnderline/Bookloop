from django.contrib import admin, include
from django.urls import path

from Users import views

urlpatterns = [
    path('register/', views.view_register),
]
