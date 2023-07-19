from rest_framework import serializers
from apps.authorized_apps.models import AuthorizedApps


class AuthorizedAppsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthorizedApps
        fields = '__all__'
