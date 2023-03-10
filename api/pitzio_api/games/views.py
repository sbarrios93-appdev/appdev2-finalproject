from rest_framework import permissions, status, viewsets
from rest_framework.response import Response

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
            side = self.request.query_params.get("side", None)
            if side is not None:
                queryset = queryset.filter(game_id=game_id, side=side)
            else:
                queryset = queryset.filter(game_id=game_id)

        player_id = self.request.query_params.get("player_id", None)
        if player_id is not None:
            queryset = queryset.filter(players__id=player_id)
        return queryset

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        if request.user in instance.players.all():
            instance.players.remove(request.user)
        elif instance.is_full:
            return Response(
                {"message": "Team is full"}, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            instance.players.add(request.user)
        serializer = self.get_serializer(instance)
        return Response(serializer.data)
