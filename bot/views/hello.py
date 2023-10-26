from telegram import Update, Update as Update
from telegram.ext import ContextTypes, CommandHandler, ContextTypes
from bot.views.base import View

class HelloView(View):
    async def execute(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        await update.message.reply_text('Hello')
    
    def handler(self):
        return CommandHandler('hello', self.execute)