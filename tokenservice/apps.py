from django.apps import AppConfig


class TokenserviceConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tokenservice'

    def ready(self):
        import tokenservice.signals