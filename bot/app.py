from django.conf import settings as _settings
from telegram.ext import ApplicationBuilder as _ApplicationBuilder

app = _ApplicationBuilder().token(_settings.TELEGRAM_BOT_TOKEN).build()