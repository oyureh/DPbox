# Generated by Django 5.1.2 on 2024-12-02 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_category_usuarios_owner_alter_usuarios_nome_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuarios',
            name='category',
        ),
        migrations.RemoveField(
            model_name='usuarios',
            name='owner',
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='gmail',
            field=models.EmailField(max_length=255, unique=True),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
