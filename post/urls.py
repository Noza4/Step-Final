from django.urls import path
from . import views

url_patterns = [
    path('', views.register, name='register'),
    path('dashboard', views.dashboard, name='dashboard'),
]
