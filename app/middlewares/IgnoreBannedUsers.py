from aiogram import BaseMiddleware
from aiogram.types import Message, TelegramObject
from typing import Dict, Awaitable, Callable, Any

import os
import sys

from config import BannedUsers, dp
class IgnoreBannedUser(BaseMiddleware):
    async def __call__(
            self,
            handler: Callable[[TelegramObject, Dict[str, Any]], Awaitable[Any]],
            event: TelegramObject,
            data: Dict[str, Any]) -> Any:

        if event.inline_query:
            user_id = event.inline_query.message.from_user.id

        elif event.message:
            user_id = event.message.from_user.id
        else:
            user_id = 0

        if user_id not in await BannedUsers.get_all():
            return await handler(event, data)

dp.update.middleware.register(IgnoreBannedUser())