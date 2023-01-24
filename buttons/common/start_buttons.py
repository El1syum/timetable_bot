from aiogram import types


def start_buttons():
    kb = [
        [types.KeyboardButton(text='Create TimeTable')],
        [types.KeyboardButton(text='Check TimeTable')],
        [types.KeyboardButton(text='Secret')],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True, input_field_placeholder='Choose action')
    return keyboard


if __name__ == '__main__':
    ...
