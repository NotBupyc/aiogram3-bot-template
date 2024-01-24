from aiogram import types, Router, Bot
from aiogram.filters import CommandStart
from app.messages import START

from app.db.models import User

router = Router()

@router.message(CommandStart())
async def start(message: types.Message, bot: Bot, user: User):
    text = START
    await message.answer(text=text)
