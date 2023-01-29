from aiogram import Bot, Dispatcher, executor, types
from bots import config

bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, )
