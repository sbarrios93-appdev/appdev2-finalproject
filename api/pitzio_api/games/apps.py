from django.apps import AppConfig


class GamesConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "pitzio_api.games"

    def ready(self):
        from . import signals  # noqa
