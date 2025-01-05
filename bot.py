#импорт конфига для токена
import os
import dotenv

from config_reader import config

import logging
import sys

import asyncio
from aiogram import Bot, Dispatcher


# Импорт ваших хендлеров
from handlers import start, group_games, questions, different_types, usernames, animals, game_1_100, Seva


"""Точка входа в приложение
Театр начинается с вешалки, а бот начинается с точки входа.
Пусть это будет файл bot.py.
В нём мы определим асинхронную функцию main(),
в которой создадим необходимые объекты и запустим поллинг.
Какие объекты являются необходимыми?
Во-первых, разумеется, бот.
Их может быть несколько, но об этом как-нибудь в другой раз.
Во-вторых, диспетчер.
Он занимается приёмом событий от Telegram и раскидыванием их по хэндлерам через фильтры и мидлвари."""


# Запуск бота
async def main():

    #---через библу os и dotenv-----------------------------------------------------
    #dotenv.load_dotenv()
    #bot = Bot(token=os.getenv('BOT_TOKEN'))
    #-------------------------------------------------------------------------------
    bot = Bot(token=config.bot_token.get_secret_value()) # через файл config_readers
    #--------------------------------------------------------------------------------
    dp = Dispatcher()

    #dp.include_routers(group_games.router, questions.router, different_types.router)

    # Альтернативный вариант регистрации роутеров по одному на строку
    dp.include_router(start.router)
    dp.include_router(game_1_100.router)
    # dp.include_router(questions.router)
    # dp.include_router(different_types.router)
    # dp.include_router(group_games.router)
    dp.include_router(usernames.router)
    dp.include_router(animals.router)
    dp.include_router(Seva.router)

    # Запускаем бота и пропускаем все накопленные входящие
    # Да, этот метод можно вызвать даже если у вас поллинг
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    # ---логгирование---------------
    logging.basicConfig(level=logging.INFO,
                        format='[{asctime}] #{levelname:8} {filename}:'
                               '{lineno} - {name} - {message}',
                        style='{',
                        stream=sys.stdout,
                        encoding='utf-8')

    # создаем логгер
    root_logger = logging.getLogger() # корневой. без имени
    root_logger.setLevel(logging.INFO)

    # Удаляем другие обработчики корневого логгера, если они есть
    for handler in root_logger.handlers:
        root_logger.removeHandler(handler)

    # ==ХЕНДЛЕР ДЛЯ ЗАПИСИ В ФАЙЛ================================
    # Инициализируем хэндлер, который будет записывать логи в файл
    file_handler = logging.FileHandler(filename='logs.log',
                                       mode='a', # 'a'-добавление , 'w'- перезапись файла
                                       encoding='utf-8')

    # создаем формат для logger формат
    # Установка формата для файла
    file_formatter = logging.Formatter(fmt='[{asctime}] #{levelname:8} {filename}:'
                                           '{lineno} - {name} - {message}',
                                       style='{')
    #прописываем в хендлер
    file_handler.setFormatter(fmt=file_formatter)
    file_handler.setLevel(level=logging.WARNING)   # уровень WARNING  и выше
    #=====================================================
    #==ХЕНДЛЕР ДЛЯ ЗАПИСИ В КОНСОЛЬ=======================
    # Обработчик для вывода логов в консоль
    console_handler = logging.StreamHandler(stream=sys.stdout)
    console_formatter = logging.Formatter(fmt='[{asctime}] #{levelname:8} {filename}:'
                                           '{lineno} - {name} - {message}',
                                       style='{')
    # прописываем в хендлер
    console_handler.setFormatter(fmt=console_formatter)
    #=====================================================

    # Добавляем хэндлеры логгеру
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

    #-------------------------------
    asyncio.run(main())

    # Закрываем файловый хендлер после завершения работы
    file_handler.close()

