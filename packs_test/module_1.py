import logging

from module_2 import devide_number
from module_3 import square_number

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)


# # Инициализируем форматтер
# formatter_1 = logging.Formatter(
#     fmt='[%(asctime)s] #%(levelname)-8s %(filename)s:'
#         '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
# )
#
# # Инициализируем хэндлер, который будет писать логи в файл `error.log`
# error_file = logging.FileHandler('error.log', 'w', encoding='utf-8')
# # Устанавливаем хэндлеру уровень `DEBUG`
# error_file.setLevel(logging.DEBUG)
#
# # Добавляем хэндлеру фильтр `ErrorLogFilter`, который будет пропускать в
# # хэндлер только логи уровня `ERROR`
# error_file.addFilter(ErrorLogFilter())
#
# # Определяем форматирование логов в хэндлере
# error_file.setFormatter(formatter_1)
#
# # Добавляем хэндлер в логгер
# logger.addHandler(error_file)


def main():
    a, b = 12, 2
    c, d = 4, 0

    logger.debug('Лог1 DEBUG')
    logger.info('Лог1 INFO')
    logger.warning('Лог1 WARNING')
    logger.error('Лог1 ERROR')
    logger.critical('Лог1 CRITICAL')

    print(devide_number(a, square_number(b)))
    print(devide_number(square_number(c), d))