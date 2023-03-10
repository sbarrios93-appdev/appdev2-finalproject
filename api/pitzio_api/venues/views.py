from rest_framework import viewsets

from .models import Venue
from .serializers import VenueSerializer


# Create your views here.
class VenueViewSet(viewsets.ModelViewSet):
    queryset = Venue.objects.all()
    serializer_class = VenueSerializer
