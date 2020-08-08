from django.urls import path, include
from .views import AbsenceAPIView
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('', AbsenceAPIView, basename='absence')

urlpatterns = [
    path('', include(router.urls))
]