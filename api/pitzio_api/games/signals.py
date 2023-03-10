from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import FieldSide, Game, Team


@receiver(post_save, sender=Game)
def create_game(sender, instance, created, **kwargs):
    if created:
        Team.objects.create(
            game=instance, side=FieldSide.HOME, capacity=instance.capacity / 2
        )
        Team.objects.create(
            game=instance, side=FieldSide.AWAY, capacity=instance.capacity / 2
        )
