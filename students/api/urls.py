from django.urls import path
from students.api import views

app_name = "student_api"

urlpatterns = [
    path('v1/students_list/', views.ListStudentsAPIView.as_view(), name='students_list'),
    path('v1/students_create/', views.CreateStudentAPIView.as_view(), name='students_create'),
    path('v1/students_update/<int:pk>/', views.UpdateStudentAPIView.as_view(), name='students_update'),
    path('v1/students_delete/<int:pk>/', views.DeleteStudentAPIView.as_view(), name='students_delete'),
]
