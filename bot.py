#импорт конфига для токена
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
    bot = Bot(token=config.bot_token.get_secret_value())
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
    # логгирование
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())