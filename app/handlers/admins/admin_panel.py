import asyncio
import contextlib
import logging
from datetime import datetime

from aiogram import types, Router, Bot, F
from aiogram.filters import Command, CommandObject

from app.filters import IsAdmin
from app.config import dp, GIT_REPO
from app.messages import BOT_INFO
from app.utils.misc import run_command, bot_info_dict


router = Router()
logger = logging.getLogger(__name__)

# Взято у Джамиля(kawasaji) и Ополо(Opolo)
@router.message(
    Command('git'),
    IsAdmin()
)
async def git(message: types.Message, command: CommandObject, bot: Bot):
    """Ну типо обновление в боте"""
    git_message = await bot.send_message(message.chat.id, "🪛 *Ожидаем клонирования...*", parse_mode="Markdown")

    output, errors = await run_command(f"git pull {GIT_REPO}")

    await bot.edit_message_text(f"🪛 *Ожидаем клонирования...\n<b>Output:</b>\n<blockquote>{output}</blockquote>", git_message.chat.id,
                                git_message.message_id, )

    if "Already up to date.\n" not in output and "Уже актуально." not in output:
        await bot.send_message(message.chat.id,
                               f"*Выход!* _(⏰{datetime.now().strftime('%d.%m.%Y %H:%M:%S')})_",
                               parse_mode="Markdown")

        with contextlib.suppress(Exception):
            await dp.stop_polling()

        with contextlib.suppress(Exception):
            await dp.wait_closed()

    else:
        await bot.send_message(message.chat.id, f"*Файлы не затронуты, перезагрузка не требуется!*",
                               parse_mode="Markdown")
@router.message(
    Command('restart'),
    IsAdmin()
)
async def restart(message: types.Message):
    """Перезапускает бота"""
    with contextlib.suppress(Exception):
        await dp.stop_polling()

    with contextlib.suppress(Exception):
        await dp.wait_closed()

@router.message(
    Command("botinfo"),
    IsAdmin()
)
async def botinfo(message: types.Message):
    """Информация про бота и сервер"""

    m = await message.reply("🚀 <b>Получение данных...</b>")
    t = BOT_INFO.format(**await bot_info_dict())

    await asyncio.sleep(1)
    await m.edit_text(t)
