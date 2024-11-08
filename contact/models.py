from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=255)
    gmail = models.EmailField(max_length=255)
    senha = models.CharField(max_length=255, validators=[MinLengthValidator(4)])
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self) -> str:
        return f'{self.nome}'