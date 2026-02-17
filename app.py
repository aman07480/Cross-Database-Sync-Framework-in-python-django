from django.apps import AppConfig

class SyncAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'sync_app'

    def ready(self):
        import sync_app.signals
