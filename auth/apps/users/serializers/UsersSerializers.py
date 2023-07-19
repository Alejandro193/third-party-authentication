from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from apps.users.models import Users


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ['password']


class UserCreateUpdateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(required=False, write_only=True)

    @staticmethod
    def validate_password(value):
        return make_password(value)

    class Meta:
        model = Users
        fields = ('username', 'password', 'is_superuser', 'is_staff', 'email')
