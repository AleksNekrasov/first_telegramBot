from aiogram import Router, F
from aiogram.fsm.context import FSMContext
from aiogram.types import Message, CallbackQuery, ReplyKeyboardRemove
from aiogram.filters import Command
from random import randint

from states_FSM import Form
from keyboards.kb_for_start import kb_for_start
from keyboards.kb_for_game import kb_yes_or_no, kb_exit

router = Router()

# Словарь, в котором будут храниться данные пользователя
users = {}

@router.message(Command('exit'))
async def cmd_wichod(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(
        text='Очень жаль, что ты не хочешь закончить игру.\n\n',
        reply_markup=ReplyKeyboardRemove()
    )
    await message.answer(
        text='Вы находитесь в главном меню',
        reply_markup=kb_for_start()
    )





@router.callback_query(F.data == 'want_a_game?')
async def cmd_want_a_game(callback: CallbackQuery):
    await callback.message.answer(text='Сыграем?', reply_markup=kb_yes_or_no())
    await callback.answer()


@router.callback_query(F.data == 'No')
async def cmd_no(callback: CallbackQuery):
    await callback.message.answer(text='Приходи в другой раз ')
    await callback.message.answer(text='Вы в главном меню:',
                                  reply_markup=kb_for_start())
    await callback.answer()

@router.callback_query(F.data == 'Yes')
async def cmd_yes(callback: CallbackQuery, state: FSMContext):
    hidden_number = randint(1,100)
    await state.update_data(hidden_number=hidden_number, attempts=0) # Храним число и попытки в FSM

    await callback.message.answer(text=f'Отлично!\n'
                                  f'Я загадал число от 1 до 100'
                                  f'у Тебя 7 попыток чтобы его отгадать.')
    await state.set_state(Form.in_game)
    await callback.answer()

@router.message(Form.in_game)  # возможно нужно будет убрать 'state='
async def cmd_in_game(message: Message, state: FSMContext):

    fsm_data = await state.get_data()
    attempts = fsm_data.get('attempts')
    hidden_number = fsm_data.get('hidden_number')

    # Проверяем, что введено число
    if message.text.isdigit() and 1 <= int(message.text) <= 100:
        game_number = int(message.text)
        attempts += 1

        if game_number == hidden_number:
            await message.answer(
                text='Ура!!! Вы угадали число!\n\nМожет, сыграем еще?',
                reply_markup=kb_yes_or_no()
            )
            await state.clear()

        else:
            # Подсказка игроку
            if game_number > hidden_number:
                await message.answer(text='Мое число меньше!',
                                     reply_markup=kb_exit())
            else:
                await message.answer(text='Мое число больше!',
                                     reply_markup=kb_exit())

            if attempts >= 7:
                await message.answer(
                    text=f'К сожалению, все попытки исчерпаны. '
                         f'Я загадал число: {hidden_number}\n\nМожет, сыграем снова?',
                    reply_markup=kb_yes_or_no()
                )
                await state.clear()
            #  Сохраняем обновлённые данные в состояние
            else:
                await state.update_data(attempts=attempts)

    else:
        await message.answer(text='Пожалуйста, введи число от 1 до 100.')




