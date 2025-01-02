
from aiogram.types import Message, CallbackQuery
import aiohttp

from keyboards.kb_for_animals import kb_for_animals

API_CATS_URL = 'https://api.thecatapi.com/v1/images/search'
API_DOGS_URL = 'https://random.dog/woof.json'
API_FOX_URL = 'https://randomfox.ca/floof/'

ERROR_TEXT = 'Здесь должна была быть картинка с котиком :('

async def cats(callback):
    async with aiohttp.ClientSession() as session:
        async with session.get(API_CATS_URL) as cat_response:
            if cat_response.status == 200:
                cat_data = await cat_response.json()
                cat_link = cat_data[0]['url']
                await callback.message.answer_photo(photo=cat_link)
                await callback.message.answer(text='Еще котика?',
                                              reply_markup=kb_for_animals(animal='cat'))
                await callback.answer()
            else:
                await callback.message.answer(ERROR_TEXT)

async def dogs(callback):
    async with aiohttp.ClientSession() as session:

        while True: # этот бесконечный цикл делается из-за файла '.webm' который не поддерживает телеграм

            async with session.get(API_DOGS_URL) as dog_response:
                if dog_response.status == 200:

                    dog_data = await dog_response.json()
                    dog_link = dog_data['url']

                    # .endswith ПРИНИМАЕТ КОРТЕЖИ!!!!!
                    # Проверка расширения файла
                    if dog_link.lower().endswith(('.jpg', '.jpeg', '.png')):
                        await callback.message.answer_photo(photo=dog_link)
                        await callback.message.answer(text='Еще собачку?',
                                                      reply_markup=kb_for_animals(animal='dog'))
                        await callback.answer()
                        break

                    elif dog_link.lower().endswith('.gif'):
                        await callback.message.answer_animation(animation=dog_link)
                        await callback.message.answer(text='Еще собачку?',
                                                      reply_markup=kb_for_animals(animal='dog'))
                        await callback.answer()
                        break

                    elif dog_link.lower().endswith('.mp4'):
                        await callback.message.answer_video(video=dog_link)
                        await callback.message.answer(text='Еще собачку?',
                                                      reply_markup=kb_for_animals(animal='dog'))
                        await callback.answer()
                        break

                    else:
                        # Если формат неподдерживаемый, делаем новый запрос
                        continue

                else:
                    await callback.message.answer(ERROR_TEXT)
                    await callback.answer()


async def foxes(callback):
    async with aiohttp.ClientSession() as session:
        async with session.get(API_FOX_URL) as fox_response:
            if fox_response.status == 200:
                fox_data = await fox_response.json()
                fox_link = fox_data['image']
                await callback.message.answer_photo(fox_link)
                await callback.message.answer(text='Еще лисичку??',
                                              reply_markup=kb_for_animals(animal='fox'))
                await callback.answer()
                #await message.answer(message.model_dump_json(indent=4,exclude_none=True))

            else:
                await callback.message.answer('ERROR')