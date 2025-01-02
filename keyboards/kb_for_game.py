from aiogram.types import InlineKeyboardButton, KeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder


def kb_yes_or_no():
    builder = InlineKeyboardBuilder()

    builder.button(
        text='Да',
        callback_data='Yes'
    )
    builder.button(
        text='Нет',
        callback_data='No'
    )
    builder.adjust(2)

    return builder.as_markup()

def kb_exit():
    builder = ReplyKeyboardBuilder()
    builder.button(
        text='/exit'
    )
    builder.adjust(2)

    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder='Для выхода из игры напишите /exit'
    )


