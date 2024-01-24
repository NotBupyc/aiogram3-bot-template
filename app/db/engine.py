import os

from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

# .env.example
IP = os.getenv('IP')
PGUSER = os.getenv('PGUSER')
PGPASSWORD = os.getenv('PGPASSWORD')
DATABASE = os.getenv('DATABASE')

POSTGRES_URL = f'postgresql+asyncpg://{PGUSER}:{PGPASSWORD}@{IP}/{DATABASE}'

# Создание подключение
engine = create_async_engine(POSTGRES_URL, future=True, poolclass=NullPool)
async_session = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)
