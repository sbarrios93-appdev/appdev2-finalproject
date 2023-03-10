from django.urls import path
from rest_framework import routers

from .views import GameViewSet, TeamViewSet

router = routers.DefaultRouter()
urlpatterns = [
    path("", GameViewSet.as_view({"get": "list"}), name="games"),
    path(
        "teams",
        TeamViewSet.as_view({"get": "list"}),
        name="teams",
    ),
    path(
        "teams/<str:pk>",
        TeamViewSet.as_view({"put": "update", "get": "retrieve"}),
        name="teams_update",
    ),
]
