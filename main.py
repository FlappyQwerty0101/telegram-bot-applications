import asyncio
import logging

from aiogram import Bot, Dispatcher

from config import TOKEN
from handlers import user, admin
from database.db import init_db

bot = Bot(token=TOKEN)
dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)

    dp.include_routers(user.router, admin.router)
    await init_db()
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')