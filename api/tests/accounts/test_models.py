import pytest
from django.contrib.auth import get_user_model

from pitzio_api.accounts.models import CustomUser


@pytest.mark.django_db
def test_get_user_model_data_returns_correct_user_model():
    assert get_user_model() == CustomUser


@pytest.mark.django_db
def test_create_normal_user(user_normal: CustomUser):
    assert user_normal.email == "testNormalUser@test.com"
    assert user_normal.date_of_birth == "1990-01-01"
    assert user_normal.first_name == "NormalFirstName"
    assert user_normal.last_name == "NormalLastName"
    assert user_normal.password == "testNormalUser"
    assert user_normal.is_active is True
    assert user_normal.is_admin is False
    assert user_normal.is_staff is False


@pytest.mark.django_db
def test_create_super_user(user_superUser: CustomUser):
    assert user_superUser.email == "testSuperUser@test.com"
    assert user_superUser.date_of_birth == "1990-01-01"
    assert user_superUser.first_name == "SuperFirstName"
    assert user_superUser.last_name == "SuperLastName"
    assert user_superUser.password == "testSuperUser"
    assert user_superUser.is_active is True
    assert user_superUser.is_admin is True
    assert user_superUser.is_staff is True


@pytest.mark.django_db
class TestCustomUserManager:
    def test_create_user(self):
        user = CustomUser.objects.create_user(
            email="testNormalUser@test.com",
            date_of_birth="1990-01-01",
            first_name="NormalFirstName",
            last_name="NormalLastName",
            password="testNormalUser",
        )
        assert isinstance(user, CustomUser)
        assert user.email == "testNormalUser@test.com"
        assert user.date_of_birth == "1990-01-01"
        assert user.first_name == "NormalFirstName"
        assert user.last_name == "NormalLastName"
        assert user.is_active is True
        assert user.is_admin is False
        assert user.is_staff is False
        assert str(user) == user.email

    def test_create_superuser(self):
        user = CustomUser.objects.create_superuser(
            email="testSuperUser@test.com",
            date_of_birth="1990-01-01",
            first_name="SuperFirstName",
            last_name="SuperLastName",
            password="testSuperUser",
        )
        assert user.email == "testSuperUser@test.com"
        assert user.date_of_birth == "1990-01-01"
        assert user.first_name == "SuperFirstName"
        assert user.last_name == "SuperLastName"
        assert user.is_active is True
        assert user.is_admin is True
        assert user.is_staff is True
        assert str(user) == user.email

    def test_create_user_without_email(self):
        with pytest.raises(ValueError):
            CustomUser.objects.create_user(
                email=None,
                date_of_birth="1990-01-01",
                first_name="NormalFirstName",
                last_name="NormalLastName",
                password="testNormalUser",
            )

    def test_create_superuser_without_email(self):
        with pytest.raises(ValueError):
            CustomUser.objects.create_superuser(
                email=None,
                date_of_birth="1990-01-01",
                first_name="NormalFirstName",
                last_name="NormalLastName",
                password="testNormalUser",
            )
