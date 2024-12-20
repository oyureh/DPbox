from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User


class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    gmail = models.EmailField(max_length=255, unique=True)
    senha = models.CharField(max_length=255, validators=[MinLengthValidator(4)])
    created_date = models.DateTimeField(default=timezone.now)

# esse def serve para retornar o nome dos cadastro no admin do django 
    def __str__(self) -> str:
        return f'{self.nome}'
    

