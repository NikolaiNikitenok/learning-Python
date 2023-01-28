import asyncio
from aiogram import Bot, Dispatcher, types


async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)}?!", parse_mode=types.ParseMode.HTML,
    )
    

async def how_handler(event: types.Message):
    await event.answer(
        f"Okay, i'm ready!"
    )
    
    
async def main():
    bot = Bot(token="5987927045:AAFpCElru0cA794E3NJqwi8Zx0KRYgXMxgM")
    print("In progress!")
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        
        disp.register_message_handler(how_handler, commands="go")
        
        await disp.start_polling()
    finally:
        await bot.close()

asyncio.run(main())
