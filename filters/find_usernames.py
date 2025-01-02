from typing import Dict, Any

from aiogram.filters import BaseFilter
from aiogram.types import Message

class HasUsernameFilter(BaseFilter):

    async def __call__(self, message: Message)-> bool | Dict[str, Any]:
        # Если entities вообще нет, вернётся None,
        # в этом случае считаем, что это пустой список
        entities = message.entities or []

        # Проверяем любые юзернеймы и извлекаем их из текста
        # методом extract_from(). Подробнее см. главу
        # про работу с сообщениями
        found_usernames = [
            item.extract_from(message.text) for item in entities
            if item.type == 'mention'
        ]

        # Если юзернеймы есть, то "проталкиваем" их в хэндлер
        # по имени "usernames"
        if len(found_usernames) > 0:
            return {"usernames": found_usernames}
        # Если не нашли ни одного юзернейма, вернём False
        return False

# поиск числа в сообщении
# Этот фильтр будет проверять наличие неотрицательных чисел
# в сообщении от пользователя, и передавать в хэндлер их список
class NumbersInMessage(BaseFilter):
    async def __call__(self, message: Message) -> bool | dict[str, list[int]]:
        numbers = []
        # Разрезаем сообщение по пробелам, нормализуем каждую часть, удаляя
        # лишние знаки препинания и невидимые символы, проверяем на то, что
        # в таких словах только цифры, приводим к целым числам
        # и добавляем их в список
        for word in message.text.split():
            normalized_word = word.replace('.', '').replace(',', '').strip()
            if normalized_word.isdigit():
                numbers.append(int(normalized_word))
        # Если в списке есть числа - возвращаем словарь со списком чисел по ключу 'numbers'
        if numbers:
            return {'numbers': numbers}
        return False