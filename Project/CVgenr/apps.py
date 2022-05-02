from django.apps import AppConfig


class CvgenrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'CVgenr'

    def ready(self):
        import CVgenr.signals