# Imports


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Chat(Base):
    __tablename__ = "chats"

    id = Column(Integer(), primary_key=True)
    chat_id = Column(Integer(), nullable=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), nullable=False, default=0)

class BannedUser(Base):
    __tablename__ = 'banned_users'

    id = Column(Integer(), primary_key=True)
    user_id = Column(Integer(), nullable=False)


