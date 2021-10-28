from .http import Http
from .bot import Bot

class User(object):

    def __init__(self, data: dict, bot: Bot=None):
        self.raw = data
        self.bot = bot

        if bot:
            self.http = bot.http

        self.first_name = data.get("first_name")
        self.last_name = data.get("last_name")
        self.username = data.get("username")
        self.language_code = data.get("language_code")
        self.is_bot = data.get("is_bot")
        self.id = data.get("id")

    async def send(self, text):
        return self.bot.send_message(self.id, text)