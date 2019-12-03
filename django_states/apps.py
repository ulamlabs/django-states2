from django.apps import AppConfig


class StateAppConfig(AppConfig):
    name = "django_states"
    verbose_name = "Django States"

    def ready(self):
        pass
