from django.urls import path
from .views import *

app_name = 'subject'

urlpatterns = [
    path('import_subjects', import_subjects, name="import_subject"),
    path('list_subjects', list_subjects, name="list_subjects"),
]
