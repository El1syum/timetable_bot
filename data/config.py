import logging
import os.path

from dotenv import dotenv_values

if not os.path.exists('logs/'):
    os.mkdir('logs')

logging.basicConfig(filename='logs/bot.log', level=logging.INFO, encoding='utf-8')

API_TOKEN = dotenv_values().get("TOKEN")
