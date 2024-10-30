from django.urls import path
from .views import index

urlpatterns = [
   path('index/', index, name='home')
# path('login/', views.usuarios, name='listagem_usuarios'),
]