from aiogram import Router, F
import os

from aiogram.enums import ContentType
from aiogram.types import Message
from aiogram.types.input_file import FSInputFile
#from PIL import Image
import random

# инфа о блокировке бота
from  aiogram.filters import ChatMemberUpdatedFilter, KICKED
from aiogram.types import ChatMemberUpdated

from filters.admin_filters import IsAdmin

router = Router()

# Устанавливаем путь к изображению
DOWNLOAD_FOLDER = '/home/alex/Загрузки/tBot/photo'
IMAGE_PATH = os.path.join(DOWNLOAD_FOLDER, 'мопс.jpg')

def load_images_from_folder(folder_path):
    images = []  # Список для хранения путей к изображениям
    supported_extensions = (".jpg", ".jpeg", ".png")  # Поддерживаемые форматы

    if not os.path.exists(folder_path):
        print("Папка не найдена!")
        return images

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(supported_extensions):  # Проверяем расширение файла
            file_path = os.path.join(folder_path, filename)  # Получаем полный путь к файлу
            images.append(file_path)  # Добавляем путь к списку

    return images

admin_ids = [5096884737]

@router.message(F.text.lower() == 'мопс' and IsAdmin(admin_ids))
async def seva(message: Message):
    # if os.path.exists(IMAGE_PATH):           # проверяем что путь есть
    #     photo = InputFile(IMAGE_PATH)
    #     await message.answer_photo(photo=photo)
    # else:
    #     await message.answer("Изображение не найдено!")

    if os.path.exists(IMAGE_PATH):  # Проверяем, что файл существует
        images = load_images_from_folder(DOWNLOAD_FOLDER)
        random_image = random.choice(images)

        photo = FSInputFile(random_image)
        await message.answer_photo(photo=photo)  # Отправляем фото
    else:
        await message.answer("Изображение не найдено!")

# Инфа о блокировке бота
@router.my_chat_member(ChatMemberUpdatedFilter(member_status_changed=KICKED))
async def process_user_blocked_bot(event: ChatMemberUpdated):
    print(f'Пользователь {event.from_user.id} заблокировал бота')
