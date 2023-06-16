from django.db import models

from base.models import BaseModel


class Subject(BaseModel):
    code = models.CharField(max_length=150, verbose_name="Área", unique=True)
    name = models.CharField(max_length=300, verbose_name="Nombre")

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
