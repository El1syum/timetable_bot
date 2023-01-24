from aiogram import types


def choose_day_of_week():
    keyboard_markup = types.InlineKeyboardMarkup(row_width=4)
    text_and_data = (
        ('Mon', 'monday'),
        ('Tue', 'tuesday'),
        ('Wed', 'wednesday'),
        ('Thu', 'thursday'),
        ('Fri', 'friday'),
        ('Sat', 'saturday'),
        ('Sun', 'sunday')
    )
    row_btns = (types.InlineKeyboardButton(text, callback_data=data) for text, data in text_and_data)
    keyboard_markup.row(*row_btns)

    return keyboard_markup


if __name__ == '__main__':
    ...
