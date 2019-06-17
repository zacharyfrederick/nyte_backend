from django.apps import AppConfig
from django.conf import settings

class ApiConfig(AppConfig):
    name = 'api'

    def ready(self):
        import api.signals
        import stripe 

        stripe.api_key = settings.STRIPE_SECRET_KEY