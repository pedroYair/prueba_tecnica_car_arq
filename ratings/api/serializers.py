from rest_framework import serializers
from ratings.models import Rating
from teachers.api.serializers import TeacherSummarySerializer
from students.api.serializers import StudentSummarySerializer
from subjects.api.serializers import SubjectSummarySerializer
from django.db.transaction import atomic


class RatingSerializer(serializers.ModelSerializer):
    teacher = TeacherSummarySerializer(many=False)
    student = StudentSummarySerializer(many=False)
    subject = SubjectSummarySerializer(many=False)

    class Meta:
        model = Rating
        fields = ['id',
                  'activity',
                  'student',
                  'teacher',
                  'subject',
                  'rating_number',
                  'observations',
                  ]


class RatingCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rating
        fields = ['id',
                  'activity',
                  'student',
                  'teacher',
                  'subject',
                  'rating_number',
                  'observations',
                  ]

    def create(self, validated_data):
        with atomic():
            teacher = validated_data["teacher"]
            subject = validated_data["subject"]
            student = validated_data["student"]
            if teacher != subject.teacher:
                raise serializers.ValidationError(
                    "El profesor ingresado no corresponde al que imparte la asignatura"
                )

            if student not in subject.students.all():
                raise serializers.ValidationError(
                    "El estudiante no esta matriculado en el curso ingresado"
                )

            return Rating.objects.create(**validated_data)

    def update(self, rating, validated_data):  # noqa
        with atomic():
            teacher = validated_data.get("teacher", rating.teacher)
            subject = validated_data.get("subject", rating.subject)
            student = validated_data.get("student", rating.student)
            if teacher != subject.teacher:
                raise serializers.ValidationError(
                    "El profesor ingresado no corresponde al que imparte la asignatura"
                )

            if student not in subject.students.all():
                raise serializers.ValidationError(
                    "El estudiante no esta matriculado en el curso ingresado"
                )

            rating.activity = validated_data.get("activity", rating.activity)
            rating.student = student
            rating.teacher = teacher
            rating.subject = subject
            rating.rating_number = validated_data.get("rating_number", rating.rating_number)
            rating.observations = validated_data.get("observations", rating.observations)
            rating.save()
            return rating
