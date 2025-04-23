from django.contrib import admin
from django.urls import path, include

from Users import views

urlpatterns = [
    path('register/', views.Register.as_view()),
]
