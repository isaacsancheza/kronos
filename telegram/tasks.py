from celery import shared_task
from telebot import TeleBot
from django.conf import settings


@shared_task
def send_message(chat_id, message, parse_mode=None):
    bot = TeleBot(settings.TELEGRAM_TOKEN, parse_mode=None)
    bot.send_message(chat_id, message)
