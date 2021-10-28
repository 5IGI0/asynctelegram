from .http import Http
from .user import User
from .chat import Chat
from .bot import Bot

class Message(object):
    
    def __init__(self, data: dict, bot: Bot=None):
        self.raw = data
        self.bot = bot

        if bot:
            self.http = self.bot

        self.author = User(data.get("from"), bot=bot) if data.get("from") else None
        self.chat = Chat(data.get("chat"), bot=bot)

        self.id = data.get("message_id")
        self.date = data.get("date")
        self.text = data.get("text")
