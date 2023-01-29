# import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove
# from config import API_TOKEN, HELP_COMMANDS, ALPHABET, DESCRIPTION
import config
import random

# logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1 = KeyboardButton("/random")
b2 = KeyboardButton("/image")
b3 = KeyboardButton("/count")
kb.add(b1).insert(b2).add(b3)

count = 1


async def on_startup(_):
    print("Bot is ready! Let's fxcking go!")


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message=types.Message):
    await message.answer(f"Hi, I'm <em>Echo BOT</em>!\n<b>Powered by aiogram.</b>",
                         parse_mode="HTML",
                         reply_markup=kb)
    await message.answer(config.HELP_COMMANDS, parse_mode="HTML")
    await message.delete()


@dp.message_handler(commands=['add'])
async def add_smth(message: types.Message):
    await message.answer(f"Что добавить?")
    await message.delete()


@dp.message_handler(commands=['random'])
async def random_letter(message: types.Message):
    await message.answer(f"Random letter: {random.choice(config.ALPHABET)}")
    await message.delete()


@dp.message_handler(commands=['description'])
async def description(message: types.Message):
    await message.answer(config.DESCRIPTION)
    await message.delete()


@dp.message_handler(commands=['count'])
async def counter(message: types.Message):
    global count
    await message.answer(f'Now count = {count}!')
    await message.delete()
    count += 1


@dp.message_handler(commands=["give"])
async def give_sticker(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker=config.STICKER_ID)
    await message.delete()


@dp.message_handler(commands=["image"])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.from_user.id,
                         photo="https://tipik.ru/wp-content/uploads/2019/06/"\
                               "%D0%9F%D0%B8%D0%BD%D0%B3%D0%B2%D0%B8%D0%BD%D1%8B-"\
                               "%D0%BD%D0%B0-%D1%80%D0%B0%D0%B1%D0%BE%D1%87%D0%B8%D0%B9"\
                               "-%D1%81%D1%82%D0%BE%D0%BB-%D0%BE%D0%B1%D0%BE%D0%B8-%D1%84%D0%BE%D0%BD018.jpg"
                         )
    await message.delete()


@dp.message_handler(commands=["location"])
async def send_point(message: types.Message):
    await bot.send_location(chat_id=message.from_user.id,
                            latitude=59.869132,
                            longitude=29.855710)
    await message.delete()


@dp.message_handler()
async def echo_upper(message: types.Message):
    counter = 0
    for i in message.text:
        if i == "✅":
            counter += 1

    await message.reply(f"There are {counter} checkmarks in your message!!!")

    if message.text == "❤️":
        await message.reply("🖤")
    
    if "0" in message.text:
        await message.reply(f'YES!')
    
    if message.text.count(' ') < 1:
        await message.reply(f"WTF, WHY ONLY ONE WORD?????")
        
    else:    
        await message.reply(message.text.upper() + "❤️")


@dp.message_handler(content_types=["sticker"])
async def send_sticker_id(message: types.Message):
    await message.reply(f"<b>ID for your sticker:</b> \n<em>{message.sticker.file_id}</em>", parse_mode="HTML")
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)  # Пропускать ответ на сообщения в оффлайне
