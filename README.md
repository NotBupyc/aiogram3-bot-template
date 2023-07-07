# Aiogram3 bot template

## Начало работы
1. Загрузите шаблон командой: `git clone https://github.com/NotBupyc/aiogram3-bot-template`
2. Зайдите в файл `.env`
```
BOT_TOKEN = YOUR_TOKEN
```
Подставьте токен своего бота

3. Создайте [venv](https://docs.python.org/3/library/venv.html)
4. Установите зависимости из requirements.txt: `pip install -r requirements.txt`
5. Запустите проект командой: `python main.py`
___
## Регистрация хендлеров
1. Зайдите в папку `handlers`
2. Зайдите в папку `users` или `admins`
3. Создайте файл `your_filename.py`
4. Создайте роутер в файле `your_filename.py`

```python
from aiogram import Router
from config import dp

router = Router()
dp.include_router(router)
```

Регистрирование хэндлеров декораторами:

```python
from aiogram.filters import Command
from aiogram import types

@router.message(Command('Your Command'))
async def cmd(message:types.Message):
    await message.reply("Your text")
```
## Туториалы с aiogram v3

Видосов пока нет, но @Groosha уже начал делать [свой учебник](https://mastergroosha.github.io/aiogram-3-guide/).

