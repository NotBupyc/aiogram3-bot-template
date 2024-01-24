# Мидлвери
---
## Список мидлвери
- [IgnoreBannedUsers](#ignorebannedusers)
- [CheckSub](#checksub)
- [GetUserInHandler](#getuserinhandler)

## IgnoreBannedUsers
Игнориует пользователей если они находятся в базе игнора

## CheckSub
Проверяет есть ли человек в канале(ах), если нет просит его подписаться

## GetUserInHandler
Самый ахуенный мидлвери, передает класс User в хендлер

```py
from app.db.models import User
from aiogram import Router, types

router = Router()

@router.message()
async def test_handler(message: types.Message, user: User):
    pass
```

