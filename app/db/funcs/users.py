from datetime import timedelta, datetime
import typing

from sqlalchemy import select, update, desc, func
from sqlalchemy.ext.asyncio import AsyncEngine
from sqlalchemy.orm import sessionmaker, aliased, joinedload, selectinload

from app.db.models import (
    User,
)

class Userdb:
    def __init__(
        self,
        engine: AsyncEngine,
        async_session: sessionmaker
        ):
        self.engine = engine
        self.async_session = async_session

    async def create_user(
            self,
            user_id: int,

    ) -> None:
        """Add user in db"""

        async with self.async_session() as s:
            u = User(
                user_id=user_id,)
            s.add(u)
            await s.commit()

    async def delete_user(self, user_id: int) -> None:
        """Delete user from db"""
        async with self.async_session() as s:
            q = select(User).where(
                User.user_id == user_id
            )
            u = (await s.execute(q)).scalar()
            await s.delete(u)
            await s.commit()

    async def get_user(self, user_id: int) -> typing.Optional[User]:
        """Get info a user from db"""
        async with self.async_session() as s:
            q = select(User).where(User.user_id == user_id)
            u = await s.execute(q)

            try:
                return u.fetchone()[0]
            except TypeError:
                return None

    async def get_all(self) -> typing.Union[typing.List[User], list]:
        async with self.async_session() as s:
            q = select(User)
            all = (await s.execute(q)).fetchall()

            try:
                return [i[0].user_id for i in all]
            except:
                return []
