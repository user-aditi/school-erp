"""
URL configuration for erp_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin

from django.urls import path
from students.views import student_list, attendance_list, StudentListAPI, AttendanceCreateAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', student_list, name='student_list'),
    path('attendance/', attendance_list, name='attendance_list'),
    path('api/students/', StudentListAPI.as_view(), name='student_list_api'),
    path('api/attendance/', AttendanceCreateAPI.as_view(), name='attendance_create_api'),
]

