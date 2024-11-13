from  telegram import Bot, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler
import requests
import json
import datetime


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('Бот работает')
    
async def prazdnik_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    def load_dict_from_json(filename):
        with open(filename, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        return data
    days_of_week = {
    1: "Понедельник",
    2: "Вторник",
    3: "Среда",
    4: "Четверг",
    5: "Пятница",
    6: "Суббота",
    7: "Воскресенье"
    }
    
    await update.message.reply_text(load_dict_from_json('prazdniki.json')[days_of_week[datetime.datetime.today().isoweekday()]])
    
def main():
    token = '7287412207:AAEs9MrRkDLmcJlcOQOUxM6wWq0zOVpriD4'
    application = Application.builder().token(token).build()
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('prazdnik', prazdnik_now))
    application.run_polling()

if __name__ == '__main__':
    main()
    
    
    