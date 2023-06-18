from django.urls import path
from .views import *

app_name = 'base'

urlpatterns = [
    path('massive_import', import_massive_data, name="import_massive_data"),
]
