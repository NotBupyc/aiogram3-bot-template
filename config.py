from aiogram import Bot, Dispatcher
import os
from db.db import Userdb, BannedUserdb
from environs import load_dotenv

load_dotenv()

bot = Bot(token=os.getenv('BOT_TOKEN'))
dp = Dispatcher()

BASE_DIR = os.path.dirname(__file__)
PATH_TO_DB = os.path.join(BASE_DIR, 'db.db')

# DB
Users = Userdb()
BannedUsers = BannedUserdb()




