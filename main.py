import logging

from aiogram import Bot, Dispatcher, executor, types
from dotenv import dotenv_values

# Configure logging
logging.basicConfig(filename='bot.log', level=logging.INFO, encoding='utf-8')

API_TOKEN = dotenv_values().get("TOKEN")
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    logging.info(message)
    await message.reply(f'Hello, {message.from_user.first_name}!')


@dp.message_handler(lambda message: message.text == 'I love you')
async def love(message: types.Message):
    logging.info(message)
    await message.answer(f'I love you too, {message.from_user.first_name}')
    # await message.answer_sticker()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
