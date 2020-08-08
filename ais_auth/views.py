from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import AISTokenObtainPairSerializer
# Create your views here.

class RegistrationAPIView(CreateAPIView):
    permission_classes = []
    model = CustomUser
    serializer_class = CustomUserSerializer

class UserViewSet(ModelViewSet):
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    # permission_classes = []
    queryset = CustomUser.objects.all()
    serializer_class = CustomUserSerializer


class AISTokenObtainPairView(TokenObtainPairView):
    serializer_class = AISTokenObtainPairSerializer;

        