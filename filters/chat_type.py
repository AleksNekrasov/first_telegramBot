from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message

class ChatTypeFilter(BaseFilter):
    def __init__(self, chat_type: str | list):
        self.chat_type = chat_type

    async def __call__(self, message: Message)-> bool:
        if isinstance(self.chat_type, str):
            return self.chat_type == message.chat.type # True | False
        else:
            return message.chat.type in self.chat_type # True | False
