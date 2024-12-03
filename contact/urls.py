from django.urls import path
from contact import views

urlpatterns = [
   path('', views.index, name='index'),
   path('login/', views.login, name='login'),
   path('quemsomos/', views.quemsomos, name='quemsomos'),
   path('usuarios/', views.usuarios, name='usuarios'),
    path('search/', views.search, name='search'),
]