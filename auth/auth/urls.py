from django.urls import path, include
from core.Swagger import sw

docs_url = [
    path('docs/', sw.with_ui('swagger', cache_timeout=0)),
    path('docs/v2/', sw.with_ui('redoc', cache_timeout=0)),
]

apps_url = [
    path('api/v1/authorized-apps/', include('apps.authorized_apps.urls')),
    path('api/v1/users/', include('apps.users.urls')),


]

urlpatterns = apps_url + docs_url
