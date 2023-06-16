from django.contrib import admin
from teachers.models import Teacher


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):

    list_display = ('id', 'document_number', 'first_name', 'last_name', 'gender', 'phone', 'email', 'status',)
    ordering = ('id',)
