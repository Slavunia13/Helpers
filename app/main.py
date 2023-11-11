import asyncio
from aiogram import Bot, Dispatcher
from handlers import start, booking, answer
import logging

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token="6842911878:AAEEm3-PRUrLV5pJMELdWaSohpkEs4WNbIo")
    dp = Dispatcher()
    dp.include_routers(start.router)
    dp.include_routers(booking.router)
    dp.include_routers(answer.router)

    print(1)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())