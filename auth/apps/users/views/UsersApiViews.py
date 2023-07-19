import requests_toolbelt.utils.dump
from rest_framework import permissions, viewsets, status
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.serializers import TokenVerifySerializer
from rest_framework_simplejwt.views import TokenObtainPairView, TokenVerifyView

from apps.users.models import Users
from apps.users.serializers.TokenSerializers import TokenSerializer
from apps.users.serializers.UsersSerializers import UserListSerializer, UserCreateUpdateSerializer


class UsersViews(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAdminUser, ]
    serializer_class = UserListSerializer
    queryset = Users.objects.all()

    def get_serializer_class(self):
        if self.action in ['list', 'retrieve']:
            return self.serializer_class
        return UserCreateUpdateSerializer


class LoginView(TokenObtainPairView):
    serializer_class = TokenSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            return Response({
                'message': "Login Error",
                'data': e.args[0]
            }, 401)
        return Response({
            'message': "Success Login",
            'data': serializer.validated_data
        })


class MyTokenObtainPairView(TokenVerifyView):
    serializer_class = TokenVerifySerializer

    def post(self, request, *args, **kwargs):

        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        utils = JWTAuthentication()
        token = utils.get_validated_token(request.data.get("token"))

        user = utils.get_user(token)

        return Response(user.json(), status=status.HTTP_200_OK)
