from typing import List

from aiogram import Router, F
from aiogram.types import Message

from filters.find_usernames import HasUsernameFilter, NumbersInMessage

router =Router()

@router.message(F.text,HasUsernameFilter())
async def message_with_username(message: Message, usernames: List[str]):
    message.d
    await message.reply(
        f'Спасибо! Обязательно подпишусь на '
        f'{", ".join(usernames)}'
    )

@router.message(F.text.lower().startswith('найди числа'),
            NumbersInMessage())
# Помимо объекта типа Message, принимаем в хэндлер список чисел из фильтра
# по соответствующему ключу `numbers`
async def process_if_numbers(message: Message, numbers: list[int]):
    await message.answer(
            text=f'Нашел: {", ".join(str(num) for num in numbers)}')

# Этот хэндлер будет срабатывать, если сообщение пользователя
# начинается с фразы "найди числа", но в нем нет чисел
@router.message(F.text.lower().startswith('найди числа'))
async def process_if_not_numbers(message: Message):
    await message.answer(
            text='Не нашел что-то :(')