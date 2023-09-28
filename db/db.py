from sqlalchemy import select, and_, update
from sqlalchemy.ext.asyncio import AsyncSession, async_session, create_async_engine
from sqlalchemy.orm import sessionmaker
import typing
from .models import Base, Chat, User, BannedUser


class Chatdb:
    def __init__(self, db_name: str = "db.db"):
        self.engine = create_async_engine(f"sqlite+aiosqlite:///{db_name}")
        self.async_session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

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


class Userdb:
    def __init__(self, db_name: str = "db.db"):
        self.engine = create_async_engine(f"sqlite+aiosqlite:///{db_name}")
        self.async_session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

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
                and_(User.user_id == user_id)
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


class BannedUserdb:
    def __init__(self, db_name: str = "db.db"):
        self.engine = create_async_engine(f"sqlite+aiosqlite:///{db_name}")
        self.async_session = sessionmaker(
            self.engine, class_=AsyncSession, expire_on_commit=False
        )

    async def create_user(self, user_id: int) -> None:
        """Add user in db"""
        async with self.async_session() as s:
            u = User(user_id=user_id)
            s.add(u)
            await s.commit()

    async def delete_user(self, user_id: int) -> None:
        """Delete user from db"""
        async with self.async_session() as s:
            q = select(User).where(User.user_id == user_id)
            u = (await s.execute(q)).scalar()
            await s.delete(u)
            await s.commit()

    async def get_all(self) -> typing.Union[typing.List[BannedUser], list]:
        async with self.async_session() as s:
            q = select(BannedUser)
            all = (await s.execute(q)).fetchall()

            try:
                return [i[0].user_id for i in all]
            except:
                return []
