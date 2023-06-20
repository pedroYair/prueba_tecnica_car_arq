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

    def update(self, teacher, validated_data):  # noqa
        with atomic():
            date_of_birth = validated_data.get("date_of_birth", teacher.date_of_birth)
            if relativedelta(datetime.now(), date_of_birth).years < 18:
                raise serializers.ValidationError(
                    "La fecha de nacimiento no corresponde a la de una persona mayor de edad"
                )

            teacher.document_number = validated_data.get("document_number", teacher.document_number)
            teacher.document_type = validated_data.get("document_type", teacher.document_type)
            teacher.first_name = validated_data.get("first_name", teacher.first_name)
            teacher.last_name = validated_data.get("last_name", teacher.last_name)
            teacher.date_of_birth = date_of_birth
            teacher.gender = validated_data.get("gender", teacher.gender)
            teacher.phone = validated_data.get("phone", teacher.phone)
            teacher.email = validated_data.get("email", teacher.email)
            teacher.address = validated_data.get("address", teacher.address)
            teacher.save()
            return teacher

