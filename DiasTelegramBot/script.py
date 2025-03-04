import asyncio, logging
from aiogram import Bot, Dispatcher
from config import TG_TOKEN
from handlers import router

async def main():
    bot = Bot(token = TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    try:
        asyncio.run(main())
    except KeyboardInterrupt as e:
        logger.info('Sayonara!')