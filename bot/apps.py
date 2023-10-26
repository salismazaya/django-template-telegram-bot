from django.apps import AppConfig
from django.conf import settings
import os, glob

class BotConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bot'

    def ready(self):
        super().ready()

        run_once = os.environ.get('DJANGO_BOT_RUN_ONCE') == 'True'
        if run_once:
            return
        
        os.environ['DJANGO_BOT_RUN_ONCE'] = 'True'
        for file in glob.glob(str(settings.BASE_DIR.joinpath('bot/views/*.py'))):
            module = file.split('/')[-1].removesuffix('.py')
            __import__('bot.views.' + module)
        
        import bot.app