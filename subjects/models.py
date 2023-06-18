from django.db import models

from base.models import BaseModel
from teachers.models import Teacher
from students.models import Student


class Subject(BaseModel):
    code = models.CharField(max_length=150, verbose_name="Área", unique=True)
    name = models.CharField(max_length=300, verbose_name="Nombre")
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.PROTECT,
        verbose_name="Profesor",
        related_name="teacher_subject",
        null=True,
        blank=True
    )
    students = models.ManyToManyField(
        Student, related_name="students_subject", verbose_name="Estudiantes", blank=True
    )

    def __str__(self):
        return f"{self.code} - {self.name}"

    class Meta:
        verbose_name = "Curso"
        verbose_name_plural = "Cursos"
