from django.urls import path
from teachers.api import views

app_name = "teacher_api"

urlpatterns = [
    path('v1/teachers_list/', views.ListTeachersAPIView.as_view(), name='teachers_list'),
    path('v1/teachers_create/', views.CreateTeacherAPIView.as_view(), name='teachers_create'),
    path('v1/teachers_update/<int:pk>/', views.UpdateTeacherAPIView.as_view(), name='teachers_update'),
    path('v1/teachers_delete/<int:pk>/', views.DeleteTeacherAPIView.as_view(), name='teachers_delete'),
]
