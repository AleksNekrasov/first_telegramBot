from aiogram import Router
from aiogram.enums.dice_emoji import DiceEmoji
from aiogram.types import Message
from aiogram.filters import Command

#созданный мною фильтр
from filters.chat_type import ChatTypeFilter

#==============================================================
router = Router()

# фильтры можно цеплять прямо на роутеры!
# В этом случае проверка будет выполнена ровно один раз,
# когда апдейт долетит до этого роутера

router.message.filter(
    ChatTypeFilter(chat_type= ["group", "supergroup"])
)

@router.message(Command('dice'))
async def cmd_dice_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.DICE)

@router.message(Command(commands=['basketball'])) # по сути тоже самое что Command('basketball')
async def cmd_basketball_in_group(message: Message):
    await message.answer_dice(emoji=DiceEmoji.BASKETBALL)



