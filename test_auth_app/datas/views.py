from rest_framework import viewsets
from rest_framework.response import Response
from core import Permissions


class TestView(viewsets.ViewSet):
    permission_classes = [Permissions.MSIsAdmin, ]

    def test_view(self, request):
        return Response({
            'message':'Success Login',
            'user': self.request.user,
            
        })
