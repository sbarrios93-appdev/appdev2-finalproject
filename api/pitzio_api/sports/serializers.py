from rest_framework import serializers

from pitzio_api.venues.serializers import VenueSerializer

from .models import Sport


class SportSerializer(serializers.ModelSerializer):
    venue = VenueSerializer(many=True, read_only=True)

    class Meta:
        model = Sport
        fields = ["id", "name", "venue"]
