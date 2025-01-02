from sys import prefix

from aiogram import Router, F
from aiogram.filters.callback_data import CallbackData
from aiogram.types import Message, KeyboardButton, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

#класс для фабрики колбэков
from callbackClasses.callbackClass import CallbackClass

# клавиатура для животных:
# да- еще одна генерация изображения
#нет - выход в главное меню
def kb_for_animals(animal: str):
    builder = InlineKeyboardBuilder()
    builder.row(
        InlineKeyboardButton(text="Да",
                             callback_data=CallbackClass(animal=animal).pack()
        ),
        InlineKeyboardButton(text='Нет',
                             callback_data=CallbackClass(animal='no_animal').pack()
        ),
    )
    return builder.as_markup(resize_keyboard=True)
