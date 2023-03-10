import uuid

from django.db import models

from pitzio_api.sports.models import Sport


# Create your models here.
class Venue(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    country_code = models.CharField(max_length=2)
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    image_url = models.URLField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    sport = models.ForeignKey(
        Sport,
        on_delete=models.CASCADE,
        related_name="venue",
    )
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
