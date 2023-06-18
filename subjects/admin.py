from django.contrib import admin
from subjects.models import Subject


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):

    list_display = ('id', 'code', 'name', 'teacher')
    ordering = ('id',)
