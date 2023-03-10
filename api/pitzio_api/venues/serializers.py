from rest_framework import serializers

from pitzio_api.sports.models import Sport

from .models import Venue


class VenueSerializer(serializers.ModelSerializer):
    sport = serializers.PrimaryKeyRelatedField(
        queryset=Sport.objects.all(), required=True
    )

    class Meta:
        model = Venue
        fields = "__all__"
