from django.utils.deprecation import MiddlewareMixin
from django.conf import settings
from django.core.exceptions import PermissionDenied
from apps.authorized_apps.models import AuthorizedApps


class AppMiddleware(MiddlewareMixin):
    authorized_apps = AuthorizedApps.objects.filter(is_active=True)

    def process_view(self, request, view_func, view_args, view_kwargs):
        host = request.get_host()
        app_id = request.META.get("HTTP_UUID")
        free = view_kwargs.get("no_header", False)
        is_free_url = request.path in ["/media/", "/swagger/"]
        app = self.authorized_apps.filter(identification=app_id).first() or False
        if app is not None or free or is_free_url or host in settings.AUTHORIZED_HOSTS:
            return
        else:
            raise PermissionDenied
