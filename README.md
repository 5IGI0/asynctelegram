# AsyncTelegram

_A simple library to create telegram bot._

# Getting Started

## Installation

1. Install the package with pip
```
pip install asynctelegram
```
2. Code!

```python

from asynctelegram import Bot

class MyBot(Bot):
    def on_login(self):
        print("logged in as", self.user.username)

bot = MyBot()

@bot.command(name="ping", description="pong!")
async def ping(ctx, args): 
    await ctx.send("pong!")

bot.start("<your token>")
```

unfortunately for the moment there is no documentation.\
you can help yourself with the [example codes](examples/).\
or you can [contact me](#contact)

# Contribute

## note
to contribute do what you can, only one thing to respect, if your code risks to break the bots which use this library, do not make it on ``master`` use rather ``unstable`` so that it is added to the next major update

## before contributing
before contributing you need to know where to find the telegram documentation, so [here](https://core.telegram.org/bots/api) it is

# Contact

- Discord: 5IGI0#1429
- [telegram](https://t.me/s5IGI0)