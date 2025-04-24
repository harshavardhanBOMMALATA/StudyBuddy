from django.shortcuts import render,redirect
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from .models import User
from .serializer import UserSerializer
from django.http import HttpResponse

def home(request):
    return render(request,'index1.html')
def softskills(request):
    return render(request,'softskills.html')
def softskillsadd(request):
    return render(request,'softskillsadd.html')
def technical(request):
    return render(request,'technical.html')
def technicaladd(request):
    return render(request,'technicaladd.html')
def register(request):
    return render(request,'register.html')
def login(request):
    return render(request,'login.html')

def creation(request):
    return render(request,'login.html')
def userlogin(request):
    return redirect('home')
def community(request):
    return render(request,'community.html')
def mentor(request):
    return render(request,'mentor.html')
def nontechnical(request):
    return render(request,'nontechnical.html')
def join(request):
    return render(request,'join.html')
def create(request):
    return render(request,'create.html')
def smartschedular(request):
    return render(request,'studyschedular.html')
def mycollege(request):
    return render(request,'mycollege.html')
def mygroup(request):
    return render(request,'mygroup.html')