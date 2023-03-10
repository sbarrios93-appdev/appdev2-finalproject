import pytest
from django.urls import reverse
from rest_framework.test import APIClient

from pitzio_api.accounts.models import CustomUser


@pytest.mark.django_db
class TestRegisterView:
    client = APIClient()

    def test_register_get_method_not_allowed(self):
        response = self.client.get(reverse("register"))
        assert response.status_code == 405

    def test_register_post_method_incorrect_data(self, register_fields):
        response = self.client.post(
            reverse("register"),
            {
                "email": register_fields["email"],
                "password": register_fields["password"],
                "password_confirm": "wrong_password",
                "first_name": register_fields["first_name"],
                "last_name": register_fields["last_name"],
                "date_of_birth": register_fields["date_of_birth"],
            },
        )
        assert response.status_code == 400
        assert CustomUser.objects.count() == 0

    def test_register_post_method_correct_data(self, register_fields):
        response = self.client.post(
            reverse("register"),
            {
                "email": register_fields["email"],
                "password": register_fields["password"],
                "password_confirm": register_fields["password"],
                "first_name": register_fields["first_name"],
                "last_name": register_fields["last_name"],
                "date_of_birth": register_fields["date_of_birth"],
            },
        )
        assert response.status_code == 201
        assert CustomUser.objects.count() == 1
