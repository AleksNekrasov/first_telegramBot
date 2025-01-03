import logging

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)

# # Инициализируем форматтер
# formatter_3 = logging.Formatter(
#     fmt='#%(levelname)-8s [%(asctime)s] - %(message)s'
# )
#
# # Инициализируем первый хэндлер, который будет писать логи в `stderr`
# stderr = logging.StreamHandler()
# # Инициализируем второй хэндлер, который будет писать логи в файл `critical.log`
# critical_file = logging.FileHandler('critical.log', mode='w', encoding='utf-8')
#
# # Определяем форматирование логов во втором хэндлере
# critical_file.setFormatter(fmt=formatter_3)
#
# # Добавляем второму хэндлеру фильтр `CriticalLogFilter`, который будет
# # пропускать в хэндлер только логи уровня `CRITICAL`
# critical_file.addFilter(CriticalLogFilter())
#
# # Добавляем хэндлеры к логгеру
# logger.addHandler(stderr)
# logger.addHandler(critical_file)


def square_number(number: int | float):

    logger.debug('Лог3 DEBUG')
    logger.info('Лог3 INFO')
    logger.warning('Лог3 WARNING')
    logger.error('Лог3 ERROR')
    logger.critical('Лог3 CRITICAL')

    return number**2