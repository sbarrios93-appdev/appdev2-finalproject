import random

from django.core.management.base import BaseCommand
from django.db import transaction

from factories import GameFactory, SportFactory, UserFactory, VenueFactory
from pitzio_api.accounts.models import CustomUser
from pitzio_api.games.models import Game, Team
from pitzio_api.sports.models import Sport
from pitzio_api.venues.models import Venue

NUM_USERS = 50
NUM_VENUES = 10
NUM_GAMES = 20
SPORTS = ["Soccer", "Basketball", "Baseball", "Football"]

VENUES_NAMES = [
    "Hilltop Field",
    "Lakeside Field",
    "Lions Field",
    "Eagle Field",
    "Tigers Field",
    "Panthers Field",
    "Ravens Field",
    "Eagles Field",
    "Falcons Field",
    "Wildcats Field",
]


VENUES_IMAGES = [
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1508098682722-e99c43a406b2.jpg?alt=media&token=861632ec-e144-43e4-a3b6-4283bbaacb89",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1522778119026-d647f0596c20.jpg?alt=media&token=80a07d3c-e819-422b-b4dc-f41baf7404c8",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1594467974320-2cddc11e52bc.jpg?alt=media&token=31d47e45-6eee-4bc6-9973-22d5fde74bab",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1508098682722-e99c43a406b2.jpg?alt=media&token=861632ec-e144-43e4-a3b6-4283bbaacb89",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1512719994953-eabf50895df7.jpg?alt=media&token=7ac37d1a-ea71-4c46-a6f5-64349ded4582",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1489944440615-453fc2b6a9a9.jpg?alt=media&token=8bb89355-19a3-428d-86ae-a0176e5026ef",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1512719994953-eabf50895df7.jpg?alt=media&token=7ac37d1a-ea71-4c46-a6f5-64349ded4582",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1522778119026-d647f0596c20.jpg?alt=media&token=80a07d3c-e819-422b-b4dc-f41baf7404c8",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1599158150601-1417ebbaafdd.jpg?alt=media&token=cc51f5ae-36c6-4847-9901-92bdbd92a6a5",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1540747913346-19e32dc3e97e.jpg?alt=media&token=2d2cff2a-58dd-41ea-905b-3ef5e10656c6",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1540747913346-19e32dc3e97e.jpg?alt=media&token=2d2cff2a-58dd-41ea-905b-3ef5e10656c6",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1508098682722-e99c43a406b2.jpg?alt=media&token=861632ec-e144-43e4-a3b6-4283bbaacb89",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1599158150601-1417ebbaafdd.jpg?alt=media&token=cc51f5ae-36c6-4847-9901-92bdbd92a6a5",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1599158150601-1417ebbaafdd.jpg?alt=media&token=cc51f5ae-36c6-4847-9901-92bdbd92a6a5",
    "https://firebasestorage.googleapis.com/v0/b/pitzio-dev-78bcb.appspot.com/o/photo-1599158150601-1417ebbaafdd.jpg?alt=media&token=cc51f5ae-36c6-4847-9901-92bdbd92a6a5",
]


class Command(BaseCommand):
    help = "Generates test data"

    @transaction.atomic
    def handle(self, *args, **kwargs):
        self.stdout.write("Deleting old data...")
        models = [CustomUser, Sport, Venue, Game, Team]
        for m in models:
            m.objects.all().delete()

        self.stdout.write("Creating new data...")
        # create superuser
        UserFactory(
            email="test@test.com",
            date_of_birth="2000-01-01",
            first_name="Test",
            last_name="Test",
            plain_password="test",
            is_admin=True,
        )
        # Create all the users
        people = []
        for _ in range(NUM_USERS):
            person = UserFactory()
            people.append(person)
        # Create all the venues

        sports = []
        for sport in SPORTS:
            sport = SportFactory(name=sport)
            sports.append(sport)

        venues = []
        for _ in range(NUM_VENUES):
            sport = random.choice(sports)
            venue_image = random.choice(VENUES_IMAGES)
            venue = VenueFactory(
                sport=sport,
                image_url=venue_image,
                name=VENUES_NAMES.pop(),
            )
            venues.append(venue)

        games = []
        for _ in range(NUM_GAMES):
            venue = random.choice(venues)
            game = GameFactory(
                venue=venue,
                sport=venue.sport,
                capacity=random.randrange(8, venue.capacity + 1, 2),
                # players=people,
            )
            games.append(game)

        for game in games:
            teams = [team for team in game.teams.all()]
            all_people = [p for p in people]
            for team in teams:
                capacity = team.capacity
                joined = random.sample(all_people, random.randint(0, capacity))
                team.players.add(*joined)
                # removed already joined people from the list
                all_people = [p for p in all_people if p not in joined]
