from rest_framework import viewsets
from rest_framework.permissions import AllowAny, IsAdminUser

from pitzio_api.sports.models import Sport
from pitzio_api.sports.serializers import SportSerializer

# Create your views here.


class SportViewSet(viewsets.ModelViewSet):
    queryset = Sport.objects.all()
    serializer_class = SportSerializer

    def get_permissions(self):
        permission_classes: list
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == "list":
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAdminUser]
        return [permission() for permission in permission_classes]
