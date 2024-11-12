from  telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler
import requests

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Бот работает')
    
async def prazdnik_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    with open('prazdnik.txt', 'r') as file:
        text = file.read()
    await update.message.reply_text(text)
    
def main():
    token = '7287412207:AAEs9MrRkDLmcJlcOQOUxM6wWq0zOVpriD4'
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler('prazdnik', prazdnik_now))
    application.run_polling()

if __name__ == '__main__':
    main()
    
    
    