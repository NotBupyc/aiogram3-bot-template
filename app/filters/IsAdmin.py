from typing import Union

from aiogram.filters import BaseFilter
from aiogram.types import Message

from app.config import admins

class IsAdmin(BaseFilter):
    def __init__(self):
        pass

    async def __call__(self, message: Message) -> bool:
        if message.from_user.id in admins:
            return True
        return False
