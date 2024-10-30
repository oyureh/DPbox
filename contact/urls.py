
from django.contrib import admin
from django.urls import path
from contact import views
from project import templates

app_name = 'contact'

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.usuarios, name='listagem_usuarios'),
]