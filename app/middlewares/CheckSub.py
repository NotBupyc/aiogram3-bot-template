from aiogram import BaseMiddleware

from aiogram.types import TelegramObject
from typing import Dict, Awaitable, Callable, Any

from app.keyboards.inline import channels_not_sub
from app.messages import CHANNELS_NOT_SUB
from app.utils.misc import check_subs

class CheckSub(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]) -> Any:

        if event.callback_query and event.callback_query.data == "check_sub":
            return await handler(event, data)

        user = data['event_from_user']
        chan_not_sub = await check_subs(user.id, event.bot)

        if len(chan_not_sub) > 0:
            await event.bot.send_message(
                user.id,
                text=CHANNELS_NOT_SUB,
                reply_markup=channels_not_sub(chan_not_sub)
            )
        else:
            return await handler(event, data)
