from datetime import datetime

from dateutil.relativedelta import relativedelta
from rest_framework import serializers
from teachers.models import Teacher
from django.db.transaction import atomic


class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Teacher
        fields = ['id',
                  'document_number',
                  'document_type',
                  'first_name',
                  'last_name',
                  'date_of_birth',
                  'gender',
                  'phone',
                  'email',
                  'address']

    def create(self, validated_data):
        with atomic():
            if relativedelta(datetime.now(), validated_data["date_of_birth"]).years < 18:
                raise serializers.ValidationError(
                    "La fecha de nacimiento no corresponde a la de una persona mayor de edad"
                )

            return Teacher.objects.create(**validated_data)

