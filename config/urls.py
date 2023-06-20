"""prueba_tecnica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('home.urls', namespace="home")),
    path('base/', include('base.urls', namespace="base")),
    path('base_api/', include('base.api.urls', namespace="base_api")),
    path('subjects/', include('subjects.urls', namespace="subjects")),
    path('teacher_api/', include('teachers.api.urls', namespace="teacher_api")),
    path('student_api/', include('students.api.urls', namespace="student_api")),
    path('subject_api/', include('subjects.api.urls', namespace="subject_api")),
    path('rating_api/', include('ratings.api.urls', namespace="rating_api")),
    path('', RedirectView.as_view(url='/home/')),
    path('accounts/', include('registration.backends.default.urls'))
]
