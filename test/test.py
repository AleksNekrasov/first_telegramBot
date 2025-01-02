import logging
import sys

#класс фильтрации
class ErrorLogFilter(logging.Filter):
    # Переопределяем метод filter, который принимает `self` и `record`
    # Переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, log_record) -> bool:

        return log_record.levelname == 'ERROR' and 'важно' in log_record.msg.lower()


# Определяем первый вид форматирования
format_1 = '#%(levelname)-8s [%(asctime)s] - %(filename)s:'\
           '%(lineno)d - %(name)s - %(message)s'
# Определяем второй вид форматирования
format_2 = '#{levelname:8} [{asctime}] - {filename}:'\
           '{lineno} - {name} - {message}'

# Инициализируем первый форматтер
formatter_1 = logging.Formatter(fmt=format_1)
# Инициализируем второй форматтер
formatter_2 = logging.Formatter(fmt=format_2,
                                style='{')

# Создаем логгер
logger = logging.getLogger(__name__)

# Инициализируем хэндлер, который будет перенаправлять логи в stderr
stderr_handler = logging.StreamHandler()
# Инициализируем хэндлер, который будет перенаправлять логи в stdout
stdout_handler = logging.StreamHandler(sys.stdout)
# Инициализируем хэндлер, который будет записывать логи в файл
file_handler = logging.FileHandler('logs.log', mode='w') # mode='w' - перезапись в файл

# Устанавливаем форматтеры для хэндлеров
stderr_handler.setFormatter(formatter_1)
stdout_handler.setFormatter(formatter_2)
file_handler.setFormatter(formatter_2)

# Подключаем фильтр к хэндлеру
file_handler.addFilter(ErrorLogFilter())

# Добавляем хэндлеры логгеру
logger.addHandler(stdout_handler)
logger.addHandler(stderr_handler)
logger.addHandler(file_handler)

# Создаем лог
logger.warning('Важно! Это лог с предупреждением!')
logger.error('Важно! Это лог с ошибкой!')
logger.info('Важно! Это лог с уровня INFO!')
logger.error('Это лог с ошибкой!')

logger.exception(" лог эксепт")




# print(logging.DEBUG)
# print(logging.INFO)
# print(logging.WARNING)
# print(logging.ERROR)
# print(logging.CRITICAL)



#API_URL = 'https://api.telegram.org/bot'
#BOT_TOKEN = '7475484223:AAFGC4PkHZPkJzLFNpFMOhU3LK18_DC8weQ'

