from aiogram.filters.callback_data import CallbackData



class CallbackClass(CallbackData, prefix='animals'):
    animal: str