from django.urls import path
from rest_framework_simplejwt import views as jwt_views

app_name = "base_api"

urlpatterns = [
    path('v1/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token_refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
