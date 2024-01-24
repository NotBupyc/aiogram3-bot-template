import asyncio
import tracemalloc
from datetime import datetime

from aiogram import Bot
import logging

from apscheduler.schedulers.asyncio import AsyncIOScheduler

# Config
from app.config import admins, LOG_CHAT, TgLogger
from app.utils.misc import disabled_loggers

logger = logging.getLogger('root')
scheduler = AsyncIOScheduler()

logging.basicConfig(
    level=logging.INFO,
    format="%(name)s %(asctime)s %(levelname)s %(message)s")

# Отключения дефолтных логеров
loggers_for_disabled = [
    "apscheduler.executors.default",
    "apscheduler.scheduler",
    "aiogram.dispatcher",
    "aiogram.event",
]

disabled_loggers(loggers_for_disabled)

async def on_startup(bot: Bot):
    user = await bot.me()
    logger.info(f'{user.first_name}(id={user.id}) was started!')

    # tasks
    scheduler.add_job(TgLogger.send_logs, trigger="interval", minutes=1)

    logger.info(f'Tasks was added')

    scheduler.start()

    await bot.send_message(LOG_CHAT,
                           f"*Вход!* _(⏰{datetime.now().strftime('%d.%m.%Y %H:%M:%S')})_",
                           parse_mode="Markdown")

async def on_shutdown(bot: Bot):
    scheduler.shutdown()
    await bot.send_message(LOG_CHAT,
                           f"*Бот отключен* _(⏰{datetime.now().strftime('%d.%m.%Y %H:%M:%S')})_",
                           parse_mode="Markdown")

async def _main():
    from app.config import dp, bot

    import app.middlewares


    from app.handlers import routers

    dp.include_routers(*routers)

    await bot.delete_webhook(drop_pending_updates=True)
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)

    await dp.start_polling(bot)


def main():
    asyncio.run(_main())

if __name__ == '__main__':
    main()
