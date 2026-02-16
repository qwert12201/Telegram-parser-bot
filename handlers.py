from telegram.ext import CallbackContext
from telegram import Update

from db import db_session
from models import City, Country, Language, CurrencyRate, Name
import jobs

message = "Данные недоступны"

def li_getter(model) -> str:
    items = db_session.query(model).all()
    return "\n".join(item.name for item in items)

def greet_user(update: Update, context: CallbackContext):
    username = update.message.chat.username
    update.message.reply_text(f"Привет {username}!")
    update.message.reply_text("Это тестовый бот, для обучения")

def get_cities(update: Update, context: CallbackContext):
    a = li_getter(City)
    if a is None:
        update.message.reply_text(message)
        return
    update.message.reply_text(a)

def get_langs(update: Update, context: CallbackContext):
    a = li_getter(Language)
    if a is None:
        update.message.reply_text(message)
        return
    update.message.reply_text(a)

def get_countries(update: Update, context: CallbackContext):
    a = li_getter(Country)
    if a is None:
        update.message.reply_text(message)
        return
    update.message.reply_text(a)

def get_names(update: Update, context: CallbackContext):
    a = li_getter(Name)
    if a is None:
        update.message.reply_text(message)
        return
    update.message.reply_text(a)

def get_curse(update: Update, context: CallbackContext):
    try:
        rates = db_session.query(CurrencyRate).order_by(CurrencyRate.date.desc()).all()
        if not rates:
            update.message.reply_text(message)
            return
        p = "\n".join(f"Курс доллара = {rate.rate} {rate.date}" for rate in rates)
        update.message.reply_text(p)
    except Exception as e:
        update.message.reply_text(f"Ошибка получения курса: {e}")

def save(update: Update, context: CallbackContext):
    jobs.save()
    update.message.reply_text("Данные обновлены")
