"""
URL configuration for studybuddy project.

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
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('softskills/',views.softskills,name='softskills'),
    path('softskillsadd',views.softskillsadd,name='softskillsadd'),
    path('technical/',views.technical,name='technical'),
    path('technicaladd',views.technicaladd,name='technicaladd'),
    path('register/',views.register,name='register'),
    path('login/',views.login,name='login'),
    path('creation/',views.creation,name='creation'),
    path('userlogin/',views.userlogin,name='userlogin'),
    path('community/',views.community,name='community'),
    path('mentor/',views.mentor,name='mentor'),
    path('nontechnical/',views.nontechnical,name='nontechnical'),
    path('join/',views.join,name='join'),
    path('create/',views.create,name='create'),
    path('smartschedular/',views.smartschedular,name='smartschedular'),
    path('mycollge/',views.mycollege,name='mycollege'),
    path('mygroup/',views.mygroup,name='mygroup'),
    ]
