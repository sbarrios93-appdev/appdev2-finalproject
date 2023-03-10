from rest_framework import serializers

from pitzio_api.utils.common_serializer_validators import even_number

from .models import Game, Team


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
        depth = 1


class GameSerializer(serializers.ModelSerializer):
    joined = serializers.SerializerMethodField()
    teams = TeamSerializer(many=True)

    class Meta:
        model = Game
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")
        depth = 1

        def validate_capacity(self, value):
            even_number(value)
            return value

    def get_joined(self, instance):
        return instance.joined_players

    def get_teams(self, instance):
        return instance.teams.all()
