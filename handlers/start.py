from aiogram import Bot, Router, F
from aiogram.types import Message
from aiogram.filters import Command
import os

from config_reader import config
from keyboards.kb_for_start import kb_for_start


router = Router()

@router.message(Command('start'))
async def cmd_start(message: Message):

    await message.answer(text="Главное меню:",
        reply_markup=kb_for_start()
    )

@router.message(F.photo)
async def download_foto(message: Message):
    """
        Функция для обработки фотографий, отправленных в бот.
        Сохраняет изображение на локальный компьютер.
    """
    bot = Bot(token=config.bot_token.get_secret_value())

    # Указываем папку, куда будут сохраняться загруженные изображения
    DOWNLOAD_FOLDER = '/home/alex/Загрузки/tBot/photo'
    # Проверяем, существует ли папка, и создаём её, если её нет
    if not os.path.exists(DOWNLOAD_FOLDER):
        os.makedirs(DOWNLOAD_FOLDER)

    # Получаем информацию о загруженной фотографии.
    # Telegram отправляет несколько версий фото с разным разрешением,
    # берём самую большую (последнюю в списке)
    photo = message.photo[-1]

    # Загружаем информацию о файле Telegram (получаем путь к файлу на серверах Telegram)
    file_info = await bot.get_file(photo.file_id)

    # Определяем имя файла: используем оригинальное имя, но можно задать своё
    file_name = f'{message.from_user.id}_{photo.file_id}.jpg'

    # Путь для сохранения файла на вашем компьютере
    file_path = os.path.join(DOWNLOAD_FOLDER, file_name)

    # Скачиваем файл из Telegram и сохраняем его в локальной папке
    await bot.download_file(file_info.file_path, file_path)

    # Отправляем подтверждение пользователю
    await message.reply(f"Ваше изображение сохранено как: {file_path}", reply=False)
