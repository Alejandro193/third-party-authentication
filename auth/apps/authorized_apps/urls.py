from django.urls import include, path
from rest_framework import routers
from apps.authorized_apps.views.AuthorizedAppsViews import AuthorizedAppsViews

router = routers.DefaultRouter()
router.register('', AuthorizedAppsViews)

urlpatterns = router.urls
