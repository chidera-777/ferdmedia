from django.apps import AppConfig


class FerdmediaConfig(AppConfig):
    name = 'ferdmedia'
    def ready(self):
      import ferdmedia.signals
