from django.urls import include, path
from rest_framework import routers

from .views import VenueViewSet

router = routers.DefaultRouter()
router.register(
    r"",
    VenueViewSet,
    basename="sport",
)
urlpatterns = [path("", include(router.urls))]
