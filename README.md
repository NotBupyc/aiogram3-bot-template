# Aiogram3 Bot Template

---
## Оглавление
- [Системные требования](#системные-требования)
- [Начало работы](#начало-работы)
- [Регистрация хендлеров](#регистрация-хендлеров)
- [Создание мидлвери](#создание-мидлвери)
---
## Системные требования

- [Python 3.11+](https://www.python.org/)
- [PostgreSQL](https://www.postgresql.org/)
- [poetry](https://python-poetry.org/)

## Начало работы
1. Загрузите бота: `git clone https://github.com/NotBupyc/aiogram3-bot-template
2. Переименуйте файл `.env` и введите данные: `mv .env.example .env`
3. Установите зависимости командой `poetry install`
4. Создайте файл таблицы в базе данных `poetry python create_tables`

И запустите бота командой `poetry run bot`
___

## Использованные технологии
- [Aiogram 3.x](https://github.com/aiogram/aiogram) (Фреймворк для создания телеграм ботов
- [PostgreSQL](https://www.postgresql.org/) (База данных)
- [SQLAlchemy](https://docs.sqlalchemy.org/en/20/) (Работа с базой даных через бд)
- [Alembic](https://alembic.sqlalchemy.org/en/latest/) (Для создания миграций бд)
