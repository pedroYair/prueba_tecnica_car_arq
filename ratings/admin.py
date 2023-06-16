from django.contrib import admin
from ratings.models import Rating


@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):

    list_display = ('id', 'activity', 'student', 'subject', 'teacher', 'rating_number', 'date_created')
    ordering = ('id',)
