from django.apps import AppConfig


class CoreCustomConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core_custom'

    def ready(self):
        import core_custom.signals.handlers
