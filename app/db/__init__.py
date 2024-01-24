from .engine import async_session, engine
from .funcs import Userdb, Chatdb, BannedUserdb, Channelsdb
from . import models

Chats = Chatdb(engine, async_session)
Users = Userdb(engine, async_session)
BannedUsers = BannedUserdb(engine, async_session)
Channels = Channelsdb(engine, async_session)
