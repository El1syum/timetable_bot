from aiogram import types


def day_of_the_week():
    kb = [
        [types.KeyboardButton(text='Monday')],
        [types.KeyboardButton(text='Tuesday')],
        [types.KeyboardButton(text='Wednesday')],
        [types.KeyboardButton(text='Thursday')],
        [types.KeyboardButton(text='Friday')],
        [types.KeyboardButton(text='Saturday')],
        [types.KeyboardButton(text='Sunday')],
        [types.KeyboardButton(text='Cancel')],
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb, resize_keyboard=True,
                                         input_field_placeholder='Choose day of the week')
    return keyboard


if __name__ == '__main__':
    ...
