from django.urls import path
from ratings.api import views

app_name = "rating_api"

urlpatterns = [
    path('v1/ratings_list/', views.ListRatingsAPIView.as_view(), name='ratings_list'),
    path('v1/ratings_create/', views.CreateRatingAPIView.as_view(), name='ratings_create'),
    path('v1/ratings_update/<int:pk>/', views.UpdateRatingAPIView.as_view(), name='ratings_update'),
    path('v1/ratings_delete/<int:pk>/', views.DeleteRatingAPIView.as_view(), name='ratings_delete'),
]
