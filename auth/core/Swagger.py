from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions


sw = get_schema_view(
    openapi.Info(
        title="API Authenticator",
        default_version='v1.0',
        description="Documentation API",
        contact=openapi.Contact(email="apuig0502@gmail.com"),
        license=openapi.License(name="OpenSource"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
