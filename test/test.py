import logging

logging.basicConfig(level=logging.DEBUG)






print(logging.DEBUG)
print(logging.INFO)
print(logging.WARNING)
print(logging.ERROR)
print(logging.CRITICAL)

loger = logging.getLogger(__name__)



loger.warning('предупреждение')
loger.critical('Опасность', stack_info=True)

#API_URL = 'https://api.telegram.org/bot'
#BOT_TOKEN = '7475484223:AAFGC4PkHZPkJzLFNpFMOhU3LK18_DC8weQ'

