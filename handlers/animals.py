
from aiogram import Router, F
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message, CallbackQuery
from keyboards.kb_for_start import kb_for_start
#import aiohttp

from callbackClasses.callbackClass import CallbackClass
from def_animals.def_animals import cats, dogs, foxes


router = Router()


@router.callback_query(CallbackClass.filter())
async def cmd_animals(callback: CallbackQuery, callback_data: CallbackClass):
    animal = callback_data.animal

    match animal:
        case 'cat':
           await cats(callback)
        case 'dog':
            await dogs(callback)
        case 'fox':
            await foxes(callback)
        case 'no_animal':
            await callback.message.answer(text='Жаль..',
                                          reply_markup=kb_for_start())





