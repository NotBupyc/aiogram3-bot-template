Регистрирование хэндлеров декораторами:

```python
from aiogram.filters import Command
from aiogram import types, Router

router = Router()

@router.message(Command('Your Command'))
async def cmd(message:types.Message):
    await message.reply("Your text")
```

Файл `__init__.py`:
```python
from . import (
    your_filename
)

routers = [
    your_filename.router,
]

```