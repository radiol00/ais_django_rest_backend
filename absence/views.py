from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from .models import Absence
from .serializers import AbsenceSerializer
# Create your views here.


class AbsenceAPIView(APIView):
    # pass
    # authentication_classes = [authentication.TokenAuthentication]
    # permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        absences = Absence.objects.all()
        serializer = AbsenceSerializer(absences, many=True)
        return Response(serializer.data)
