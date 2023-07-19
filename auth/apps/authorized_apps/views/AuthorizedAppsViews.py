from rest_framework import viewsets, permissions
from apps.authorized_apps.serializers.AuthorizedAppsSerializer import AuthorizedAppsSerializer
from apps.authorized_apps.models import AuthorizedApps


class AuthorizedAppsViews(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, ]
    serializer_class = AuthorizedAppsSerializer
    queryset = AuthorizedApps.objects.all()
