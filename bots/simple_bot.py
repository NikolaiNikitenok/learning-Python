import logging
from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN, HELP_COMMANDS, ALPHABET, DESCRIPTION
import random

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

count = 1

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message=types.Message):
    await message.answer(f"Hi, I'm Echo BOT!\nPowered by aiogram.")
    await message.answer(HELP_COMMANDS)
    await message.delete()
    
@dp.message_handler(commands=['add'])
async def add_smth(message: types.Message):
    await message.answer(f"Что добавить?")
    await message.delete()
    
@dp.message_handler(commands=['random'])
async def random_letter(message: types.Message):
    await message.answer(f"Random letter: {random.choice(ALPHABET)}")
    await message.delete()
    
@dp.message_handler(commands=['description'])
async def description(message: types.Message):
    await message.answer(DESCRIPTION)
    await message.delete()
    
@dp.message_handler(commands=['count'])
async def counter(message: types.Message):
    global count
    await message.answer(f'Now count = {count}!')
    await message.delete()
    count += 1
    
@dp.message_handler()
async def echo_upper(message: types.Message):
    
    if "0" in message.text:
        await message.reply(f'YES!')
    
    if message.text.count(' ') < 1:
        await message.reply(f"WTF, WHY ONLY ONE WORD?????")
        
    else:    
        await message.reply(message.text.upper())
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)   