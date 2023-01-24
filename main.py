import asyncio

from aiogram import Bot, Dispatcher

from data.config import logging, API_TOKEN
from handlers.echo import register_echo
from handlers.love import register_love
from handlers.start import register_welcome


def register_all_handlers(dp):
    register_welcome(dp)
    register_love(dp)
    register_echo(dp)


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(bot)
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
