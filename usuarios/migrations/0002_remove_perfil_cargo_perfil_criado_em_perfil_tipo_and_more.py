# Generated by Django 5.2 on 2025-04-18 00:29

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='cargo',
        ),
        migrations.AddField(
            model_name='perfil',
            name='criado_em',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2025, 4, 17, 21, 28, 59, 79205)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='perfil',
            name='tipo',
            field=models.CharField(choices=[('admin', 'Administrador'), ('medico', 'Médico'), ('recepcionista', 'Recepcionista'), ('paciente', 'Paciente')], default=datetime.datetime(2025, 4, 17, 21, 29, 21, 474539), max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='perfil',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
