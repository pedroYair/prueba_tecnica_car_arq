from django.urls import path
from subjects.api import views

app_name = "subject_api"

urlpatterns = [
    path('v1/subjects_list/', views.ListSubjectsAPIView.as_view(), name='subjects_list'),
    path('v1/subjects_create/', views.CreateSubjectAPIView.as_view(), name='subjects_create'),
    path('v1/subjects_update/<int:pk>/', views.UpdateSubjectAPIView.as_view(), name='subjects_update'),
    path('v1/subjects_delete/<int:pk>/', views.DeleteSubjectAPIView.as_view(), name='subjects_delete'),
]
