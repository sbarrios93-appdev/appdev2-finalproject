from django.urls import include, path
from rest_framework import routers

from pitzio_api.sports.views import SportViewSet

router = routers.DefaultRouter()
router.register(
    r"",
    SportViewSet,
    basename="sport",
)
urlpatterns = [path("", include(router.urls))]
