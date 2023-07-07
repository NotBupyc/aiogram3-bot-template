from aiogram import types, Router, Bot
from aiogram.filters import CommandStart
from messages import START
from config import dp

router = Router()
dp.include_router(router)


@router.message(CommandStart())
async def start(message: types.Message, bot: Bot):
    text = START
    await message.answer(text=text)
