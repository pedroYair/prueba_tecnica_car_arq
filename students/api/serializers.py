from datetime import datetime

from dateutil.relativedelta import relativedelta
from rest_framework import serializers
from students.models import Student
from django.db.transaction import atomic


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id',
                  'document_number',
                  'document_type',
                  'first_name',
                  'last_name',
                  'date_of_birth',
                  'gender',
                  'phone']

    def create(self, validated_data):
        with atomic():
            if relativedelta(datetime.now(), validated_data["date_of_birth"]).years < 15:
                raise serializers.ValidationError(
                    "La fecha de nacimiento no es valida para un estudiante"
                )
            return Student.objects.create(**validated_data)

    def update(self, student, validated_data):  # noqa
        with atomic():
            date_of_birth = validated_data.get("date_of_birth", student.date_of_birth)
            if relativedelta(datetime.now(), date_of_birth).years < 15:
                raise serializers.ValidationError(
                    "La fecha de nacimiento no es valida para un estudiante"
                )

            student.document_number = validated_data.get("document_number", student.document_number)
            student.document_type = validated_data.get("document_type", student.document_type)
            student.first_name = validated_data.get("first_name", student.first_name)
            student.last_name = validated_data.get("last_name", student.last_name)
            student.date_of_birth = date_of_birth
            student.gender = validated_data.get("gender", student.gender)
            student.phone = validated_data.get("phone", student.phone)
            student.save()
            return student
