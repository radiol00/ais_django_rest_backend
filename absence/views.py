from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework import status
from rest_framework.parsers import JSONParser
from .models import Absence
from .serializers import AbsenceSerializer, UserAbsenceSerializer
from rest_framework.generics import ListAPIView
# Create your views here.


class AbsenceAPIView(viewsets.ModelViewSet):
    serializer_class = AbsenceSerializer
    queryset = Absence.objects.all()

    class isOwnerOrReject(permissions.BasePermission):
        def has_permission(self, request, view):
            pk = view.kwargs['pk']
            try:
                user_absence = Absence.objects.get(pk=pk)                
            except:
                return False

            if user_absence.user.id == request.user.id:
                return True
            return False


    # for normal user to get his absences, fetch get on /user/absence/
    def get_permissions(self):
        if self.action == 'list':
            permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
        else:
            permission_classes = [permissions.IsAuthenticated, self.isOwnerOrReject]
        return [permission() for permission in permission_classes]
    

    def create(self, request):
        serializer = AbsenceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            # print('added')
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class UserAbsences(ListAPIView):
    serializer_class = AbsenceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
        return Absence.objects.filter(user=user)

