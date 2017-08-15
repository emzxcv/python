from urllib.parse import urlencode
import discord
from discord.ext.commands import Bot

import secret


Heartbreaker_Bot = Bot(command_prefix="!")

@Heartbreaker_Bot.event
async def on_read():
    print ("Client logged in")


@Heartbreaker_Bot.command()
async def hello(*args):
    return await Heartbreaker_Bot.say("Hello world!")

@Heartbreaker_Bot.command()
async def python_help(*args):
    print(args)
    url = ("https://docs.python.org/3/search.html?{}&check_"
        "keywords=yes&area=default".format(
        urlencode({'q': ' '.join(args)})
        ))
    return await Heartbreaker_Bot.say(url)

Heartbreaker_Bot.run(secret.BOT_TOKEN)

