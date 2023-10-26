from django.apps import AppConfig
from django.conf import settings
from asgiref.sync import async_to_sync, sync_to_async
import os, glob, threading, asyncio
from telegram import Update

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

        async def start():
            await bot.app.app.initialize()
            offset = 0
            while True:
                await asyncio.sleep(0.5)
                updates = await bot.app.app.bot.get_updates(offset = offset)
                if not updates:
                    return
                
                last_update: Update = updates[-1]
                offset = last_update.update_id
                print(await asyncio.gather(*[bot.app.app.process_update(update) for update in updates]))
                await bot.app.app.update_persistence()

        t = threading.Thread(target = async_to_sync(start))
        t.setDaemon(True)
        t.start()