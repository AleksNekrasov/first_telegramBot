from aiogram import Router, F
from aiogram.types import Message
from pydantic.v1.validators import anystr_strip_whitespace

router = Router()

@router.message(F.text)
async def message_with_text(message: Message):
    await message.answer(
        text="Это текстовое сообщение"
    )

@router.message(F.sticker)
async def message_with_sticker(message: Message):
    await message.answer(
        text="Это стикер!"
    )

@router.message(F.animation)
async def message_with_animation(message: Message):
    await message.answer(
        text='Это Гифка!'
    )
