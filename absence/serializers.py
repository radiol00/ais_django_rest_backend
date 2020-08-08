from rest_framework import serializers
from .models import Absence

class AbsenceSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(slug_field='email', read_only=True)
    class Meta:
        model = Absence
        fields = '__all__'


class UserAbsenceSerializer(serializers.Serializer):
    class Meta:
        fields = '__all__'

