import time
import asyncio
import contextlib
import html
import logging
import os
import platform
import subprocess
import sys
import time
from datetime import datetime, timedelta
from typing import Any, Literal

import aiogram
import psutil
from aiogram import Bot

from app.db import Channels, Users, BannedUsers
from app.db.models import User


time_st = time.perf_counter()
logger = logging.getLogger('root')

async def run_command(cmd: str, echo=False) -> tuple[str, str]:
    """Нужна для команды /git"""
    cmd = cmd.split()

    pull_result = subprocess.Popen(cmd, stdout=subprocess.PIPE,
                                   text=True, stderr=subprocess.PIPE)
    output, errors = pull_result.communicate(input="Hello from the other side!")
    pull_result.wait()

    if echo:
        print('Output', output, 'Errors', errors)

    return (output, errors)

def check_timestamp(time_in_timestamp: float) -> bool:
    """
    :param time_in_timestamp:
    :return: True если дата в time больше чем сегодняшняя
    """

    if not time_in_timestamp:
        return False

    if time_in_timestamp == 1:
        return True

    now = datetime.now()
    date = datetime.fromtimestamp(time_in_timestamp)

    if (date-now) > timedelta(seconds=1):
        return True

    return False


def convert_timestamp_to_str(time_timestamp:float) -> str:
    if time_timestamp == 1:
        return "Навсегда"

    date = datetime.fromtimestamp(time_timestamp)
    now = datetime.now()
    if (date - now) >= timedelta(days=1):
        d = date.strftime('%w.%m.%y')
        return f'{d} ({(date - now).days} дней)'
    d = (date - now)
    return str(d).split(".")[0]

async def check_subs(user_id: int, bot: Bot) -> list[str]:
    """Проверяет на сколько каналов не подписан юзер"""
    all_channels = await Channels.get_all()

    chan_not_sub = []

    for i in all_channels:

        chat_member = await bot.get_chat_member(i.link, user_id)

        if chat_member.status == "left":
            chan_not_sub.append(i.link)

    return chan_not_sub

def uptime() -> int:
    """
    Returns bot uptime in seconds
    :return: Uptime in seconds
    """
    return round(time.perf_counter() - time_st)

# спизжено с хикки
def formatted_uptime() -> str:
    """
    Returnes formmated uptime
    :return: Formatted uptime
    """
    return str(timedelta(seconds=uptime()))

def bytes_to_megabytes(b: int) -> int:
    return round(b / 1024 / 1024, 1)

async def bot_info_dict() -> dict:
    """Возращает данные про бота и серв"""
    inf = {
        "cpu": "n/a",
        "cpu_load": "n/a",
        "ram": "n/a",
        "ram_load_mb": "n/a",
        "ram_load": "n/a",
        "arch_emoji": "n/a",
        "arch": "n/a",
        "os": "n/a",

        "python": "n/a",
        "aiogram": aiogram.__version__,

        "process_ram": "n/a",
        "process_ram_percent"
        "process_cpu_percent": "n/a",

        "bot_working": formatted_uptime(),

        "users_in_bd": "n/a",
        "users_in_ignore": "n/a"

    }

    with contextlib.suppress(Exception):
        inf["cpu"] = psutil.cpu_count(logical=True)

    with contextlib.suppress(Exception):
        inf["cpu_load"] = psutil.cpu_percent()

    with contextlib.suppress(Exception):
        inf["ram"] = bytes_to_megabytes(
            psutil.virtual_memory().total - psutil.virtual_memory().available
        )

    with contextlib.suppress(Exception):
        inf["ram_load_mb"] = bytes_to_megabytes(psutil.virtual_memory().total)

    with contextlib.suppress(Exception):
        inf["ram_load"] = psutil.virtual_memory().percent

    with contextlib.suppress(Exception):
        inf["arch"] = html.escape(platform.architecture()[0])

    inf["arch_emoji"] = (
        "<emoji document_id=5172881503478088537>💻</emoji>"
        if "64" in (inf.get("arch", "") or "")
        else "<emoji document_id=5174703196676817427>💻</emoji>"
    )

    with contextlib.suppress(Exception):
        system = os.popen("cat /etc/*release").read()
        b = system.find('DISTRIB_DESCRIPTION="') + 21
        system = system[b: system.find('"', b)]
        inf["os"] = html.escape(system)

    with contextlib.suppress(Exception):
        inf["python"] = (
            f"{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}"
        )
    # process
    process = psutil.Process()

    with contextlib.suppress(Exception):
        inf['process_ram'] = bytes_to_megabytes(process.memory_info().rss)

    with contextlib.suppress(Exception):
        inf['process_ram_percent'] = round(process.memory_percent(), 1)

    with contextlib.suppress(Exception):
        inf['process_cpu_percent'] = round(process.cpu_percent(),1)

    inf['users_in_bd'] = len(await Users.get_all())
    inf['users_in_ignore'] = len(await BannedUsers.get_all())

    return inf


def disabled_loggers(loggers: list[str]):
    """Отключает некоторые стандартные логеры"""
    for log in loggers:
        l = logging.getLogger(log)
        l.disabled = True
    else:
        logger.info('Default loggers was disabled')
