from django.urls import path
from rest_framework.routers import DefaultRouter
from apps.users.views import UsersApiViews

router = DefaultRouter()
router.register('', UsersApiViews.UsersViews)

urlpatterns = [
                  path('login/', UsersApiViews.LoginView.as_view()),
                  path('verify/', UsersApiViews.MyTokenObtainPairView.as_view(), {"no_headers": True}),
              ] + router.urls
