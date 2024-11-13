from django.apps import AppConfig


class ExampleConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "movie"
    verbose_name = "电影"