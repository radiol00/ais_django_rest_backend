from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegistrationAPIView


urlpatterns = [
    path('', TokenObtainPairView.as_view()),
    path('refresh/', TokenRefreshView.as_view()),
    path('register/', RegistrationAPIView.as_view())
]