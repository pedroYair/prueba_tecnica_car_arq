from django.db import models


class BaseModel(models.Model):
    class Status(models.IntegerChoices):
        ACTIVE = 1, "Activo"
        INACTIVE = 2, "Inactivo"

    status = models.PositiveSmallIntegerField(
        "Estado", choices=Status.choices, default=Status.ACTIVE
    )
    date_created = models.DateTimeField("Fecha Creación", auto_now_add=True)
    date_updated = models.DateTimeField("Fecha Actualizado", auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
