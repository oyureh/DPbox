from django.urls import path
from contact import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('', views.index, name='index'),
   path('login/', views.login, name='login'),
   path('quemsomos/', views.quemsomos, name='quemsomos'),
   path('usuarios/', views.usuarios, name='usuarios'),
   path('cadastro/', views.cadastro, name='cadastro'),
   path('login/telasMaiores/', views.login_telasMaiores, name='login_telasMaiores'),
   path('login/mobile/', views.login_mobile, name='login_mobile'),
   path('password-reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
   path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password-reset-done'),
   path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password-reset-confirm'),
   path('password/done/', auth_views.PasswordResetCompleteView.as_view(), name='password-reset-complete')
]