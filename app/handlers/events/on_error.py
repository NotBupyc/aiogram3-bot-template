import html
import traceback
import logging

from aiogram import Router
from aiogram.handlers import ErrorHandler
from aiogram.types import ErrorEvent

from app.db.models import User
from app.config import LOG_CHAT
from app.utils.misc import run_command, bot_info_dict

router = Router()
logger = logging.getLogger(__name__)

# @router.errors()
# async def errors_handler(update: types.Update, exception: Exception, bot: Bot, user: User):
#     await bot.send_message(admins[1], f"Произошла ошибка: \n{exception}, \Юзер: {user.id} ({user.name})")

@router.errors()
async def error_handler(exception: ErrorEvent):
    update = exception.update
    user = update.callback_query or exception.update.message
    user = user.from_user

    if update.message is not None and getattr(update.message, "text"):
        text = update.message.text

    else:
        text = update.callback_query.message.text

    callback_data = getattr(update.callback_query, 'data', 'Отсуствует')
    exc = "\n".join(traceback.format_exc().splitlines()[-7:])
    # logger.info(text)
    t = ("Произошла ошибка в inline: \n"
         f"Текст сообщения: <blockquote>{html.escape(text)}</blockquote>\n"
         f'data: <blockquote>{callback_data}</blockquote> \n'
         f'Ошибка: \n<pre><code class="language-py">{html.escape(exc)}</code></pre>\n'
         f"Юзер: {html.escape(user.first_name)} ({user.id})"
         )
    logger.info(traceback.format_exc())

    await update.bot.send_message(LOG_CHAT, t)
