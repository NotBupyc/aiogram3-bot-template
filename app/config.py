from aiogram import Bot, Dispatcher
import os

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

from app.db import (
    Users,
    BannedUsers,
    Chats
)
from app.utils.tglogger import TgLogger

# env
TOKEN = os.getenv('BOT_TOKEN')
GIT_REPO = os.getenv('GIT_REPO')
LOG_CHAT = os.getenv('LOG_CHAT')

# aiogram
bot = Bot(token=TOKEN, parse_mode='HTML')
dp = Dispatcher()

BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(os.path.dirname(BASE_DIR), 'assets')

#
admins: list[int] = [admins_id]
TgLogger = TgLogger()


