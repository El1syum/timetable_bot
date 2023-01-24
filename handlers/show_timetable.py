from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import StatesGroup, State

from buttons.common.choose_day_of_the_week import day_of_the_week
from buttons.common.start_buttons import start_buttons
from data.config import logging
from postgresql.timetable import create_cursor, get_timetable


class Form2(StatesGroup):
    day = State()


async def choose_day(message: types.Message):
    logging.info(message)
    keyboard = day_of_the_week()

    await Form2.day.set()

    await message.reply(f'Alright, choose day of the week', reply_markup=keyboard)


async def cancel_handler(message: types.Message, state: FSMContext):
    """
    Allow user to cancel any action
    """
    current_state = await state.get_state()
    if current_state is None:
        return

    logging.info('Cancelling state %r', current_state)
    # Cancel state and inform user about it
    await state.finish()
    # And remove keyboard (just in case)
    await message.reply('Cancelled.', reply_markup=start_buttons())


async def get_data(message: types.Message, state: FSMContext):
    logging.info(message)
    day = message.text

    cursor = create_cursor()

    show_data = get_timetable(cursor, day, message.from_user.id)

    await message.answer('Here you go:\n' + show_data, reply_markup=start_buttons())

    await state.finish()


def register_show_timetable(dp: Dispatcher):
    dp.register_message_handler(choose_day, lambda message: message.text == 'Check TimeTable')
    dp.register_message_handler(cancel_handler, state='*', commands=['cancel'])
    dp.register_message_handler(cancel_handler, Text(equals='cancel', ignore_case=True), state='*')
    dp.register_message_handler(get_data, state=Form2.day)
