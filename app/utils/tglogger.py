from datetime import datetime

from aiogram import Bot

class TgLogger:
    """Ну типо логи"""
    def __init__(
        self,
        bot: Bot,
        log_chat: int

    ) -> None:
        self.logs: dict[int, str] = {}
        self.bot: Bot = bot
        self.log_chat = log_chat

    async def add_log(self, text: str) -> None:
        t = await self.__get_current_time()
        self.logs[len(self.logs.keys())+1] = f"{t}: {text}"

    async def remove_log(self, id: int):
        del self.logs[id]

    async def __get_current_time(self) -> str:
        return datetime.now().strftime("%H:%M:%S")

    async def compress_the_logs(self) -> str:
        return "\n".join(f"{v}" for v in self.logs.values())

    async def send_logs(self) -> None:
        if len(self.logs.keys()) == 0: return

        text = "Логи за текущую минуту: \n"
        text += await self.compress_the_logs()
        self.logs.clear()
        await self.bot.send_message(self.log_chat, text)
