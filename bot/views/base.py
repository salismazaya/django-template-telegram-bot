from __future__ import annotations
from telegram import Update as _Update
from telegram.ext import ContextTypes as _ContextTypes, CommandHandler as _CommandHandler
from bot.app import app as _app

class View:
    async def execute(self, update: _Update, context: _ContextTypes.DEFAULT_TYPE):
        pass

    def handler(self):
        pass

    def error_handler(self):
        pass

    def __init_subclass__(cls):
        obj = cls()
        _app.add_handler(obj.handler())
        _app.add_error_handler(obj.error_handler())