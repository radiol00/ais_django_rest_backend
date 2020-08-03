from django.urls import path
from .views import AbsenceAPIView


urlpatterns = [
    path('', AbsenceAPIView.as_view())
]