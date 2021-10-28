from asynctelegram import Bot
from os import environ

class MyBot(Bot):
    async def on_login(self):
        print(f"logged in as {self.user.username}")

bot = MyBot()

# Decorator's parameters:
#   name[str]       : Command name           | Default: Function's name
#   description[str]: Command Description    | Default: "no description"
#   hide[bool]      : Is the function hidden | Default: False
#                     on the autocomplation
@bot.command(hide=True)
async def start(ctx, args):
    cliched_sentences = {
        "fr": "hon hon hon, j'aime les baguettes",
        "ru": "vodka!"
    }

    lang = ctx.author.language_code

    await ctx.send(cliched_sentences[lang] if cliched_sentences.get(lang) is not None else "hello")

@bot.command(name="ping", description="ping the bot")
async def ping(ctx, args):
    await ctx.send("pong")

@bot.command(hide=True)
async def shutdown(ctx, args):
    await ctx.send("bye")
    bot.stop()

bot.start(environ["TOKEN"])