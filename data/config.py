import logging

from dotenv import dotenv_values

logging.basicConfig(filename='logs/bot.log', level=logging.INFO, encoding='utf-8')

API_TOKEN = dotenv_values().get("TOKEN")
