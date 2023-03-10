import datetime

import factory
from django.contrib.auth import get_user_model
from factory.django import DjangoModelFactory

from pitzio_api.games.models import Game
from pitzio_api.sports.models import Sport
from pitzio_api.venues.models import Venue


class UserFactory(DjangoModelFactory):
    class Meta:
        model = get_user_model()

    email = factory.Faker("email")
    date_of_birth = factory.Faker("date_of_birth")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
    plain_password = factory.PostGenerationMethodCall(
        "set_password",
        "testpassword",
    )


class SportFactory(DjangoModelFactory):
    class Meta:
        model = Sport

    name = ""
    created_at = factory.Faker("date_between", start_date="-1y", end_date="now")
    updated_at = factory.SelfAttribute("created_at")


class VenueFactory(DjangoModelFactory):
    class Meta:
        model = Venue

    name = factory.Faker("name")
    country_code = factory.Faker("country_code")
    city = factory.Faker("city")
    address = factory.Faker("address")
    image_url = factory.Faker("image_url")
    created_at = factory.Faker("date_between", start_date="-1y", end_date="now")
    updated_at = factory.SelfAttribute("created_at")
    sport = factory.SubFactory(SportFactory)
    capacity = factory.Faker("random_int", min=8, max=22, step=2)


class GameFactory(DjangoModelFactory):
    class Meta:
        model = Game

    date = factory.Faker(
        "date_time_between",
        start_date="now",
        end_date="+30d",
        tzinfo=datetime.timezone.utc,
    )

    venue = factory.SubFactory(VenueFactory)
    sport = factory.SubFactory(SportFactory)
    duration = factory.Faker(
        "random_element",
        elements=[
            datetime.timedelta(minutes=30),
            datetime.timedelta(minutes=45),
            datetime.timedelta(minutes=60),
            datetime.timedelta(minutes=75),
            datetime.timedelta(minutes=90),
        ],
    )
    capacity = 0
