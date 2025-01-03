import logging
import sys

# Инициализируем логгер модуля
logger = logging.getLogger(__name__)

#
# # Инициализируем форматтер
# formatter_2 = logging.Formatter(
#     fmt='#%(levelname)-8s [%(asctime)s] - %(filename)s:'
#         '%(lineno)d - %(name)s:%(funcName)s - %(message)s'
# )
#
# # Инициализируем хэндлер, который будет писать логи в `stdout`
# stdout = logging.StreamHandler(sys.stdout)
#
# # Добавляем хэндлеру фильтр `DebugWarningLogFilter`, который будет пропускать в
# # хэндлер только логи уровня `DEBUG` и `WARNING`
# stdout.addFilter(DebugWarningLogFilter())
#
# # Определяем форматирование логов в хэндлере
# stdout.setFormatter(fmt=formatter_2)
#
# # Добавляем хэндлер к логгеру
# logger.addHandler(stdout)

def devide_number(dividend: int | float, devider: int | float):

    logger.debug('Лог2 DEBUG')
    logger.info('Лог2 INFO')
    logger.warning('Лог2 WARNING')
    logger.error('Лог2 ERROR')
    logger.critical('Лог2 CRITICAL')

    try:
        return dividend / devider
    except ZeroDivisionError:
        logger.exception('Произошло деление на 0')