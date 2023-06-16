from django.db import models
import uuid

from base.models import BaseModel
from phonenumber_field.modelfields import PhoneNumberField


class Teacher(BaseModel):
    class DocumentType(models.TextChoices):
        CC = "CC", "Cédula de ciudadania"
        CE = "CE", "Cédula de Extranjeria"

    class GenderType(models.TextChoices):
        MALE = "M", "Masculino"
        FEMALE = "F", "Femenino"

    uuid = models.UUIDField("UUID", unique=True, default=uuid.uuid4, editable=False, db_index=True)
    document_number = models.CharField(verbose_name="Número de documento", max_length=50, db_index=True, unique=True)
    document_type = models.CharField(verbose_name="Tipo de documento", max_length=10, choices=DocumentType.choices)
    first_name = models.CharField(max_length=50, verbose_name="Nombres")
    last_name = models.CharField(max_length=50, verbose_name="Apellidos")
    date_of_birth = models.DateField("Fecha de nacimiento", null=True, blank=True)
    gender = models.CharField(verbose_name="Género", max_length=10, choices=GenderType.choices)
    phone = PhoneNumberField(verbose_name="Teléfono")
    email = models.EmailField(verbose_name="Email", max_length=250)
    address = models.CharField(verbose_name="Dirección", max_length=250, null=True, blank=True)

    # RECORDAR ACTUALIZAR EL ARCHIVO DE REQUERIMIENTOS

    class Meta:
        verbose_name = "Profesor"
        verbose_name_plural = "Profesores"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
