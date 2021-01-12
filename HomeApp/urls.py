from os import name
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name= 'login'),
    path('register/', views.register, name='register'),
    path('register/reg_done', views.reg_done, name = 'reg_done'),
    path('login/login_done', views.login_done, name='log_done'),
]