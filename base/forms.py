import os

from django import forms
from django.core.exceptions import ValidationError
from base import constants


class LoadDataForm(forms.Form):
    actions = (
        (constants.LOAD, "Importar datos"),
        (constants.GET_FORMAT, "Descargar formato de importación"),
    )
    object_types = (
        (constants.TEACHERS, "Profesores"),
        (constants.STUDENTS, "Estudiantes"),
        (constants.RATINGS, "Calificaciones")
    )
    type_action = forms.ChoiceField(label="Acción", widget=forms.Select, choices=actions)
    object_type = forms.ChoiceField(required=True, label="Tipo de objeto a importar", widget=forms.Select, choices=object_types)
    file = forms.FileField(required=False, label="Archivo")

    def clean_file(self):
        file = self.cleaned_data['file']
        type_action = self.cleaned_data['type_action']

        if type_action == constants.LOAD and not file:
            raise ValidationError('Adjunte el archivo con los datos', code="invalid")

        if file:
            ext = os.path.splitext(file.name)[1]  # [0] returns path+filename
            ext = ext.lower()
            valid_extensions = ['.csv', '.xlsx', '.xls']
            if ext not in valid_extensions:
                raise ValidationError('Tipo de archivo invàlido, adjunte csv, xlsx o xls', code="invalid")
            else:
                return file
        else:
            return file
