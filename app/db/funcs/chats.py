from datetime import timedelta, datetime
import typing

from sqlalchemy import select, update, desc, func
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker, aliased, joinedload, selectinload

from app.db.models import (
    Chat,
)

class Chatdb:
    def __init__(
        self,
        engine: AsyncEngine,
        async_session: sessionmaker
    ):
        self.engine = engine
        self.async_session = async_session

    async def create_chat(self, server_id: int) -> None:
        """Add server in db"""
        async with self.async_session() as s:
            guild = Chat(chat_id=server_id)
            s.add(guild)
            await s.commit()

    async def delete_chat(self, server_id: int) -> None:
        """Delete server from db"""
        async with self.async_session() as s:
            q = select(Chat).where(Chat.chat_id == server_id)
            guild = (await s.execute(q)).scalar()
            # user = user.scalar()
            await s.delete(guild)
            await s.commit()

    async def get_chat(self, server_id: int) -> typing.Optional[Chat]:
        """Get server info from db"""
        async with self.async_session() as s:
            q = select(Chat).where(Chat.chat_id == server_id)
            u = await s.execute(q)

            try:
                return u.fetchone()[0]
            except TypeError:
                return None


    async def get_all(self) -> typing.Union[typing.List[Chat], list]:
        async with self.async_session() as s:
            q = select(Chat)
            all = (await s.execute(q)).fetchall()

            try:
                return [i[0].chat_id for i in all]
            except:
                return []
