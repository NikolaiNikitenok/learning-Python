import logging

from aiogram import Bot, Dispatcher, executor, types

from config import API_TOKEN

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message=types.Message):
    await message.reply(f"Hi, I'm Echo BOT!\nPowered by aiogram.")
    
@dp.message_handler()
async def echo_upper(message: types.Message):
    await message.answer(message.text.upper())  # UpperCase simbols
    
    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)   