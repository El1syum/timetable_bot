from aiogram import types, Dispatcher

from buttons.common.start_buttons import start_buttons
from data.config import logging


async def love(message: types.Message):
    logging.info(message)
    await message.answer(f'I love you, {message.from_user.first_name}', reply_markup=start_buttons())


def register_love(dp: Dispatcher):
    dp.register_message_handler(love, lambda message: message.text == 'Secret')
