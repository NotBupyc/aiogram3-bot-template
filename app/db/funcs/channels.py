from datetime import timedelta, datetime
import typing

from sqlalchemy import select, update, desc, func
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker, aliased, joinedload, selectinload

from app.db.models import (
    ChannelsForSub,
)

class Channelsdb:
    def __init__(
        self,
        engine: AsyncEngine,
        async_session: sessionmaker
    ):
        self.engine = engine
        self.async_session = async_session

    async def create_channel(
        self,
        link: str
    ) -> None:
        """Add user in db"""
        async with self.async_session() as s:
            u = ChannelsForSub(
                link=link
            )
            s.add(u)
            await s.commit()

    async def get_channel(self, link: str) -> typing.Optional[ChannelsForSub]:
        async with self.async_session() as s:
            q = select(ChannelsForSub).where(
                ChannelsForSub.link == link
            )
            u = await s.execute(q)

            try:
                return u.fetchone()[0]
            except TypeError:
                return None

    async def get_all(self) -> typing.Union[typing.List[ChannelsForSub], list]:
        async with self.async_session() as s:
            q = select(ChannelsForSub)
            _all = (await s.execute(q)).fetchall()

            try:
                return [i[0] for i in _all]
            except:
                return []

    async def delete_channel(self, link:str) -> None:
        """Delete user from db"""
        async with self.async_session() as s:
            q = select(ChannelsForSub).where(ChannelsForSub.link == link)
            u = (await s.execute(q)).scalar()
            await s.delete(u)
            await s.commit()
