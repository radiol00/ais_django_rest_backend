from rest_framework import serializers
from .models import Absence

class AbsenceSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Absence
        fields = '__all__'