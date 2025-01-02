from aiogram import Router, F
from aiogram.types import Message, KeyboardButton, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder

#фабрика колбэков
from callbackClasses.callbackClass import CallbackClass

def kb_for_start():
    builder = InlineKeyboardBuilder()

    builder.row(
        InlineKeyboardButton(text="Собачки", callback_data=CallbackClass(animal='dog').pack()),
        InlineKeyboardButton(text="Лисички", callback_data=CallbackClass(animal='fox').pack()),
        InlineKeyboardButton(text="Котятки", callback_data=CallbackClass(animal='cat').pack())
    )

    builder.row(
        InlineKeyboardButton(text="Сыграем в игру?", callback_data='want_a_game?')
    )

    return builder.as_markup(resize_keyboard=True)
