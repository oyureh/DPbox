# Generated by Django 5.1.2 on 2025-01-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_remove_usuarios_category_remove_usuarios_owner_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='is_admin',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='last_login',
            field=models.DateTimeField(blank=True, null=True, verbose_name='last login'),
        ),
        migrations.AddField(
            model_name='usuarios',
            name='password',
            field=models.CharField(default='password123', max_length=128, verbose_name='password'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='usuarios',
            name='senha',
            field=models.CharField(max_length=255),
        ),
    ]