"""
URL configuration for jobposting project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LoginView
from django.urls import path, include

from post import views
from post.urls import url_patterns
from post.views import post_job, job_detail, custom_login, role_page, JobDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(url_patterns)),
    path('api/post-job/', post_job, name='post_job_api'),
    path('job/<int:job_id>/', job_detail, name='job_detail'),
    path('login/', custom_login, name='login'),
    path('role', role_page, name='role'),
    path('role/', views.role_page, name='role'),
    # path('api/jobs/<int:pk>/', JobDetailView.as_view(), name='job_detail_api')
    path('apply/<int:job_id>/', views.apply_for_job, name='apply_for_job'),

]

