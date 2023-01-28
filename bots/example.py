import asyncio
from aiogram import Bot, Dispatcher, types


async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} ?!", parse_mode=types.ParseMode.HTML,
    )
    
    
async def main():
    bot = Bot(token=BOT-TOKEN)
    try:
        disp = Dispatcher(bot=bot)
        disp.register_message_handler(start_handler, commands={"start", "restart"})
        await disp.start_polling()
    finally:
        await bot.close()
        
asyncio.run(main())
