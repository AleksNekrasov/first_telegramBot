import logging


# Определяем свой фильтр, наследуясь от класса Filter библиотеки logging
class ErrorLogFilter(logging.Filter):
    # Переопределяем метод filter, который принимает `self` и `record`
    # Переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, record):
        return record.levelname == 'ERROR'


# Определяем свой фильтр, наследуюясь от класса Filter библиотеки logging
class DebugWarningLogFilter(logging.Filter):
    # Переопределяем метод filter, который принимает `self` и `record`
    # Переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, record):
        return record.levelname in ('DEBUG', 'WARNING')


# Определяем свой фильтр, наследуюясь от класса `Filter` библиотеки `logging`
class CriticalLogFilter(logging.Filter):
    # Переопределяем метод `filter`, который принимает `self` и `record`
    # Переменная рекорд будет ссылаться на объект класса LogRecord
    def filter(self, record):
        return record.levelname == 'CRITICAL'
