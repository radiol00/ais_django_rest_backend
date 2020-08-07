from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import CustomUserSerializer
from .models import CustomUser
from rest_framework_simplejwt.views import TokenObtainPairView
from .serializers import AISTokenObtainPairSerializer
# Create your views here.

class RegistrationAPIView(CreateAPIView):
    permission_classes = []
    model = CustomUser
    serializer_class = CustomUserSerializer
    
    def post(request):
        print(request);



class AISTokenObtainPairView(TokenObtainPairView):
    serializer_class = AISTokenObtainPairSerializer;

        