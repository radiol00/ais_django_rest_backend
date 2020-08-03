from django.shortcuts import render
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from .serializers import CustomUserSerializer
from .models import CustomUser
# Create your views here.

class RegistrationAPIView(CreateAPIView):
    model = CustomUser
    serializer_class = CustomUserSerializer
    queryset = CustomUser.objects.all()
    def get(self, request):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)



    # def post(self, request):
    #     serializer = CustomUserSerializer(data=request.data)
    #     if serializer.is_valid():
    #         return Response(serializer.data, status=201)
    #     return Response(serializer.errors, status=400)
        