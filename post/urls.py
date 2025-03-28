from django.urls import path
from . import views

url_patterns = [
    path('', views.register, name='register'),
    path('role', views.role_page, name='role'),
    path('dashboard', views.dashboard, name='dashboard')
]
