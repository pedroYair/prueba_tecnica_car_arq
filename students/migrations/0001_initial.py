# Generated by Django 3.2 on 2023-06-16 02:54

from django.db import migrations, models
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'Inactivo')], default=1, verbose_name='Estado')),
                ('date_created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha Creación')),
                ('date_updated', models.DateTimeField(auto_now=True, null=True, verbose_name='Fecha Actualizado')),
                ('uuid', models.UUIDField(db_index=True, default=uuid.uuid4, editable=False, unique=True, verbose_name='UUID')),
                ('document_number', models.CharField(db_index=True, max_length=50, unique=True, verbose_name='Número de documento')),
                ('document_type', models.CharField(choices=[('TI', 'Tarjeta de identidad'), ('CC', 'Cédula de ciudadania')], max_length=10, verbose_name='Tipo de documento')),
                ('first_name', models.CharField(max_length=50, verbose_name='Nombres')),
                ('last_name', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('date_of_birth', models.DateField(blank=True, null=True, verbose_name='Fecha de nacimiento')),
                ('gender', models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=10, verbose_name='Género')),
                ('phone', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Teléfono')),
            ],
            options={
                'verbose_name': 'Estudiante',
                'verbose_name_plural': 'Estudiantes',
            },
        ),
    ]
