from django.contrib import admin
from django.urls import path, include

from Users import views

app_name = 'Users'

urlpatterns = [
    path('register/', views.Register.as_view(), name='Register'),
    path('login/', views.Login.as_view(), name='Login')
]
