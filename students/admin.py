from django.contrib import admin
from students.models import Student

admin.site.site_header = "PRUEBA TECNICA"
admin.site.site_title = "PRUEBA TECNICA"
admin.site.index_title = "PRUEBA TECNICA"


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = ('id', 'document_number', 'first_name', 'last_name', 'date_of_birth', 'gender', 'phone', 'status',)
    ordering = ('id',)
