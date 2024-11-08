from django.contrib import admin
from contact import models

@admin.register(models.Usuarios)
class UsuariosAdmin(admin.ModelAdmin):
    list_display = 'id_usuario','nome', 'gmail', 'created_date',
    ordering = '-id_usuario',
    list_filter = 'created_date',
    search_fields = 'id_usuario','nome', 'gmail', 'created_date',
    list_per_page = 100 