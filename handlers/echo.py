from aiogram import types, Dispatcher

from data.config import logging


async def echo(message: types.Message):
    logging.info(message)
    await message.answer(message.text)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(echo)
