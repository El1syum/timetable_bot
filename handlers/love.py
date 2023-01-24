from aiogram import types, Dispatcher

from data.config import logging


async def love(message: types.Message):
    logging.info(message)
    await message.answer(f'I love you too, {message.from_user.first_name}')


def register_love(dp: Dispatcher):
    dp.register_message_handler(love, lambda message: message.text == 'I love you')
