from django.urls import include, path

from rest_framework.routers import DefaultRouter

from api.views import CustomUserViewSet

router = DefaultRouter()
router.register("users", CustomUserViewSet, basename="users")

urlpatterns = [
    path("auth/", include("djoser.urls.authtoken")),
    path("", include("djoser.urls")),
    path("", include(router.urls)),
]
