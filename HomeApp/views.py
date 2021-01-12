from os import error, name
from django.core.checks.messages import Error
from django.db.models import query
from django.http.response import Http404
from django.shortcuts import render, HttpResponse
from . import models


def index(request):
    return render(request, 'HomeApp/index.html')


def register(request):
    return render(request, 'HomeApp/register.html')


def login(request):
    return render(request, 'HomeApp/login.html')


def reg_done(request):
    regobj = models.Register()

    name = request.POST.get('name')
    email = request.POST.get('email')
    phone = request.POST.get('phone')
    password = request.POST.get('password')
    repassword = request.POST.get('repassword')
    
    #-------------
    regobj.name = name
    regobj.email = email
    regobj.phone = phone
    regobj.password = password
    regobj.repassword = repassword
    regobj.save()

    return render(request, 'HomeApp/reg_done.html')

def login_done(request):
    logobj = models.Register()

    lemail = request.POST.get('lemail')
    lpassword = request.POST.get('lpassword')

    email = logobj.email
    password = logobj.password

    if lemail == email:
        return render(request, 'index.html')
    else:
        return Http404()
