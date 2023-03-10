import enum
import uuid

from django.db import models


@enum.unique
class FieldSide(int, enum.Enum):
    HOME = 0
    AWAY = 1

    @classmethod
    def choices(cls):
        return [(item.value, item.name) for item in cls]


# Create your models here.
class Game(models.Model):  # type: ignore
    # see: https://github.com/django-money/django-money/issues/677
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateTimeField()
    venue = models.ForeignKey(
        "venues.Venue",
        on_delete=models.CASCADE,
        related_name="games",
    )
    sport = models.ForeignKey(
        "sports.Sport",
        on_delete=models.CASCADE,
        related_name="games",
    )

    capacity = models.PositiveIntegerField()

    duration = models.DurationField()

    @property
    def joined_players(self):
        return sum(team.players.count() for team in self.teams.all())


class Team(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    side = models.IntegerField(choices=FieldSide.choices())
    capacity = models.PositiveIntegerField()
    players = models.ManyToManyField(
        "accounts.CustomUser",
        related_name="teams",
    )
    game = models.ForeignKey(
        Game,
        on_delete=models.CASCADE,
        related_name="teams",
    )

    @property
    def is_full(self):
        return self.capacity == self.players.count()

    @property
    def is_empty(self):
        return self.players.count() == 0

    @property
    def remaining_capacity(self):
        return self.capacity - self.players.count()
