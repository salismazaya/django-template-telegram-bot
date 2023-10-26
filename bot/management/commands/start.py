from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = "Start bot polling"

    def handle(self, *args, **options):
        from bot.app import app

        print('BOT STARTED')
        app.run_polling()