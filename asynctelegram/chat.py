from .http import Http
from .bot import Bot

from typing import Union

class Chat(object):

    def __init__(self, data: dict, bot: Bot=None):
        self.raw = data
        self.bot = bot

        if bot:
            self.http: Http = bot.http

        self.id: int = data.get("id")
        self.type: str = data.get("type")
        self.title: Union[str, None] = data.get("title")
        self.username: Union[str, None] = data.get("username")
        self.first_name: Union[str, None] = data.get("first_name")
        self.last_name: Union[str, None] = data.get("last_name")

    async def send(self, text):
        return await self.bot.send_message(self.id, text)