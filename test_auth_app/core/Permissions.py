from rest_framework.permissions import BasePermission
from core.Helpers import verify


class MSIsAdmin(BasePermission):

    def has_permission(self, request, view):
        is_verify = verify(request.META)
        if not is_verify:
            return False

        request.user = is_verify
        
        if request.user['is_superuser']:
            return True
        return False


class MSAllowAny(BasePermission):

    def has_permission(self, request, view):
        user = verify(request.META)
        if user:
            request.user = user
            return True
        request.user = None
        return True


class MSIsAuthenticated(BasePermission):

    def has_permission(self, request, view):
        is_verify = verify(request.META)
        if not is_verify:
            return False
        request.user = is_verify
        return True
