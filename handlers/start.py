from aiogram import types, Dispatcher

from buttons.common.start_buttons import start_buttons
from data.config import logging


async def send_welcome(message: types.Message):
    logging.info(message)
    await message.reply(f'Hello, {message.from_user.first_name}!', reply_markup=start_buttons())


def register_welcome(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
