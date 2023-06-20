from rest_framework import serializers
from subjects.models import Subject
from teachers.api.serializers import TeacherSummarySerializer
from students.api.serializers import StudentSummarySerializer
from django.db.transaction import atomic


class SubjectSerializer(serializers.ModelSerializer):
    teacher = TeacherSummarySerializer(many=False)
    students = StudentSummarySerializer(many=True)

    class Meta:
        model = Subject
        fields = ['id',
                  'code',
                  'name',
                  'teacher',
                  'students',
                  ]


class SubjectCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Subject
        fields = ['id',
                  'code',
                  'name',
                  'teacher',
                  'students',
                  ]
