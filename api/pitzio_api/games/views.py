from rest_framework import viewsets

from .models import Game, Team
from .serializers import GameSerializer, TeamSerializer


# Create your views here.
class GameViewSet(viewsets.ModelViewSet):
    serializer_class = GameSerializer

    def get_queryset(self):
        queryset = Game.objects.all()
        id = self.request.query_params.get("id", None)
        if id is not None:
            queryset = queryset.filter(id=id)
        return queryset


class TeamViewSet(viewsets.ModelViewSet):
    serializer_class = TeamSerializer

    def get_queryset(self):
        queryset = Team.objects.all()
        game_id = self.request.query_params.get("game_id", None)
        if game_id is not None:
            queryset = queryset.filter(game_id=game_id)
        return queryset
