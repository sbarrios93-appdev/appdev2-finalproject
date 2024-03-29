from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pitzio_api.accounts"

    def ready(self):
        from . import signals  # noqa
