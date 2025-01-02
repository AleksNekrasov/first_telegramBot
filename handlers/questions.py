from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, ReplyKeyboardRemove

#импорты из моих файлов(мои созданные)
from keyboards.for_questions import get_yes_or_no

router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):
    await message.answer(
        text='Вы довольны своей работой?',
        reply_markup=get_yes_or_no()
    )

@router.message(F.text.lower() == 'да')
async def answer_yes(message: Message):
    await message.answer(
        text='Отлично!!',
        reply_markup=ReplyKeyboardRemove()
    )

@router.message(F.text.lower() == 'нет')
async def answer_no(message: Message):
    await message.answer(
        text='Нужно работать над собой!!',
        reply_markup=ReplyKeyboardRemove()
    )