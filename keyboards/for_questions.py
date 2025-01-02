from aiogram.types import  ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_yes_or_no() ->ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text='да')
    kb.button(text='нет')
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)