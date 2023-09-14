from django.apps import AppConfig


class StokappConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'stokApp'
    
    
    def ready(self):
        import stokApp.signals