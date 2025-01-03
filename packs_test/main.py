import logging.config


#from logging_settings import logging_config  # через питоновский словарь
import yaml   # через yaml файл

from module_1 import main

with open('logging_config.yaml', 'rt') as yaml_file:     # 'rt' чтение в текстовом режиме
    log_config = yaml.safe_load(yaml_file.read())


logging.config.dictConfig(log_config)

# Загружаем настройки логирования из словаря `logging_config`
#logging.config.dictConfig(logging_config)


# Исполняем функцию `main` из модуля `module_1.py`
main()
