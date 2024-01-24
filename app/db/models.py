# Imports
from sqlalchemy import Column, Integer, String, INTEGER
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class BaseModel(Base):
    __abstract__ = True

    id = Column(INTEGER, nullable=False, primary_key=True)

    def __repr__(self):
        return "<{0.__class__.__name__}(id={0.id!r})>".format(self)

    @property
    def to_dict(self) -> dict:
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

    async def save(self, session: AsyncSession):
        session.add(self)
        await session.commit()

    async def delete(self, session: AsyncSession):
        await session.delete(self)
        await session.commit()


class Chat(BaseModel):
    __tablename__ = "chats"

    chat_id = Column(Integer(), nullable=False)


class User(BaseModel):
    __tablename__ = "users"

    user_id = Column(Integer(), nullable=False, default=0)

class BannedUser(BaseModel):
    __tablename__ = 'banned_users'

    user_id = Column(Integer(), nullable=False)

class ChannelsForSub(BaseModel):
    __tablename__ = 'channels'

    link = Column(String(), nullable=False)
