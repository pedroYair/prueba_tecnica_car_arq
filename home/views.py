from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import Student
from teachers.models import Teacher
from subjects.models import Subject
from ratings.models import Rating


@login_required
def home(request):

    students = Student.objects.all().count()
    teachers = Teacher.objects.all().count()
    subjects = Subject.objects.all().count()
    ratings = Rating.objects.all().count()

    context = {'count_students': students,
               'count_teachers': teachers,
               'count_subjects': subjects,
               'count_ratings': ratings,
               }

    return render(request, 'home/index.html', context)
