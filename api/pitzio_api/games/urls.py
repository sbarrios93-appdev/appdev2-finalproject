from django.urls import path

from .views import GameViewSet, TeamViewSet

urlpatterns = [
    path("", GameViewSet.as_view({"get": "list"}), name="games"),
    path("teams", TeamViewSet.as_view({"get": "list"}), name="teams"),
]
