from django.db import models

from base.models import BaseModel
from students.models import Student
from teachers.models import Teacher
from subjects.models import Subject
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import CheckConstraint, Q


class Rating(BaseModel):
    class ActivityType(models.TextChoices):
        TEST = "EXAMEN", "Examen"
        EXPOSITION = "EXPOSICION", "Exposición"
        READING = "LECTURA", "Lectura"
        PARTICIPATION = "PARTICIPACION_CLASE", "Participación en Clase"
        TASK = "TAREA", "Tarea"

    activity = models.CharField(verbose_name="Tipo de actividad", max_length=100, choices=ActivityType.choices)
    student = models.ForeignKey(
        Student,
        on_delete=models.PROTECT,
        verbose_name="Estudiante",
        related_name="student_activity_rating",
    )
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.PROTECT,
        verbose_name="Profesor",
        related_name="teacher_activity_rating",
    )
    subject = models.ForeignKey(
        Subject,
        on_delete=models.PROTECT,
        verbose_name="Asignatura",
        related_name="subject_activity_rating",
    )
    rating_number = models.FloatField(
        verbose_name="Calificación numérica",
        validators=[MinValueValidator(0.0), MaxValueValidator(10.0)]
    )
    observations = models.TextField(verbose_name="Observaciones", null=True, blank=True)

    def __str__(self):
        return f"{self.student} - {self.rating_number}"

    class Meta:
        verbose_name = "Calificación"
        verbose_name_plural = "Calificaciones"
        constraints = (
            # for checking in the DB
            CheckConstraint(
                check=Q(rating_number__gte=0.0) & Q(rating_number__lte=10.0),
                name='rating_number_range'),
        )
