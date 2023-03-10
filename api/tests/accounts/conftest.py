import pytest

from pitzio_api.accounts.models import CustomUser


@pytest.fixture
def register_fields():
    return {
        "email": "test@test.com",
        "date_of_birth": "1990-01-01",
        "first_name": "FirstName",
        "last_name": "LastName",
        "password": "testpass123",
    }


# Create your tests here.
@pytest.fixture
def user_normal() -> CustomUser:
    return CustomUser.objects.create(
        email="testNormalUser@test.com",
        date_of_birth="1990-01-01",
        first_name="NormalFirstName",
        last_name="NormalLastName",
        password="testNormalUser",
    )


@pytest.fixture
def user_superUser() -> CustomUser:
    return CustomUser.objects.create(
        email="testSuperUser@test.com",
        date_of_birth="1990-01-01",
        first_name="SuperFirstName",
        last_name="SuperLastName",
        password="testSuperUser",
        is_admin=True,
    )
