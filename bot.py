from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


TOKEN = "6263933313:AAEon8UHzpE8nUjJoIid0qYYt_7i21SqtEE"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Да")
    keyboard.add(button_1)
    button_2 = "Я уже знаю, что хочу заказать"
    keyboard.add(button_2)
    await message.answer("Добро пожаловать в наш мир, где мы создаем неповторимые и индивидуальные деревянные предметы декора. \nМы рады услышать Ваши предложения и исполнять Ваши мечты! Отдаем максимум внимания каждому клиенту и стремимся предоставить высококачественный продукт.\n\nХочешь выбрать функциональный и красивый декор для дома?", reply_markup=keyboard)


@dp.message_handler(commands='help')
async def any_text_message(message: types.Message):
   await message.answer("Добро пожаловать в наш мир, где мы создаем неповторимые и индивидуальные деревянные предметы декора. \nМы рады услышать Ваши предложения и исполнять Ваши мечты! Отдаем максимум внимания каждому клиенту и стремимся предоставить высококачественный продукт.\n\nОтпрвь '/start' для начала")


@dp.message_handler(text="Да")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Шкатулка")
    keyboard.add(button_1)
    button_2 = "Фотография"
    keyboard.add(button_2)
    button_3 = "Часы"
    keyboard.add(button_3)
    button_4 = "/start"
    keyboard.add(button_4)
    await message.answer("Вот список изделий:\n*Шкатулка с любым размером, вырезкой и гравюровкой\n*Фотография, картина на дереве\n*Часы на стол любого размера, формы, с любым узором и цветом\n\nНапиши мне, что тебя заинтерисовало", reply_markup=keyboard)


@dp.message_handler(text=['Шкатулка'])
async def any_text_message(message: types.Message):
    with open('sk.jpg', 'rb') as photo_file:
        await message.answer_photo(photo_file, "Деревянная шкатулка ручной работы - сделана на заказ и единственная в своем роде! 💡 Добавьте нотку деревенского шарма в ваш дом с помощью нашей деревянной шкатулки ручной работы. Каждая шкатулка изготовлена на заказ и тщательно обработана умелыми руками с использованием традиционных техник. В результате получается уникальное и функциональное произведение искусства, идеально подходящее для хранения ваших самых ценных вещей.\n\nЦена определяется в зависимости от размера, формы и узоров\nот 1500руб.\n\nДля заказа пиши сюда: URL = 'https://t.me/argoncompany'")


@dp.message_handler(text=['Фотография'])
async def any_text_message(message: types.Message):
    with open('k.jpg', 'rb') as photo_file:
        await message.answer_photo(photo_file, "Привнесите нотку природы в интерьер вашего дома с помощью наших деревянных фотографий или картин ручной работы! 📷 Наши художники используют традиционную технику перевода фото на дерево, чтобы бережно воплотить в жизнь ваши заветные воспоминания. Каждый принт выполнен на заказ и демонстрирует естественную красоту дерева, создавая теплую и уютную атмосферу в любой комнате. Будь то особый момент с близкими или живописный пейзаж, мы поможем вам сохранить его действительно уникальным в своем роде способом. Закажите прямо сейчас и превратите ваши фотографии в произведение искусства! 🎨\n\nЦена определяется в зависимости от размера\nот 500руб.\n\nДля заказа пиши сюда: URL = 'https://t.me/argoncompany'")



@dp.message_handler(text=['Часы'])
async def any_text_message(message: types.Message):
    with open('w2.png', 'rb') as photo_file:
        await message.answer_photo(photo_file, "Представляем нашу самую большую на данный момент работу - величественный замок-часы из дерева, созданный нашим мастером с использованием техники витражной мозаики. Этот декоративный предмет является настоящим произведением искусства, который станет главным украшением любого интерьера. \nМы предлагаем вам возможность создать свои собственные часы из дерева с индивидуальным дизайном. Эти часы будут идеально подходить для вашего дома, офиса или любого другого места, где вы хотели бы их разместить. Наши часы изготавливаются только из высококачественных материалов, которые обеспечивают долговечность и надежность. Каждый заказ создаётся индивидуально, по вашим желаниям и требованиям.\n\nЦена определяется в зависимости от размера,  формы, сложности узоров и механизма часов\nот 5000руб.\n\nДля заказа пиши сюда: URL = 'https://t.me/argoncompany'")



@dp.message_handler(text="Я уже знаю, что хочу заказать")
async def cmd_start(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup()
    button_1 = types.KeyboardButton(text="Шкатулочка")
    keyboard.add(button_1)
    button_2 = "Фотография или картина"
    keyboard.add(button_2)
    button_3 = "Часы на стол"
    keyboard.add(button_3)
    button_4 = "/start"
    keyboard.add(button_4)
    # button_4 = "Назад"
    # keyboard.add(button_4, callback_data="Start")
    await message.answer("Что бы вы хотели к себе в дом?", reply_markup=keyboard)

@dp.message_handler(text=['Шкатулочка'])
async def any_text_message(message: types.Message):
   await message.answer("Пиши сюда:https://t.me/argoncompany, чтобы разработать свой дизайн вместе с мастером")

@dp.message_handler(text=['Фотография или картина'])
async def any_text_message(message: types.Message):
   await message.answer("Пиши сюда:https://t.me/argoncompany, чтобы отправить свою фотографию мастеру")

@dp.message_handler(text=['Часы на стол'])
async def any_text_message(message: types.Message):
   await message.answer("Пиши сюда:https://t.me/argoncompany, чтобы разработать свой дизайн вместе с мастером")

if __name__ == '__main__':
 executor.start_polling(dp)
