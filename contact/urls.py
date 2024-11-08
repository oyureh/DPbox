from django.urls import path
from contact import views

urlpatterns = [
   path('', views.index, name='index'),
   path('', views.login, name='login'),
   path('', views.Quem_somos, name='Quem-somos')
]