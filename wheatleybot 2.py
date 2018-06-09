#Bot built by Noah, for Xander's Discord server

import discord
from discord.ext import commands
import asyncio
import chalk

prefix = "!"
bot = commands.Bot(command_prefix=prefix)

@bot.event
async def on_ready():
    print("Ready when you are!")

@bot.event
async def on_message(message):
    print("The message's content was: " + message.content)

    
@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("ponggggg!")
    await bot.say(str(ctx.message.channel))



@bot.command()
async def echo(ctx, *, content:str):
    await bot.say()


@bot.command()
async def channelnamevote(ctx.message)
    await 



bot.run("NDQ5NzA5NzEzOTE2MTY2MTQ0.Depjsg.PqAQCSS0ngFNKQvkCsWA3KiAKiE")
