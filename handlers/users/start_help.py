from aiogram import types, Router, Bot
from aiogram.filters import CommandStart
from messages import START
from config import dp
from db.models import User

router = Router()
dp.include_router(router)


@router.message(CommandStart())
async def start(message: types.Message, bot: Bot, user: User):
    text = START
    await message.answer(text=text)
