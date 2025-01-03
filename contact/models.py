from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils import timezone

class UsuariosManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Cria e retorna um usuário com email e senha.
        """
        if not email:
            raise ValueError('O email é obrigatório')
        email = self.normalize_email(email)
        user = self.model(gmail=email, **extra_fields)
        user.set_password(password)  
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_admin', True)
        return self.create_user(email, password, **extra_fields)


class Usuarios(AbstractBaseUser):
    # Definindo os campos do modelo
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    gmail = models.EmailField(max_length=255, unique=True)  
    senha = models.CharField(max_length=255)  # Campo de senha (será criptografada)
    created_date = models.DateTimeField(default=timezone.now)  
    is_active = models.BooleanField(default=True)  
    is_admin = models.BooleanField(default=False) 

    USERNAME_FIELD = 'gmail'  
    REQUIRED_FIELDS = ['nome']  

    objects = UsuariosManager() 

    def __str__(self):
        return self.nome


