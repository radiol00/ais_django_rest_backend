from .models import CustomUser
from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()


class CustomUserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = CustomUser.objects.create(
            email=validated_data['email']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user

    class Meta:
        model = User
        fields = ['email', 'password']