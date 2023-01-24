import asyncio

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from data.config import logging, API_TOKEN
from handlers.create_timetable import register_create_timetable
from handlers.echo import register_echo
from handlers.love import register_love
from handlers.show_timetable import register_show_timetable
from handlers.start import register_welcome


def register_all_handlers(dp):
    register_welcome(dp)
    register_show_timetable(dp)
    register_create_timetable(dp)
    register_love(dp)
    register_echo(dp)


async def main():
    bot = Bot(token=API_TOKEN)
    storage = MemoryStorage()
    dp = Dispatcher(bot, storage=storage)
    register_all_handlers(dp)
    try:
        await dp.start_polling()
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        logging.error('Bot stopped!')
