from  telegram import Bot, Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ContextTypes
import requests

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Бот работает')
    
async def prazdnik_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    
    
    